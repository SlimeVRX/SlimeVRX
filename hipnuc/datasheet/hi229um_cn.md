# Hi229 User Manual

> IMU/VRU/AHRS Attitude Measurement Module , Rev 1.0 [(PDF)](https://www.hipnuc.com/doc_gen/hi229/hi229um_cn.pdf)

<p align="left"><img width="400", src="https://user-images.githubusercontent.com/60751518/162100908-e1a732ac-b3e2-40f8-a385-436e349fcdae.png"></p>

- [Functional Overview](#FunctionalOverview)
  - [Key features](#Keyfeatures)
  - [Key features of integrated sensors](#Keyfeaturesofintegratedsensors)
  - [Typical application](#Typicalapplication)
  - [General description](#Generaldescription)
  - [Hi229 Connectivity](#Hi229Connectivity)
    - [Pin Descriptions](#PinDescriptions)
- [Performance Characteristics](#PerformanceCharacteristics)
  - [Attitude angle](#Attitudeangle)
  - [Accelerometer](#Accelerometer)
  - [Gyroscope](#Gyroscope)
  - [Magnetometer](#Magnetometer)
  - [Module data interface](#Moduledatainterface)
- [Calibration and Interpretation](#CalibrationandInterpretation)
  - [Accelerometer and Gyroscope Calibration](#AccelerometerandGyroscopeCalibration)
  - [Magnetometer Calibration](#MagnetometerCalibration)
    - [More about magnetic field interference](#Moreaboutmagneticfieldinterference)
    - [Difference between 6-axis and 9-axis mode](#Differencebetween6-axisand9-axismode)
    - [Mobile Robot](#MobileRobot)
- [Hi229 Orientation](#Hi229Orientation)
- [Packaging Information](#PackagingInformation)
  - [Package Outline](#PackageOutline)
  - [Soldering Guidelines](#SolderingGuidelines)
- Application Guide
  - The module is connected to the PC
  - The module is connected to the MCU
- Serial communication protocol
- Serial data packet
  - Overview
  - Product Support Package List
  - 0x90 (User ID)
  - 0xA0 (Acceleration)
  - 0xB0 (Angular Velocity)
  - 0xC0 (Magnetic Field Strength)
  - 0xD0 (Eulerian Angles)
  - 0XD1 (Quaternion)
  - 0XF0 (Air Pressure)
  - 0X91 (IMUSOL)
  - Factory default data package
  - Example of data frame structure
    - The data frame is configured as 0x90,0xA0,0xB0,0xC0,0xD0,0xF0 packets
    - The data frame is configured as 0x91 packets
- AT command
  - AT+ID
  - AT+INFO
  - AT+ODR
  - AT+BAUD
  - AT+EOUT
  - AT+RST
  - AT+SETYAW
  - AT+MODE
  - AT+SETPTL
- Appendix A - Evaluation Board
  - Introduction to the Evaluation Board
  - Remove the product from the evaluation board
- Appendix C - Firmware Upgrade and Factory Reset
- Appendix D - FAQ

<a name="FunctionalOverview"/>

## Functional Overview

<a name="Keyfeatures"/>

### Key features

Key features | Description
--- | ---
Outputs fused sensor data | Quaternion, Euler angles, Linear acceleration, Angular velocity, Magnetic field, ~~Gravity, Heading~~
3 sensors in one device | A triaxial 16-bit gyroscope, a triaxial 12-bit accelerometer, a triaxial geomagnetic sensor, and a 32-bit ARM® Cortex™-M4 microcontroller
Small package | Footprint 12 x 12 mm², Height 2.6 mm
~~Power Management~~ | ~~Intelligent Power Management: normal, low power and suspend mode available~~
Digital interface | UART (TTL 1.8V - 5.0V), USB (with USB evaluation board)
Voltage supplies | VDD voltage range: 3.3V (± 100mV)
Power consumption | 86mW @3.3V
Maximum peak power consumption | 32mA
Consumer electronics suite | ~~MSL1~~, RoHS compliant, ~~halogen-free~~. Operating temperature: -20°C - 85°C
Maximum output rate | 400Hz

<a name="Keyfeaturesofintegratedsensors"/>

### Key features of integrated sensors

Sensor | Range
--- | ---
Accelerometer | ± 8G
Gyroscope | ± 2000°/s
Magnetometer | 800mG  (miligauss)

<a name="Typicalapplication"/>

### Typical application

- Augmented reality
- Motion capture
- Advanced system attitude measurement
- Robotics
- Self-driving car

<a name="Generaldescription"/>

### General description

The Hi229 manufactured by HiPNUC is a System in Package (SiP) that integrates a triaxial accelerometer, a triaxial gyroscope, a triaxial magnetometer and a 32-bit ARM® Cortex™-M4 microcontroller running HiPNUC's sensor fusion firmware. The firmware provides sophisticated signal processing algorithms to process sensor data and provide precise real-time 3D orientation, heading, calibrated acceleration and calibrated angular velocity, as well as calibrated raw sensor data. The Hi229 has certain indoor magnetic anti-interference properties, and can still work normally under a certain intensity of magnetic field interference environment.

<a name="Hi229Connectivity"/>

### Hi229 Connectivity

The Hi229 can support connections to a host microcontroller through various serial interfaces:
- UART interface (TTL 1.8V-5.0V)
- USB (with USB evaluation board)

<a name="PinDescriptions"/>

#### Pin Descriptions

<p align="left"><img width="500", src="https://user-images.githubusercontent.com/60751518/162490460-07ee5e49-ed09-401e-8458-0df3d1c5b35c.png"></p>

Pin Number | Name | Description
--- | --- | --- 
5 | N/C | Reserve
6 | VDD | Supply voltage (sensors) 3.3V
7 | SYNC_OUT | The data output is synchronized with internal pull-up. High level when there is no data output, low level when a frame of data starts to be sent, and return to high level after a frame of data is sent. Need to be suspended when not in use.
8 | RXD | The module serial port receives UART RXD (TXD connected to MCU)
9 | TXD | The module serial port sends UART TXD (RXD connected to MCU)
10 | SYNC_IN | The data input is synchronized with internal pull-up. When the module detects a falling edge, it will output a frame of data. Need to be suspended when not in use.
11 | N/C | Reserve
19 | GND | GND
20 | RST | Reset, internal pull-up. >10uS low level reset module. No need for external resistors and capacitors. It is recommended to connect to the GPIO pin of the MCU for software reset.
21 | N/C | Reserved
22 | N/C | Reserved
23 | N/C | Reserved
24 | GND | GND
25 | N/C | Reserved

<a name="PerformanceCharacteristics"/>

## Performance Characteristics

<a name="Attitudeangle"/>

### Attitude angle

Parameter | Value
--- | ---
Roll and Pitch error - Static | 0.8°
Roll and Pitch error - Dynamic | 2.5°
Heading angle error in movement (6-axis mode, tested in 30min, horizontal smooth sweeper-like movement) | <10°
Heading angle error in movement (9-axis mode, after magnetic calibration and no nearby magnetic field interference) | 3°

<a name="Accelerometer"/>

### Accelerometer

Parameter | Value | Condition
--- | --- | ---
Digital resolution | 12 bit
Resolution | 1uG ~~(0,98 mG?)~~ |
Measurement ranges (programmable)| ±8G (1G = 1x gravitational acceleration) |
Internal sampling frequency | 1KHz |
Zero Bias Stability | 60uG | @25°C,1σ
Zero offset repeatability | 4.8mG | @25°C,1σ
Non-orthogonal error | ±0.1%
Random walk | 0.08 | @25°C,1σ
Scale factor error | ±0.3% (at full scale) | After factory calibration
Full temperature range temperature change | 2mg | -20 - 85°

<a name="Gyroscope"/>

### Gyroscope

Parameter | Value | Condition
--- | --- | ---
Digital resolution | 16 bit
Resolution | 0.01°/s ~~(0.004°/s)~~ |
Measurement ranges (programmable) | ± 2000°/s |
Internal sampling frequency | 1KHz |
Zero bias stability | 8°/h | @25°C,1σ
Zero offset repeatability | 0.12°/s | @25°C,1σ
Non-orthogonal error | ±0.1% | @25°C,1σ
Random walk | 0.6° | @25°C,1σ
Scale nonlinearity | ±0.1% | At full scale (maximum)
Scale factor error | ±0.4% | After factory calibration
Acceleration sensitivity | 0.1°/s/g | 

<a name="Magnetometer"/>

### Magnetometer

Parameter | Value
--- | ---
Measuring range | 800mG (miligauss)
Nonlinearity | ±0.1%
Resolution | 0.25mG

<a name="Moduledatainterface"/>

### Module data interface

Parameter | Value
--- | ---
Serial output baud rate | 9600/115200/460800/921600 (optional)
Frame output rate | 1/25/50/100/200/400Hz (optional)

<a name="CalibrationandInterpretation"/>

## Calibration and Interpretation

<a name="AccelerometerandGyroscopeCalibration"/>

### Accelerometer and Gyroscope Calibration

The accelerometer and gyroscope are calibrated for scale factor error, non-quadrature error and zero bias error before leaving the factory. Calibration parameters are stored inside the module.

The gyroscope is also calibrated for temperature compensation before leaving the factory. Calibration parameters are stored inside the module.

<a name="MagnetometerCalibration"/>

### Magnetometer Calibration

The magnetic sensor (supported by some models) is ellipsoid calibrated before leaving the factory, but the magnetic sensor is easily disturbed by the magnetic field of the external environment, and generally requires the customer to recalibrate:

The module has its own active magnetometer calibration system. The system does not require users to send any instructions. The system automatically collects magnetic field data for a period of time in the background, analyzes and compares it, and eliminates abnormal data. Once the data is sufficient, it will try magnetometer calibration. Therefore, when using the 9-axis mode, **the magnetometer calibration can be completed without any user intervention**. However, the module still provides an interface for the user to check the current calibration status. The premise of automatic calibration is to have sufficient degree of attitude maneuver (change of module attitude) and maintain a certain period of time, so that the internal calibration system can collect the magnetic field information under different attitudes to complete the calibration. **Magnetometer calibration cannot be performed in a static state**.

When the module is used for the first time with the 9-axis mode, the following calibration operations should be performed:

1. Check if the surrounding is magnetically clean: Indoors, next to the laboratory table, near the large iron/steel frame structure. All belong to common interference areas. It is recommended to take the module to an outdoor open space. Even if you don't have the conditions to get it outdoors, try to keep the module away (>0.5m) from objects that are prone to interference, such as laboratory desks/computers.
2. In the smallest possible range (the position does not move, just rotates), slowly rotate the module and let the module experience as many attitude positions as possible (rotate each axis at least 360° for about 1 minute). Under normal circumstances, the calibration can be completed. If the module has not been successfully calibrated, it means that the surrounding magnetic field interference is relatively large.
3. The success of the calibration can be checked by using the AT command: send the AT+INFO=HSI command, and the module will print the current status of the magnetometer calibration system:

<p align="left"><img width="500", src="https://user-images.githubusercontent.com/60751518/162633949-cee0e355-e8ff-4f1f-a712-1042529b8c3b.png"></p>

Just care about **[fiterr]**: 0.03 or less indicates that the calibration result is good enough. If **[fiterr]** is always > 0.1, it means that the magnetic field interference is very large, and it needs to be calibrated again to get better calibration results. ~~拟合残差会随着时间缓慢增长。~~

4. Although magnetometer calibration parameters can be dynamically fitted automatically. However, if the surrounding magnetometer environment changes (For example, need to move to another room or indoor and outdoor, or the module is installed/soldered into a new environment), 1-3 need to be repeated.

<a name="Moreaboutmagneticfieldinterference"/>

#### More about magnetic field interference

Mode | Description | Typical Interference Source | Influence | Precaution
--- | --- | --- | --- | ---
Spatial magnetic field interference (Distortions that do not move with sensor). | The interference does not move with the sensor movement, but is in the world coordinate system. | Various fixed sources of magnetic field interference, furniture, household appliances, cables, reinforced structures in houses, etc. All sources of interference that do not move with the movement of the magnetic sensor. | Regardless of whether the magnetic field sensor is well calibrated or not, the interference of these spatial magnetic fields (or the non-uniformity of the environmental magnetic field) will distort the spatial magnetic field. Magnetic compensation will be wrong and the correct heading angle will not be obtained. They are the main culprit that makes indoor magnetic fusion difficult to use. This interference cannot be calibrated and will seriously affect the magnetic properties. Spatial magnetic field interference is especially serious indoors. | Can only try to avoid this source of interference.
Interference in the sensor coordinate system (Distortions that move with sensor). | The interference source moves with sensor movement. | Module PCB, boards fixed together with modules, instruments, products, etc. They are regarded as the same rigid body as the magnetic sensor and move with the movement of the magnetic sensor. | Causes hard/soft magnetic interference to the sensor [Link](https://zhuanlan.zhihu.com/p/98325286). These disturbances can be well eliminated by the magnetic field calibration algorithm. | Module automatic magnetic field calibration.

<p align="left"><img width="500", src="https://user-images.githubusercontent.com/60751518/162626362-8ef1d2fd-8254-4dc4-b104-308d4c29741d.png"></p>

The figure is a typical indoor magnetic field distribution map. The spatial magnetic field distortion of the general indoor environment is relatively serious (belonging to spatial magnetic field interference, which cannot be calibrated and compensated)

**Notice:** In the indoor environment, the spatial magnetic interference is particularly serious, and it cannot be eliminated by calibration. Although the module has a built-in homogeneous magnetic field detection and shielding mechanism. The heading angle accuracy of the 9-axis mode depends largely on the degree of indoor magnetic field distortion. If the indoor magnetic field environment is very poor (such as next to the computer room, electromagnetic laboratory, workshop, underground garage, etc.), even after calibration, the heading angle accuracy of the 9-axis may not be as good as the 6-axis or even a large angle error.

<a name="Differencebetween6-axisand9-axismode"/>

#### Difference between 6-axis and 9-axis mode

Because the magnetic field is very susceptible to spatial interference, great care should be taken when using the 9-axis mode. The following table lists the recommendations for different use occasions and working conditions

Mode | Applicable environment | Typical application | Advantage | Disadvantages | Precaution
--- | --- | --- | --- | --- | ---
6-axis mode. | Various environments. | Low dynamic attitude detection such as PTZ, indoor robot. | 1. Good attitude angle output stability 2. Completely immune to magnetic field interference. | Heading angle drifts slowly over time. | The heading angle drifts slowly over time and cannot be compensated.
9-axis mode. | Non-magnetic interference environment. | 1. Compass, north-finding system 2. In an empty room with less magnetic interference, the module will basically not move indoors in a large range (typical is motion capture in a studio, and the subject will not move around in a large range) | 1. The heading angle will not drift over time 2. Once the magnetic field is detected, the heading angle can be quickly corrected to point north. | Any magnetic field interference will cause a decrease in heading angle accuracy. In the case of severe indoor interference, the heading angle cannot point to the correct direction. In addition, the metal structure and motor of the mobile robot will generate very strong magnetic interference, so the mobile robot platform is not suitable for 9-axis mode. | The geomagnetic sensor needs to be calibrated before first use.

The module's automatic geomagnetic calibration system can only handle fixed magnetic field interference installed with the module. If there is magnetic field interference in the installation environment, the interference must be fixed, and the distance between the interference magnetic field and the module will not change after installation (for example: the module is installed on an iron material, because iron will have magnetic field interference, then it is necessary to rotate the iron and the module together for calibration, and the iron will not be separated from the compass during use (relative displacement). Once separated, it needs to be re-calibrated. If the size of the iron is not fixed, or the change in distance from the compass is not fixed, the interference cannot be calibrated. Even if the calibration is successful, the accuracy will be very poor, and it can only be installed away from it. The safety distance is controlled above 40CM).

<a name="MobileRobot"/>

#### Mobile Robot

Suppose the customer wants to use the 9-axis mode on the mobile robot to obtain an accurate, non-drifting heading angle, and the module is mounted on the robot (think of it as a rigid body)：

- Since the robot itself will have a lot of hard magnetic interference due to the presence of metal structures (components, circuits), it is equivalent to the "interference in the sensor coordinate system" mentioned above. This part of the interference can be calibrated.
- Due to the start and stop of the robot's motor and the change of the magnetic field interference of the robot passing through various rooms indoors, which will produce the "spatial magnetic field interference". This part of the interference cannot be calibrated.

Both kinds of interference exist at the same time and can be very large, which poses a great challenge for the 9-axis mode. At this time, it is recommended that customers use the 6-axis mode. If the 9-axis mode must be used, the following points should be done:

1. Calibration: It must be calibrated with the robot (the robot is small enough). It is not correct to take the module off and calibrate it and then install it. The robot and the module must be regarded as a rigid body to be calibrated to obtain the correct calibration result. Please refer to the above for the specific calibration link. After the calibration is successful, power on (reset) to take effect.
2. Due to the complex indoor magnetic environment, even if the calibration is completed correctly, there may still be large magnetic field errors, especially when the motor starts and stops, and the power changes, which has a huge impact on the magnetic field.

<a name="Hi229Orientation"/>

## Hi229 Orientation

<p align="left"><img width="300", src="https://user-images.githubusercontent.com/60751518/162636182-e599530f-1a5b-4b20-83cc-3169ae749d2e.png"></p>

The vector system uses the Front-Left-Up (FLU) right-handed coordinate system. The geographic coordinate system uses the North-West-Ultra (NWU) coordinate system. The Euler angle rotation order is: Z-Y-X (turn the Z axis first, then the Y axis, and finally the X axis) rotation sequence. The specific definitions are as follows:

- Rotation around the Z-axis: also called Yaw or (pronounced: Psi). Range: -180°- 180°
- Rotation around the Y-axis: also called Pitch or (pronounced: Theta). Range: -90°-90°
- Rotation around the X-axis: also called Roll or (pronounced: Phi). Range: -180°-180°

If you think of the module as an aircraft. The X-axis should be considered the direction of the machine head. When the sensor frame coincides with the inertial frame, the ideal output of Euler angles is: Pitch = 0°, Roll = 0°, Yaw = 0°

<a name="PackagingInformation"/>

## Packaging Information

<a name="PackageOutline"/>

### Package Outline

<p align="left"><img width="600", src="https://user-images.githubusercontent.com/60751518/162636659-c4b2618b-933a-468a-9ad3-ccafee286340.png"></p>

Symbol | Minimum value | Typical value | Maximum value | Unit
--- | --- | --- | --- | ---
A1 | - | 11 | - | mm
B | - | 11 | - | mm
D | - | 12 | - | mm
E | - | 12 | - | mm
H | 2.5 | 2.6 | 2.7 | mm
a | - | 1.5 | - | mm
b | - | 0.9 | - | mm
c | - | 1 | - | mm
e | - | 1.27 | - | mm
f | - | 1 | - | mm

<a name="SolderingGuidelines"/>

### Soldering Guidelines

1. The installation position should be away from the easy deformation point of the PCB, try to stay away from the edge of the PCB (>30mm), and away from the PCB positioning screw hole (>10mm).

<p align="left"><img width="600", src="https://user-images.githubusercontent.com/60751518/162638036-36e54dda-bee3-4446-9843-283242da371f.png"></p>

2. The installation position should be away from strong magnetic devices, such as motors, speakers and other strong magnetic devices.

3. The assembled PCB must not be cleaned with an ultrasonic cleaner.

4. This product cannot be plastic-sealed or sprayed with conformal paint. Spraying or plastic-sealing will cause the sensor stress to change and affect its performance.

<p align="left"><img width="600", src="https://user-images.githubusercontent.com/60751518/162638125-0ca03f68-734c-46a9-822c-614eb70c4dfc.png"></p>

5. The recommended oven temperature graph for reflow soldering is as follows:

<p align="left"><img width="600", src="https://user-images.githubusercontent.com/60751518/162638196-d36e6554-08e4-4799-8441-76cdf8eb8ef8.png"></p>

**Notice:** The final stage of reflow soldering requires natural cooling, and the furnace cannot be turned on for forced air cooling, otherwise the product performance will be seriously affected.
