import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import gps
import subprocess

RST = None
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0

disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)

disp.begin()
disp.clear()
width = disp.width
height = disp.height
image = Image.new('1', (width, height))

draw = ImageDraw.Draw(image)

font = ImageFont.truetype('6px-Normal.ttf',8)

session = gps.gps("localhost", "2947")
session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)

while True:
    location=["NO GPS", ""]
    try:
        report = session.next()
        if report['class'] == 'TPV':
            if hasattr(report, 'lat') and hasattr(report, 'lon'):
                location = [report.lat, report.lon]
    except KeyError:
        pass
    except KeyboardInterrupt:
        quit()
    except StopIteration:
        session = None
        print("GPSD has terminated")
    scan = subprocess.check_output("sudo iw dev wlan0 scan | awk -f scan.awk", shell=True)
    scan = str(scan)[2:-1].split('\\n')[:-1]
    draw.rectangle((0,0,width,height), outline=0, fill=0)
    y = -2
    for line in scan:
        y+=8
        words = line.split()
        x=[0,60,85,110]
        for i,word in enumerate(words):
            draw.text((x[i], y), str(word), font=font, fill=255)

    draw.text((20, height-10), str(location[0]), font=font, fill=255)
    draw.text((70, height-10), str(location[1]), font=font, fill=255)
    disp.image(image)
    disp.display()
