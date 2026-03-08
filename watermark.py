import tkinter as tk
from PIL import Image,ImageDraw,ImageFont,ImageTk
import os

root = tk.Tk()
root.title("My Watermark App")
root.geometry("800x600")
image=Image.open("ele.jpeg")
photo = ImageTk.PhotoImage(image)
label=tk.Label(root,image=photo)
label.image=photo
label.pack()
watermark="Watermark"

def add_watermark(input_image_path, output_path, text, font_path=None, font_size=120, opacity=128,
                  position=(0, 0)):
    if font_path:
        font = ImageFont.truetype(font_path, font_size)
    else:
        font = ImageFont.load_default()
    base=Image.open(input_image_path).convert("RGBA")

    txt_layer=Image.new("RGBA",base.size,(0,0,0,0))
    draw=ImageDraw.Draw(txt_layer)
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    width, height = base.size
    x=(width-text_width)/2
    y=(height-text_height)/2
    draw.text((x,y),text,fill=(255,255,255,opacity),font=font)
    rotated=txt_layer.rotate(45)

    watermarked=Image.alpha_composite(base,rotated)
    watermarked = watermarked.convert("RGB")
    name, ext = os.path.splitext(input_image_path)
    output_path = f"{name}_watermarked{ext}"
    watermarked.save(output_path)

    print(f"Watermarked image saved to {output_path}")


add_watermark("ele.jpeg","ele.jpeg",watermark)

root.mainloop()
