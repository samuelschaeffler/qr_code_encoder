import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer

def qr(input_data):
    code = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_L)
    code.add_data(input_data)

    img = code.make_image(image_factory=StyledPilImage, module_drawer=RoundedModuleDrawer())
    img.save('static/qrcode.png')