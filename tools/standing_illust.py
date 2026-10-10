import argparse
import shutil

from pathlib import Path
from PIL import Image, ImageDraw
from multiprocessing import Pool, cpu_count
import traceback
import json


# input_folder = Path("./tools/workdir/inputs").resolve()
grid_folder = Path("./tools/workdir/grid").resolve()
output_folder = Path("./game/images/characters").resolve()




def normalize_facial_entry(entry):
    if isinstance(entry, str):
        return {"name": entry, "dx": 0, "dy": 0}
    elif isinstance(entry, dict):
        name = entry.get("name")
        offset = entry.get("offset", {})
        dx = offset.get("dx", entry.get("dx", 0))
        dy = offset.get("dy", entry.get("dy", 0))
        return {"name": name, "dx": dx, "dy": dy}
    return {"name": None, "dx": 0, "dy": 0}


def get_merged_facials(character_key, char_config, common_facial_data):
    merged = {}

    # 1. 000_common.json
    for code, val in common_facial_data.items():
        merged[code] = normalize_facial_entry(val)

    # 2. tools/facial_maps/{character}.json (별도 json)
    char_facial_file = Path("./tools/facial_maps", f"{character_key}.json").resolve()
    if char_facial_file.exists():
        try:
            char_data = json.loads(char_facial_file.read_text(encoding="utf-8"))
            for code, val in char_data.items():
                norm = normalize_facial_entry(val)
                if code in merged:
                    existing = merged[code].copy()
                    if norm["name"] is not None:
                        existing["name"] = norm["name"]
                    if isinstance(val, dict) and ("offset" in val or "dx" in val or "dy" in val):
                        existing["dx"] = norm["dx"]
                        existing["dy"] = norm["dy"]
                    merged[code] = existing
                else:
                    merged[code] = norm
        except Exception as e:
            print(f"[WARNING] Failed to load facial map for {character_key}: {e}")

    # 3. config.json의 facials
    if "facials" in char_config and isinstance(char_config["facials"], dict):
        for code, val in char_config["facials"].items():
            norm = normalize_facial_entry(val)
            if code in merged:
                existing = merged[code].copy()
                if norm["name"] is not None:
                    existing["name"] = norm["name"]
                if isinstance(val, dict) and ("offset" in val or "dx" in val or "dy" in val):
                    existing["dx"] = norm["dx"]
                    existing["dy"] = norm["dy"]
                merged[code] = existing
            else:
                merged[code] = norm

    return merged


def process_image(image_file, config, facials):
    try:
        TARGET_WIDTH = 3000
        TARGET_HEIGHT = 4096
        HEIGHT_RATIO = 0.25
        origin_image = Image.open(image_file)
        grid_image = Image.new("RGB", (TARGET_WIDTH, TARGET_HEIGHT), (50, 50, 50))
        output_image = Image.new("RGBA", (TARGET_WIDTH, TARGET_HEIGHT), (0, 0, 0, 0))

        if "_default_" in image_file.name:
            facial_code = image_file.name.split("_default_")[-1].split(".png")[0]
        else:
            facial_code = image_file.stem

        facial_info = facials.get(facial_code)
        if facial_info is not None and facial_info.get("name") is not None:
            facial_name = facial_info["name"]
        else:
            facial_name = "facial_" + facial_code

        char_dx = config.get("dx", 0)
        char_dy = config.get("dy", 0)
        facial_dx = facial_info.get("dx", 0) if facial_info else 0
        facial_dy = facial_info.get("dy", 0) if facial_info else 0

        paste_x = (TARGET_WIDTH - origin_image.width) // 2 + char_dx + facial_dx
        paste_y = int(HEIGHT_RATIO * TARGET_HEIGHT - 0.5 * origin_image.height) + char_dy + facial_dy

        output_image.paste(origin_image, (paste_x, paste_y))

        grid_image.paste(origin_image, (paste_x, paste_y))
        draw = ImageDraw.Draw(grid_image)
        draw.line(
            [(0, int(TARGET_HEIGHT * HEIGHT_RATIO)), (TARGET_WIDTH, int(TARGET_HEIGHT * HEIGHT_RATIO))], (255, 0, 0), 10
        )

        draw.line(
            [(TARGET_WIDTH // 2, 0), (TARGET_WIDTH // 2, TARGET_HEIGHT)], (255, 0, 0), 10
        )

        filename = (config["id"] + " " + facial_name).strip() + ".png"
        output_image.save(output_folder / config["id"] / filename, "PNG")
        grid_image.save(grid_folder / config["id"] / filename, "PNG")
    except Exception as e:
        print(f"[ERROR] {image_file}: {e}")
        traceback.print_exc()


if "__main__" == __name__:
    print("Hello World!")

    if grid_folder.exists():
        shutil.rmtree(grid_folder)
    grid_folder.mkdir(parents=True, exist_ok=True)

    print("delete previous data")

    tasks = []

    config_path = Path("./tools/workdir/config.json").resolve()
    config_data = json.loads(config_path.read_text(encoding="utf-8"))

    common_facial_file = Path("./tools/facial_maps/000_common.json").resolve()
    common_facial_data = json.loads(common_facial_file.read_text(encoding="utf-8")) if common_facial_file.exists() else {}

    for character, char_config in config_data.items():
        input_folder = Path("BaSpines", character).resolve()
        if not input_folder.exists():
            print(f"[WARNING] Input folder not found: {input_folder}")
            continue

        char_output_folder = output_folder / char_config["id"]
        if char_output_folder.exists():
            shutil.rmtree(char_output_folder)
        char_output_folder.mkdir(parents=True, exist_ok=True)

        grid_output_folder = grid_folder / char_config["id"]
        grid_output_folder.mkdir(parents=True, exist_ok=True)

        merged_facials = get_merged_facials(character, char_config, common_facial_data)

        for image_file in input_folder.iterdir():
            if image_file.is_file() and image_file.suffix.lower() == ".png":
                tasks.append((image_file, char_config, merged_facials))

    print(f"병렬 처리 중... (workers: {cpu_count()}, tasks: {len(tasks)})")

    with Pool(processes=cpu_count()) as pool:
        pool.starmap(process_image, tasks)

