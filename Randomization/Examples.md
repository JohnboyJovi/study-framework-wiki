Here some examples of randomized conditions and the ideas behind those can be found. **For simplicity, I left out ``USFMapFactors`` in all of them, which are however obviously required, just imagine all of the phases run on the same map.**
I also provide ``StudySetup.json`` declarations which can be extended and used for testing, e.g., in the [Study Framework Demo project](https://git-ce.rwth-aachen.de/vr-vis/VR-Group/unreal-development/demos/study-framework-demo).

# Fully Random
If you have two factors and want to fully randomize the order of presentation of their combinations for different participants. <br>
* Color: {<span style="color:orange">Orange</span>, <span style="color:blue">Blue</span>, <span style="color:green">Green</span>}
* <font color='red'>test blue color font</font>

🔴 red: +5V
🟠 orange: +3.3V
⚫ black: ground
⚪ white: ground (pull-down)
🟣 purple: I2C signal
🟢 green: clock signal
🟡 yellow: WS2812 signal
🔵 blue: resistor bridge (analogue) input