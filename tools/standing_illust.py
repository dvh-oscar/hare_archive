import argparse
import shutil

from pathlib import Path
from PIL import Image, ImageDraw
from multiprocessing import Process


input_folder = Path("./tools/workdir/inputs").resolve()
grid_folder = Path("./tools/workdir/grid").resolve()
output_folder = Path("./tools/workdir/outputs").resolve()


def process_image(image_file):
    TARGET_WIDTH = 4096
    TARGET_HEIGHT = 4096
    origin_image = Image.open(image_file)
    grid_image = Image.new("RGB", (TARGET_WIDTH, TARGET_HEIGHT), (50, 50, 50))
    output_image = Image.new("RGBA", (TARGET_WIDTH, TARGET_HEIGHT), (0, 0, 0, 0))

    paste_x = (TARGET_WIDTH - origin_image.width) // 2
    paste_y = (TARGET_HEIGHT - origin_image.height) // 2

    output_image.paste(origin_image, (paste_x, paste_y))

    grid_image.paste(origin_image, (paste_x, paste_y))
    draw = ImageDraw.Draw(grid_image)
    draw.line(
        [(0, TARGET_HEIGHT // 2), (TARGET_WIDTH, TARGET_HEIGHT // 2)], (255, 0, 0), 10
    )

    draw.line(
        [(TARGET_WIDTH // 2, 0), (TARGET_WIDTH // 2, TARGET_HEIGHT)], (255, 0, 0), 10
    )
    output_image.save(output_folder / image_file.name, "PNG")
    grid_image.save(grid_folder / image_file.name, "PNG")


if "__main__" == __name__:
    print("Hello World!")

    # print(folder)
    print(input_folder.is_dir())

    for dir in [output_folder, grid_folder]:
        # dir의 내용물이 있어도 지우고 다시 생성할 것
        if dir.exists():
            shutil.rmtree(dir)
        dir.mkdir(parents=True, exist_ok=True)

    thread_list = []
    for image_file in input_folder.iterdir():
        
        thread = Process(target = process_image, args=(image_file,))
        thread.start()
        thread_list.append(thread)
        # break

    for thread in thread_list:
        thread.join()


