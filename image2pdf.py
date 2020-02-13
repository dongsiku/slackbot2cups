import img2pdf
from PIL import Image
import subprocess


def image2pdf(image_filename):

    img_pil = Image.open(image_filename)
    if img_pil.mode == "RGBA":
        image_filename_split = image_filename.rsplit(".", 1)
        new_image_filename = "{}_withoutAlpha.{}".format(
            image_filename_split[0], image_filename_split[1])
        command_rgba2rgb = "convert {} -background white -alpha remove -alpha off {}".format(
            image_filename, new_image_filename)
        subprocess.run(command_rgba2rgb.split())

        image_filename = new_image_filename

    a4inpt = (img2pdf.mm_to_pt(210), img2pdf.mm_to_pt(297))
    layout_fun = img2pdf.get_layout_fun(a4inpt)
    with open("{}.pdf".format(image_filename), "wb") as f:
        f.write(img2pdf.convert(image_filename, layout_fun=layout_fun))


if __name__ == "__main__":
    image2pdf("sample_image_file.png")
