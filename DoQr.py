#Easy util for making QR code

import qrcode

ref = input("print ref for ur qr: ")
name = input("print name for ur img: ")
color = input("color dots(R,G,B) or Enter for red: ").strip()



if color:
    r, g, b = map(int, color.split(','))
else:
    r, g, b = 200, 0, 0
def makeQR(ref, name, color):
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
    qr.add_data(ref)
    qr.make(fit=True)

    img = qr.make_image(fill_color=color, back_color=(255, 255, 255))
    img.save(f"{name}.png")
    print(f"save {name}.png")

makeQR(ref, name, (r,g,b))