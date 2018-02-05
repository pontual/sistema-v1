from PIL import Image
from produtos import PRODUTO_LIST

def resize_to(filename, new_filename, new_width):
    img = Image.open(filename)
    ratio = new_width / img.size[0]
    new_height = int(img.size[1] * ratio)
    img.resize((new_width, new_height), Image.ANTIALIAS).save(new_filename)

def resize_main():
    orig_dir = "C:/Users/heitor/Desktop/ptlmirror/public_html/fotos/"
    new_dir = "C:/Users/heitor/sisfotos/"

    for prod in PRODUTO_LIST:
        resize_to(orig_dir + prod + ".jpg", new_dir + prod + ".jpg", 640)
        print("Resized", prod)
        
