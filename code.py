import board
import time
import terminalio
import busio
from secrets import secrets
from adafruit_matrixportal.matrixportal import MatrixPortal

# the current working directory (where this file is)
cwd = ("/" + __file__).rsplit("/", 1)[0]
matrixportal = MatrixPortal(status_neopixel=board.NEOPIXEL,default_bg=cwd + "/coffeeclub.bmp",debug=True)

i=0

JSON_GET_URL="http://192.168.3.187:5000/"
response = matrixportal.network.fetch(JSON_GET_URL,)
matrixportal.add_text(
    text_font=terminalio.FONT,
    text_position=(2, (matrixportal.graphics.display.height // 2) - 1),
)
matrixportal.add_text(
    text_font=terminalio.FONT,
    text_position=(0,26),
    scrolling=True,
    text_color=0xff6500,
    )
matrixportal.set_text(" ", 1)
matrixportal.set_text(response.content,1)


while True:
    matrixportal.scroll_text(0.035)
