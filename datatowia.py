from wia import Wia
import gps
import subprocess

wia = Wia()
wia.access_token = "d_sk_gn5TeaB2RZNb5DFR83e7XiXr"

# Listen on port 2947 (gpsd) of localhost
session = gps.gps("localhost", "2947")
session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)

while True:
    subprocess.run('sudo iw dev wlan0 scan | awk -f /home/pi/scan.awk | convert label:@- wifi.png', shell=True)
    wia.Event.publish(name="wifi", file="./wifi.png")
    try:
        report = session.next()
        # Wait for a 'TPV' report and display the current time
        # To see all report data, uncomment the line below
        #print(report)
        if report['class'] == 'TPV':
            if hasattr(report, 'lat') and hasattr(report, 'lon'):
                wia.Location.publish(latitude=report.lat, longitude=report.lon)
    except KeyError:
        pass
    except KeyboardInterrupt:
        quit()
    except StopIteration:
        session = None
        print("GPSD has terminated")
