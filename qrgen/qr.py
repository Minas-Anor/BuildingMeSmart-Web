import qrcode
import os
from hashlib import md5

# path = os.path.join(os.path.abspath, "media/image.png")
def QR(data, info="default"):
    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_H,
        box_size = 10,
        border = 4,
    )

    qr.add_data(data)
    qr.make(fit=True)

    name = info + '-' + md5(data.encode()).hexdigest()

    img = qr.make_image()
    img.save("media/" + name + ".png")

    return name + '.png'