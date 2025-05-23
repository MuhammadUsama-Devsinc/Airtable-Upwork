from rembg import remove
from PIL import Image
import io
import os

def pre_process_image(image_path):
    with open(image_path, "rb") as input_file:
        input_data = input_file.read()

    output_data = remove(input_data)
    output_image = Image.open(io.BytesIO(output_data))
    output_image = output_image.convert("RGBA")

    width, height = output_image.size
    if not (width == height):
        max_dim = max(width, height)
        square_image = Image.new("RGBA", (max_dim, max_dim), (0, 0, 0, 0))
        paste_position = ((max_dim - width) // 2, (max_dim - height) // 2)
        square_image.paste(output_image, paste_position, output_image)
        output_image = square_image

    image_name, image_extension = os.path.splitext(os.path.basename(image_path))
    output_path = f"images/bg_rm_{image_name}.png"

    output_image.save(output_path)

pre_process_image("../images/img.jpg")
