#coding=utf-8

from PIL import Image
import qrcode

print("[+]二维码信息文件名:",end=" ")
filename=input()
filename=str(filename)
print("[+]LOGO照片文件名:",end=" ")
logo_name=input()
logo_name=str(logo_name)

with open(filename,'r',encoding='utf-8') as f:
    i=1
    for txt in f.readlines():
        qr_txt = txt
        #print(qr_txt)
        qr = qrcode.QRCode(version=2, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=8, border=4)
        qr.add_data(qr_txt)
        qr.make(fit=True)

        img = qr.make_image()
        img = img.convert("RGBA")

        icon = Image.open(logo_name) 

        img_w, img_h = img.size
        factor = 4
        size_w = int(img_w / factor)
        size_h = int(img_h / factor)

        icon_w, icon_h = icon.size
        if icon_w > size_w:
            icon_w = size_w
        if icon_h > size_h:
            icon_h = size_h
        icon = icon.resize((icon_w, icon_h), Image.ANTIALIAS)

        w = int((img_w - icon_w) / 2)
        h = int((img_h - icon_h) / 2)
        icon = icon.convert("RGBA")
        img.paste(icon, (w, h), icon)
        img.save(str(i)+'.png')
        #img.show()
        print('[+]生成图片:'+str(i)+'.png')
        i+=1