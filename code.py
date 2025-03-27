from adafruit_matrixportal.matrix import Matrix
from adafruit_matrixportal.matrix import Matrix
from adafruit_bitmap_font import bitmap_font
from adafruit_display_text.label import Label
import terminalio
import displayio
import usb_cdc
import supervisor
import re

matrix = Matrix()
display = matrix.display

group = displayio.Group()
bitmap = displayio.Bitmap(64, 32, 2)
color = displayio.Palette(4)
color[0] = 0x000000
color[1] = 0xFF0000
color[2] = 0xCC4000
color[3] = 0x85FF00

tile_grid = displayio.TileGrid(bitmap, pixel_shader=color)
group.append(tile_grid)
display.root_group = group

val = "0"

label = Label(terminalio.FONT)

label.scale = 1
bbx, bby, bbwidth, bbh = label.bounding_box

label.x = 8
label.y = 9
label.color = color[3]

group.append(label)

console = usb_cdc.data


while True:
    val = console.readline().rstrip().decode("utf-8")
    match = re.match(r"(\d+)", val)

    label.text = val
