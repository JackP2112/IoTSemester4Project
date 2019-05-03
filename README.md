# Wifi Mapping Device

This device detects wireless networks and displays their important attributes, SSID, security and signal strength along with the current position of the device, as given by GPS. The device is constructed of a Raspberry Pi 3, a GPS module and a display. I used an EM-506 GPS Receiver over UART and a 128x64 OLED Display over I2C.

![design result][design_result]

The [Adafruit_SSD1306 library](https://github.com/adafruit/Adafruit_SSD1306) works well for the display and in order to fit all the information on screen I used [6px by Jos Tan](https://www.dafont.com/6px.font) which I slightly [modified](https://github.com/JackP2112/IoTSemester4Project/blob/master/6px-Normal.ttf) to allow hyphens to display correctly.

The GPS receiver works with gpsd which is very well detailed in this [guide by Adafruit](https://learn.adafruit.com/adafruit-ultimate-gps-on-the-raspberry-pi/introduction).

## Initial Design

The intent is to create an easily portable device which will monitor and record the SSIDs of nearby wireless networks, as well as logging the signal strength and position of the device. Inspired by the numerous wireless *dead zones* on campus, where I often find myself trying to remember nearby areas with a good connection, I decided to create a device which would record these connections and their important attributes.


These attributes namely are 
* SSID
* position
* strength
* security.

This information will be sent to the cloud, where a heatmap will be constructed to give a complete overview of the networks, guiding the user of the device and providing a comprehensive illustration to submit to an organisation should they wish to address these troublesome areas.

I plan to construct this device around a Raspberry Pi 3, given its ease of use, small size and wide array of components and software available for easy installation. A battery power supply will give the Pi the high mobility needed. The wireless chip on the Pi should suffice for the monitoring of network attributes, working together with a GPS module to gather positional data. Some form of immediate feedback to the user is required, either through a display on the device or a phone app which has access to the collected data. Direction should be given to the user to allow them to navigate to the nearest known network, as well as information on when that connection was last detected and connection quality. Should a user decide that a network is currently inaccessible, they will be able to dismiss the suggested network, prompting the device for an alternative or displaying all nearby options. Connection speed may also be logged if the device successfully connects to a network, but it may prove to be too inconsistent to be relied on.
Further research has revealed the severe problem with relying on GPS for indoor positioning, as for the purposes of this device the data is so error prone it is effectively useless. To remedy this notorious problem of indoor positioning, the Raspberry Pi will also make use of an accelerometer. The function of this will be to take over from the GPS once the signal becomes unusable, attempting to track the user's location from a last known point. Possibilities include using pedometer algorithms to try and track indoor movement, which could be calibrated to any user while correct and constant GPS data is also present for reference. Another possible solution involves using the accelerometer data to try and reduce the error of the GPS by means of a Kalman filter. The filter would hopefully correct the data based upon a system of linear motion, as would be found in a human's natural movement.

![concept design][concept_design]

The main priorities of the device are **portability** and **accuracy**. This means that the device must be fairly small and preferably be one robust unit capable of withstanding travel. It is obviously necessary to make use of a mobile power supply, one which should be able to supply the Pi with power for hours, as the intention is for this device to work passively in the background until needed. This means that the operations the Pi must perform during these periods must consume as little power as possible. The accuracy will largely rely on the sensors, particularly the GPS module working in tandem with the corrections offered by the accelerometer as the practicality of this device hinges most of all on its ability to accurately locate its user. Ideally, the pre-installed wi-fi chip will be capable of recording the finer details of the network connections but this is far more tolerant to inaccuracy than the positioning, which is crucial. These priorities will continue to guide the design in the choosing of appropriate hardware and making as effective use of it as possible.

## End of Semester Status

This project was assigned as semester 4 continuous assessment for IoT Standards and Protocols. The time to work on this project as part of that module has now expired and what follows is a review of the project's progress as of the semester's end.

The device is quite effective at recording wireless network information and such information could easily be made persistent either locally or on the cloud. The GPS used works well in the right conditions and the IoT platform Wia allows for an easy translation of coordinates into a google map widget. Unfortunately, I could not find any existing software that would allow me to draw heatmaps in the way I first envisioned and as time was a pressing issue I chose to omit it rather than attempt my own. In addition, while researching Kalman filters and their applications I found enough material to understand them well enough for my purposes and sample code which would allow me to easily implement one for the problem I faced. However, when planning my usage of a Kalman filter I had included GPS and an accelerometer to correct the data based on linear motion. I realised too late that I would also need some form of directional sensor, a combination of a gyroscope and magnetometer seeming popular with similar projects online. Due to this oversight I was unable to implement a Kalman filter as I had hoped and as a result indoor positioning is infeasible with the device. The GPS in isolation however, gives pleasingly accurate readings outdoors and next to unobstructed windows, enough for the device to function well in at least some scenarios.

I chose Wia as an IoT platform because of its ease of use and my familiarity with it from the IoT labs, it also allowed for an excellent indicator of location in the form of the map widget. Due to the design of the text widgets, intended for short pieces of data, I could not display the network information as I wanted and so converted the data to an image before sending it to be displayed in an image widget. This is far from an ideal solution and if I were to progress this project any further I would definitely exchange this for normal text display, possibly in a web page with the Wia map widget embedded alongside.

While there are areas of this project which unfortunately fell short, I feel confident that more time and further consideration of the problems which arose would result in a device closely conforming to my initial design. As it stands the device can be used to detect wireless networks and display the key attributes as initially intended along with current position as read from the GPS. If the device is connected to the internet, it can send this information to Wia which allows for more sophisticated display of the data gathered.

[design_result]: https://github.com/JackP2112/IoTSemester4Project/blob/master/design_result.png "Design Result"
[concept_design]: https://github.com/JackP2112/IoTSemester4Project/blob/master/concept_design.png "Concept Design"
