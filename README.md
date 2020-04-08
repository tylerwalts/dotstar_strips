# DotStar-Illuminated Racks

This is for a project to add light and fun to some wine racks, but it could also be used for shelves or any set of ligh strips.  I wanted to be able to control the brightness and color, which I could have done with Phillips Hue or similar light strips, but I also wanted to add some automation with a motion sensor and leave options open for future sensor types, so I got a Raspberry Pi, a roll of DotStar light strips and set a few use case goals:

* *Christmas Decorations:* I started this project in December, so the first requirement is for the lights to work, and for it to look festive for guests.
* *Presence Detection:* Adding a PIR sensor to the Pi was easy, and I could use it to check and speed up the motion if a person is present and active, or slow it down if they stand still.
* *Idle Mode:* When nobody is active for a while, turn it off to save energy.
* *Wine Selection Mode:* When someone gets close to the racks, it should get brighter and help to select a bottle.
* *Security Mode:* Set it to detect presence and trigger police/strobe pattern.


### Build:

#### Wine Racks
Parts List:

* Wine Racks
* 3/4" square tubing
* Matte Black Spray Paint
* L Brackets
* Nuts & Bolts

#### Light Strips & Power

Light strips and power need to be designed together.  I originally wanted to do 144 lights-per-meter strips, but after doing the math settled on 30 lights-per-meter strips.

```
8 Strips * 1.25 meters * 144 lights/meter = 1440 lights
    Amps
    Watts
    Cost

8 Strips o* 1.25 meters * 30 lights/meter = 300 lights
    Amps
    Watts
    Cost 
```


#### Circuit

TODO

### Auto-Start

Edit dotstar.service to have the right path, and copy to /lib/systemd/system/dotstar.service


### Future Features

* Security:
  * Update to send email/SMS
  * Send alarm to SmartThings/HomeAssistant



