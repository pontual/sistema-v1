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
    
    # orig_dir = "/home/heitor/pontual/ptlmirror/public_html/fotos/"
    # new_dir = "/home/heitor/tmp/sisfotos/"

    for prod in PRODUTO_LIST:
        try:
            resize_to(orig_dir + prod + ".JPG", new_dir + prod + ".jpg", 640)
        except FileNotFoundError:
            try:
                resize_to(orig_dir + prod + ".jpg", new_dir + prod + ".jpg", 640)
            except:
                print("Could not find {}, skipping.".format(prod))
        print("Resized", prod)
        
