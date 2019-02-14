# Wifi Mapping Device

The intent is to create an easily portable device which will monitor and record the SSIDs of nearby wireless networks, as well as logging the signal strength and position of the device. Inspired by the numerous wireless *dead zones* on campus, where I often find myself trying to remember nearby areas with a good connection, I decided to create a device which would record these connections and their important attributes.

These attributes namely are 
* SSID
* position
* strength
* security.

This information will be sent to the cloud, where a heatmap will be constructed to give a complete overview of the networks, guiding the user of the device and providing a comprehensive illustration to submit to an organisation should they wish to address these troublesome areas.

I plan to construct this device around a Raspberry Pi 3, given its ease of use, small size and wide array of components and software available for easy installation. A battery power supply will give the Pi the high mobility needed. The wireless chip on the Pi should suffice for the monitoring of network attributes, working together with a GPS module to gather positional data. Some form of immediate feedback to the user is required, either through a display on the device or a phone app which has access to the collected data. Direction should be given to the user to allow them to navigate to the nearest known network, as well as information on when that connection was last detected and connection quality. Should a user decide that a network is currently inaccessible, they will be able to dismiss the suggested network, prompting the device for an alternative or displaying all nearby options. Connection speed may also be logged if the device successfully connects to a network, but it may prove to be too inconsistent to be relied on.

![concept design][concept_design]

The main priorities of the device are **portability** and **accuracy**. This means that the device must be fairly small and preferably be one robust unit capable of withstanding travel. It is obviously necessary to make use of a mobile power supply, one which should be able to supply the Pi with power for hours, as the intention is for this device to work passively in the background until needed. This means that the operations the Pi must perform during these periods must consume as little power as possible. The accuracy will largely rely on the sensors, particularly the GPS module as the practicality of this device hinges most of all on its ability to accurately locate its user. Ideally, the pre-installed wi-fi chip will be capable of recording the finer details of the network connections but this is far more tolerant to inaccuracy than the positioning, which is crucial. These priorities will continue to guide the design in the choosing of appropriate hardware and making as effective use of it as possible.

[concept_design]: https://github.com/JackP2112/IoTSemester4Project/blob/master/concept_design.png "Concept Design"
