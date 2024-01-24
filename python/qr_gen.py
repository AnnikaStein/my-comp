import qrcode
import qrcode.image.svg
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import SquareModuleDrawer, RoundedModuleDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=3,
)
qr.add_data('https://annikastein.github.io/my-comp/')

# ========== SVG part ==========
# Combined path factory, fixes white space that may occur when zooming
factory = qrcode.image.svg.SvgPathImage
img = qr.make_image(image_factory=factory)
img.save("figures/simple_qr.svg")

# ========== PNG part ==========
img_0 = qr.make_image(image_factory=StyledPilImage, module_drawer=SquareModuleDrawer())
img_1 = qr.make_image(image_factory=StyledPilImage, module_drawer=RoundedModuleDrawer())
img_2 = qr.make_image(image_factory=StyledPilImage, color_mask=RadialGradiantColorMask())
#img_3 = qr.make_image(image_factory=StyledPilImage, embeded_image_path="/path/to/image.png")
img_0.save("figures/square_qr.png")
img_1.save("figures/rounded_qr.png")
img_2.save("figures/rad_grad_qr.png")
