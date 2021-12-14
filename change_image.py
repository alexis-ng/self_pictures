from PIL import Image
import pathlib
maxsize = (272, 180)
for input_img_path in pathlib.Path("photos").iterdir():
    output_img_path = str(input_img_path).replace("photos","photos")
    with Image.open(input_img_path) as im:
        im.thumbnail(maxsize, Image.ANTIALIAS)
        im = im.rotate(90, expand = 1)
        im.save(output_img_path, "JPEG", dpi=(300,300))
        print(f"processing file {input_img_path} done...")
