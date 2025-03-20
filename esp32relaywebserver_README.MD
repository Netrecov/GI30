esp32relaywebserver
Finally got this working......
Working to clean it up.
here is images of the pcb in the back.
i marked where the twisted wire pair was soldered previously.
![alt text](https://github.com/Netrecov/GI30/blob/main/pcb_back.jpg?raw=true)
![alt text](https://github.com/Netrecov/GI30/blob/main/pcb_front.jpg?raw=true)
pcb_back.jpg
pcb_front.jpg

So today I pulled the whole back apart again, this time, taking time to desolder the antenna connector so i could fully remove it from the unit.
I took pictures of the front and back without the plastic housing so the parts could be identified.
Since the unit was still functional, the only defect now was that the push button of the radial button no longer had an effect.
Not wanting to spend all day diagnosing what part failed, i decided to yolo, and "Sacrifice" another component with the attempt to wake the unit out of standby.
I decided on the button with the number 1 on it, as its only used to set a preset eq, and i dont use that, so if i happened to damage that button, it wouldnt matter.
i soldered back on the twister pair to pins 2 and pin 3 of the tactile switch, and then put the unit back together.
I drilled a small hole on the plastic housing for the antenna for the wires to come out of the unit.
I used an esp32 to make a script that i can now remotely press the button, thus taking the unit out of standby, with all my settings saved.
![alt text](https://github.com/Netrecov/GI30/blob/main/esp32relay.jpg?raw=true)
esp32relay.jpg
