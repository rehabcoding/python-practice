import qrcode # imported from the qrcode library 

website_link = 'https://youtu.be/T6eK-2OQtew?si=JeaGXgiafu3Tgo4i'

qr = qrcode.QRCode(version = 1, box_size = 5, border = 5)
# `version` parameter is an integer from 1 to 40 that controls the size of the QR code
# `box_size` parameter controls how many pixels each “box” of the QR code is
# `border` parameter controls how many boxes thick the border should be

qr.add_data(website_link)
# giving the link to be coverted into qr

qr.make()
# to generate the qr

img = qr.make_image(fill_color = 'black', back_color = 'white')
# boxes to be black, background to be white, as standard qr codes are

img.save('youtube_qr.png')

# try these :
# Allow the website link to be typed in using input() function.
# Allow users to customize the QR code generated.
# Automate the process to create multiple QR codes.
# Include more functions (or object parameters) of the qrcode library.
# Try changing the colors and styles of the generated QR codes using different drawer modules and fill colors.
# Use an application library (like Tkinter) to add a user interface.
# Check out other QR code libraries like pyqrcode.