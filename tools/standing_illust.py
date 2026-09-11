import argparse
import shutil

from pathlib import Path
from PIL import Image, ImageDraw
from multiprocessing import Process
import json


# input_folder = Path("./tools/workdir/inputs").resolve()
grid_folder = Path("./tools/workdir/grid").resolve()
output_folder = Path("./game/images/characters").resolve()




def process_image(image_file, config, facial):
    TARGET_WIDTH = 3000
    TARGET_HEIGHT = 4096
    HEIGHT_RATIO = 0.25
    origin_image = Image.open(image_file)
    grid_image = Image.new("RGB", (TARGET_WIDTH, TARGET_HEIGHT), (50, 50, 50))
    output_image = Image.new("RGBA", (TARGET_WIDTH, TARGET_HEIGHT), (0, 0, 0, 0))

    paste_x = (TARGET_WIDTH - origin_image.width) // 2 + config["dx"]
    paste_y = int(HEIGHT_RATIO * TARGET_HEIGHT - 0.5 * origin_image.height) + config["dy"]

    output_image.paste(origin_image, (paste_x, paste_y))

    grid_image.paste(origin_image, (paste_x, paste_y))
    draw = ImageDraw.Draw(grid_image)
    draw.line(
        [(0, int(TARGET_HEIGHT * HEIGHT_RATIO)), (TARGET_WIDTH, int(TARGET_HEIGHT * HEIGHT_RATIO))], (255, 0, 0), 10
    )

    draw.line(
        [(TARGET_WIDTH // 2, 0), (TARGET_WIDTH // 2, TARGET_HEIGHT)], (255, 0, 0), 10
    )

    facial_code = image_file.name.split("_default_")[-1].split(".png")[0]

    facial_name = "faicial_" + facial_code

    if facial_code in facial.keys():
        facial_name = facial[facial_code]



    filename = (config["id"] + " " + facial_name).strip() + ".png"
    output_image.save(output_folder / config["id"] / filename, "PNG")
    grid_image.save(grid_folder / config["id"] / filename, "PNG")


if "__main__" == __name__:
    print("Hello World!")

    # print(folder)
    # print(input_folder.is_dir())

    

    # 폴더 초기화
    # for dir in [output_folder, grid_folder]:
    #     # dir의 내용물이 있어도 지우고 다시 생성할 것
    #     if dir.exists():
    #         shutil.rmtree(dir)
    #     dir.mkdir(parents=True, exist_ok=True)

    if grid_folder.exists():
        shutil.rmtree(grid_folder)
    grid_folder.mkdir(parents=True, exist_ok=True)


    
    print("delete previous data")
    

    thread_list = []

    # common_facial_data = json.loads(Path("./tools/facial_maps/000_common.json").resolve().read_text())
    config_data = json.loads(Path("./tools/workdir/config.json").resolve().read_text())
    common_facial_data = json.loads(Path("./tools/facial_maps/000_common.json").resolve().read_text())

    for character in config_data.keys():
        input_folder = Path("BaSpines", character).resolve()
        char_output_folder = output_folder / config_data[character]["id"]

        if char_output_folder.exists():
            shutil.rmtree(char_output_folder)
        char_output_folder.mkdir(parents = True, exist_ok = True)

        grid_output_folder = grid_folder / config_data[character]["id"]
        grid_output_folder.mkdir(parents = True, exist_ok = True)


        facial_data = common_facial_data
        char_facial_data = Path("./tools/facial_maps", character + ".json").resolve()
        if char_facial_data.exists():
            facial_data = json.loads(char_facial_data.read_text())

        # if char_data.exists():
        #     config_data = json.loads(char_data.read_text())


        for image_file in input_folder.iterdir():
            thread = Process(target = process_image, args=(image_file, config_data[character], facial_data))
            thread.start()
            thread_list.append(thread)
            # break
            

    print("병렬 처리 중...")

    for thread in thread_list:
        thread.join()


