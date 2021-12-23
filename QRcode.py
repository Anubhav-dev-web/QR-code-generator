import qrcode
import image

qr = qrcode.QRCode(
    version = 15,  # 15 means the version of qr  code , higher the number bigger the code image and complicated picture
    box_size = 10, # size of box where qr code will be displayed
    border = 5 # it is the white part of image ----border above in all 4 directions


)

data = input("GIVE THE DATA")
# any data to be converted

qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill = "black",dark_color = "white")
img.save("test.png")