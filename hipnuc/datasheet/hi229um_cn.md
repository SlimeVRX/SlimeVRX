# Hi229 User Manual

> IMU/VRU/AHRS Attitude Measurement Module , Rev 1.0 [(PDF)](https://www.hipnuc.com/doc_gen/hi229/hi229um_cn.pdf)

<p align="left"><img width="400", src="https://user-images.githubusercontent.com/60751518/162100908-e1a732ac-b3e2-40f8-a385-436e349fcdae.png"></p>

* [1\. Functional Overview](#FunctionalOverview)
  * [1.1\. Key features](#Keyfeatures)
  * [1.2\. Key features of integrated sensors](#Keyfeaturesofintegratedsensors)
  * [1.3\. Typical application](#Typicalapplication)
  * [1.4\. General description](#Generaldescription)
  * [1.5\. Hi229 Connectivity](#Hi229Connectivity)
    * [1.5.1\. Pin Descriptions](#PinDescriptions)
* [2\. Performance Characteristics](#PerformanceCharacteristics)
  * [2.1\. Attitude angle](#Attitudeangle)
  * [2.2\. Accelerometer](#Accelerometer)
  * [2.3\. Gyroscope](#Gyroscope)
  * [2.4\. Magnetometer](#Magnetometer)
  * [2.5\. Module data interface](#Moduledatainterface)
* [3\. Calibration and Interpretation](#CalibrationandInterpretation)
  * [3.1\. Accelerometer and Gyroscope Calibration](#AccelerometerandGyroscopeCalibration)
  * [3.2\. Magnetometer Calibration](#MagnetometerCalibration)
    * [3.2.1\. More about magnetic field interference](#Moreaboutmagneticfieldinterference)
    * [3.2.2\. Difference between 6-axis and 9-axis mode](#Differencebetween6-axisand9-axismode)
    * [3.2.3\. Mobile Robot](#MobileRobot)
* [4\. Hi229 Orientation](#Hi229Orientation)
* [5\. Packaging Information](#PackagingInformation)
  * [5.1\. Package Outline](#PackageOutline)
  * [5.2\. Soldering Guidelines](#SolderingGuidelines)
* [6\. Getting Started with Hi229](#GettingStartedwithHi229)
  * [6.1\. Connect the module to the PC](#ConnectthemoduletothePC)
  * [6.2\. Connect the module to the MCU](#ConnectthemoduletotheMCU)
  * [6.3\. Reading/Writing the Hi229](#ReadingWritingtheHi229)
    * [6.3.1\. Serial data frame structure](#Serialdataframestructure)
    * [6.3.2\. Serial data packet](#Serialdatapacket)
      * [6.3.2.1\. 0x90 (User ID)](#0x90(UserID))
      * [6.3.2.2\. 0xA0 (Acceleration)](#0xA0(Acceleration))
      * [6.3.2.3\. 0xB0 (Angular velocity)](#0xB0(Angularvelocity))
      * [6.3.2.4\. 0xC0 (Magnetic Field Strength)](#0xC0(MagneticFieldStrength))
      * [6.3.2.5\. 0xD0 (Euler Angles)](#0xD0(EulerAngles))
      * [6.3.2.6\. 0xD1 (Quaternion)](#0xD1(Quaternion))
      * [6.3.2.7\. 0xF0 (Air Pressure)](#0xF0(AirPressure))
      * [6.3.2.8\. 0x91 IMUSOL (IMU data set)](#0x91IMUSOL(IMUdataset))
    * [6.3.3\. Factory default data package](#Factorydefaultdatapackage)
    * [6.3.4\. Example of data frame structure](#Exampleofdataframestructure)
      * [6.3.4.1\. The data frame is configured as 0x90,0xA0,0xB0,0xC0,0xD0,0xF0 packets](#0x90)
      * [6.3.4.2\. The data frame is configured as 0x91 packets](#0x91)
  * [6.4\. AT command](#ATcommand)
    * [6.4.1\. AT+ID](#AT+ID)
    * [6.4.2\. AT+INFO](#AT+INFO)
    * [6.4.3\. AT+ODR](#AT+ODR)
    * [6.4.4\. AT+BAUD](#AT+BAUD)
    * [6.4.5\. AT+EOUT](#AT+EOUT)
    * [6.4.6\. AT+RST](#AT+RST)
    * [6.4.7\. AT+TRG](#AT+TRG)
    * [6.4.8\. AT+SETPTL](#AT+SETPTL)
    * [6.4.9\. AT+MODE](#AT+MODE)
    * [6.4.10\. AT+SETYAW](#AT+SETYAW)
* [7\. Appendix A-Evaluation Board](#AppendixA-EvaluationBoard)
  * [7.1\. Introduction to Evaluation Board](#IntroductiontoEvaluationBoard)
  * [7.2\. Remove the product from the evaluation board](#Removetheproductfromtheevaluationboard)
* [8\. Appendix B-Firmware Upgrade and Factory Reset](#AppendixB-FirmwareUpgradeandFactoryReset)
* [9\. Appendix C-FAQ](#AppendixC-FAQ)
* [10\. Version History](#VersionHistory)
* [11\. References](#References)

<a name="FunctionalOverview"/>

## 1\. Functional Overview

<a name="Keyfeatures"/>

### 1.1\. Key features

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

### 1.2\. Key features of integrated sensors

Sensor | Range
--- | ---
Accelerometer | ± 8G
Gyroscope | ± 2000°/s
Magnetometer | 800mG  (miligauss)

<a name="Typicalapplication"/>

### 1.3\. Typical application

- Augmented reality
- Motion capture
- Advanced system attitude measurement
- Robotics
- Self-driving car

<a name="Generaldescription"/>

### 1.4\. General description

The Hi229 manufactured by HiPNUC is a System in Package (SiP) that integrates a triaxial accelerometer, a triaxial gyroscope, a triaxial magnetometer and a 32-bit ARM® Cortex™-M4 microcontroller running HiPNUC's sensor fusion firmware. The firmware provides sophisticated signal processing algorithms to process sensor data and provide precise real-time 3D orientation, heading, calibrated acceleration and calibrated angular velocity, as well as calibrated raw sensor data. The Hi229 has certain indoor magnetic anti-interference properties, and can still work normally under a certain intensity of magnetic field interference environment.

<a name="Hi229Connectivity"/>

### 1.5\. Hi229 Connectivity

The Hi229 can support connections to a host microcontroller through various serial interfaces:
- UART interface (TTL 1.8V-5.0V)
- USB (with USB evaluation board)

<a name="PinDescriptions"/>

#### 1.5.1\. Pin Descriptions

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

## 2\. Performance Characteristics

<a name="Attitudeangle"/>

### 2.1\. Attitude angle

Parameter | Value
--- | ---
Roll Angle\Pitch Angle - Static Error | 0.8°
Roll Angle\Pitch Angle - Dynamic Error | 2.5°
Heading angle error in movement (6-axis mode, tested in 30MIN, horizontal smooth sweeper-like movement) | <10°
Heading angle error in movement (9-axis mode, after magnetic calibration and no nearby magnetic field interference) | 3°

<a name="Accelerometer"/>

### 2.2\. Accelerometer

Parameter | Value | Condition
--- | --- | ---
Digital resolution | 12 bit
Resolution | 1uG ~~(0,98 mG?)~~ |
Measurement ranges (programmable)| ±8G (1G = 1x acceleration of gravity) |
Internal sampling frequency | 1KHz |
Zero-bias stability | 60uG | @25°C,1σ
Zero-bias repeatability | 4.8mG | @25°C,1σ
Non-orthogonal error | ±0.1%
Random walk | 0.08 | @25°C,1σ
Scale factor error | ±0.3% (at full scale) | After factory calibration
Operating temperature | 2mg | -20 - 85°

<a name="Gyroscope"/>

### 2.3\. Gyroscope

Parameter | Value | Condition
--- | --- | ---
Digital resolution | 16 bit
Resolution | 0.01°/s ~~(0.004°/s)~~ |
Measurement ranges (programmable) | ± 2000°/s |
Internal sampling frequency | 1KHz |
Zero-bias stability | 8°/h | @25°C,1σ
Zero-bias repeatability | 0.12°/s | @25°C,1σ
Non-orthogonal errors | ±0.1% | @25°C,1σ
Random walk | 0.6° | @25°C,1σ
Scale nonlinearity | ±0.1% | At full scale (maximum)
Scale factor error | ±0.4% | After factory calibration
Acceleration sensitivity | 0.1°/s/g | 

<a name="Magnetometer"/>

### 2.4\. Magnetometer

Parameter | Value
--- | ---
Measuring range | 800mG (miligauss)
Nonlinearity | ±0.1%
Resolution | 0.25mG

<a name="Moduledatainterface"/>

### 2.5\. Module data interface

Parameter | Value
--- | ---
Serial output baud rate | 9600/115200/460800/921600 (optional)
Frame output rate | 1/25/50/100/200/400Hz (optional)

<a name="CalibrationandInterpretation"/>

## 3\. Calibration and Interpretation

<a name="AccelerometerandGyroscopeCalibration"/>

### 3.1\. Accelerometer and Gyroscope Calibration

The accelerometer and gyroscope are calibrated for scale factor error, non-quadrature error and zero bias error before leaving the factory. Calibration parameters are stored inside the module.

The gyroscope is also calibrated for temperature compensation before leaving the factory. Calibration parameters are stored inside the module.

<a name="MagnetometerCalibration"/>

### 3.2\. Magnetometer Calibration

The magnetic sensor (supported by some models) is ellipsoid calibrated before leaving the factory, but the magnetic sensor is easily disturbed by the magnetic field of the external environment, and generally requires the customer to recalibrate:

The module has its own active magnetometer calibration system. The system does not require users to send any instructions. The system automatically collects magnetic field data for a period of time in the background, analyzes and compares it, and eliminates abnormal data. Once the data is sufficient, it will try magnetometer calibration. Therefore, when using the 9-axis mode, **the magnetometer calibration can be completed without any user intervention**. However, the module still provides an interface for the user to check the current calibration status. The premise of automatic calibration is to have sufficient degree of attitude maneuver (change of module attitude) and maintain a certain period of time, so that the internal calibration system can collect the magnetic field information under different attitudes to complete the calibration. **Magnetometer calibration cannot be performed in a static state**.

When the module is used for the first time with the 9-axis mode, the following calibration operations should be performed:

1. Check if the surrounding is magnetically clean: Indoors, next to the laboratory table, near the large iron/steel frame structure. All belong to common interference areas. It is recommended to take the module to an outdoor open space. Even if you don't have the conditions to get it outdoors, try to keep the module away (>0.5m) from objects that are prone to interference, such as laboratory desks/computers.
2. In the smallest possible range (the position does not move, just rotates), slowly rotate the module and let the module experience as many attitude positions as possible (rotate each axis at least 360° for about 1 minute). Under normal circumstances, the calibration can be completed. If the module has not been successfully calibrated, it means that the surrounding magnetic field interference is relatively large.
3. The success of the calibration can be checked by using the AT command: send the `AT+INFO=HSI` command, and the module will print the current status of the magnetometer calibration system:

<p align="left"><img width="500", src="https://user-images.githubusercontent.com/60751518/162633949-cee0e355-e8ff-4f1f-a712-1042529b8c3b.png"></p>

Just care about `fiterr`: 0.03 or less indicates that the calibration result is good enough. If `fiterr` is always > 0.1, it means that the magnetic field interference is very large, and it needs to be calibrated again to get better calibration results. ~~拟合残差会随着时间缓慢增长。~~

4. Although magnetometer calibration parameters can be dynamically fitted automatically. However, if the surrounding magnetometer environment changes (For example, need to move to another room or indoor and outdoor, or the module is installed/soldered into a new environment), 1-3 need to be repeated.

<a name="Moreaboutmagneticfieldinterference"/>

#### 3.2.1\. More about magnetic field interference

Mode | Description | Typical Interference Source | Influence | Precaution
--- | --- | --- | --- | ---
Spatial magnetic field interference (Distortions that do not move with sensor). | The interference does not move with the sensor movement, but is in the world coordinate system. | Various fixed sources of magnetic field interference, furniture, household appliances, cables, reinforced structures in houses, etc. All sources of interference that do not move with the movement of the magnetic sensor. | Regardless of whether the magnetic field sensor is well calibrated or not, the interference of these spatial magnetic fields (or the non-uniformity of the environmental magnetic field) will distort the spatial magnetic field. Magnetic compensation will be wrong and the correct heading angle will not be obtained. They are the main culprit that makes indoor magnetic fusion difficult to use. This interference cannot be calibrated and will seriously affect the magnetic properties. Spatial magnetic field interference is especially serious indoors. | Can only try to avoid this source of interference.
Interference in the sensor coordinate system (Distortions that move with sensor). | The interference source moves with sensor movement. | Module PCB, boards fixed together with modules, instruments, products, etc. They are regarded as the same rigid body as the magnetic sensor and move with the movement of the magnetic sensor. | Causes hard/soft magnetic interference to the sensor [^1]. These disturbances can be well eliminated by the magnetic field calibration algorithm. | Module automatic magnetic field calibration.

<p align="left"><img width="500", src="https://user-images.githubusercontent.com/60751518/162626362-8ef1d2fd-8254-4dc4-b104-308d4c29741d.png"></p>

The figure is a typical indoor magnetic field distribution map. The spatial magnetic field distortion of the general indoor environment is relatively serious (belonging to spatial magnetic field interference, which cannot be calibrated and compensated)

**Notice:** In the indoor environment, the spatial magnetic interference is particularly serious, and it cannot be eliminated by calibration. Although the module has a built-in homogeneous magnetic field detection and shielding mechanism. The heading angle accuracy of the 9-axis mode depends largely on the degree of indoor magnetic field distortion. If the indoor magnetic field environment is very poor (such as next to the computer room, electromagnetic laboratory, workshop, underground garage, etc.), even after calibration, the heading angle accuracy of the 9-axis may not be as good as the 6-axis or even a large angle error.

<a name="Differencebetween6-axisand9-axismode"/>

#### 3.2.2\. Difference between 6-axis and 9-axis mode

Because the magnetic field is very susceptible to spatial interference, great care should be taken when using the 9-axis mode. The following table lists the recommendations for different use occasions and working conditions

Mode | Applicable environment | Typical application | Advantage | Disadvantages | Precaution
--- | --- | --- | --- | --- | ---
6-axis mode. | Various environments. | Low dynamic attitude detection such as PTZ, indoor robot. | 1. Good attitude angle output stability 2. Completely immune to magnetic field interference. | Heading angle drifts slowly over time. | The heading angle drifts slowly over time and cannot be compensated.
9-axis mode. | Non-magnetic interference environment. | 1. Compass, north-finding system 2. In an empty room with less magnetic interference, the module will basically not move indoors in a large range (typical is motion capture in a studio, and the subject will not move around in a large range) | 1. The heading angle will not drift over time 2. Once the magnetic field is detected, the heading angle can be quickly corrected to point north. | Any magnetic field interference will cause a decrease in heading angle accuracy. In the case of severe indoor interference, the heading angle cannot point to the correct direction. In addition, the metal structure and motor of the mobile robot will generate very strong magnetic interference, so the mobile robot platform is not suitable for 9-axis mode. | The geomagnetic sensor needs to be calibrated before first use.

The module's automatic geomagnetic calibration system can only handle fixed magnetic field interference installed with the module. If there is magnetic field interference in the installation environment, the interference must be fixed, and the distance between the interference magnetic field and the module will not change after installation (for example: the module is installed on an iron material, because iron will have magnetic field interference, then it is necessary to rotate the iron and the module together for calibration, and the iron will not be separated from the compass during use (relative displacement). Once separated, it needs to be re-calibrated. If the size of the iron is not fixed, or the change in distance from the compass is not fixed, the interference cannot be calibrated. Even if the calibration is successful, the accuracy will be very poor, and it can only be installed away from it. The safety distance is controlled above 40CM).

<a name="MobileRobot"/>

#### 3.2.3\. Mobile Robot

Suppose the customer wants to use the 9-axis mode on the mobile robot to obtain an accurate, non-drifting heading angle, and the module is mounted on the robot (think of it as a rigid body)：

- Since the robot itself will have a lot of hard magnetic interference due to the presence of metal structures (components, circuits), it is equivalent to the "interference in the sensor coordinate system" mentioned above. This part of the interference can be calibrated.
- Due to the start and stop of the robot's motor and the change of the magnetic field interference of the robot passing through various rooms indoors, which will produce the "spatial magnetic field interference". This part of the interference cannot be calibrated.

Both kinds of interference exist at the same time and can be very large, which poses a great challenge for the 9-axis mode. At this time, it is recommended that customers use the 6-axis mode. If the 9-axis mode must be used, the following points should be done:

1. Calibration: It must be calibrated with the robot (the robot is small enough). It is not correct to take the module off and calibrate it and then install it. The robot and the module must be regarded as a rigid body to be calibrated to obtain the correct calibration result. Please refer to the above for the specific calibration link. After the calibration is successful, power on (reset) to take effect.
2. Due to the complex indoor magnetic environment, even if the calibration is completed correctly, there may still be large magnetic field errors, especially when the motor starts and stops, and the power changes, which has a huge impact on the magnetic field.

<a name="Hi229Orientation"/>

## 4\. Hi229 Orientation

<p align="left"><img width="300", src="https://user-images.githubusercontent.com/60751518/162636182-e599530f-1a5b-4b20-83cc-3169ae749d2e.png"></p>

The vector system uses the Front-Left-Up (FLU) right-handed coordinate system. The geographic coordinate system uses the North-West-Ultra (NWU) coordinate system. The Euler angle rotation order is: Z-Y-X (turn the Z axis first, then the Y axis, and finally the X axis) rotation sequence. The specific definitions are as follows:

- Rotation around the Z-axis: also called Yaw or (pronounced: Psi). Range: -180°- 180°
- Rotation around the Y-axis: also called Pitch or (pronounced: Theta). Range: -90°-90°
- Rotation around the X-axis: also called Roll or (pronounced: Phi). Range: -180°-180°

If you think of the module as an aircraft. The X-axis should be considered the direction of the machine head. When the sensor frame coincides with the inertial frame, the ideal output of Euler angles is: Pitch = 0°, Roll = 0°, Yaw = 0°

<a name="PackagingInformation"/>

## 5\. Packaging Information

<a name="PackageOutline"/>

### 5.1\. Package Outline

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

### 5.2\. Soldering Guidelines

1. The installation position should be away from the easy deformation point of the PCB, try to stay away from the edge of the PCB (>30mm), and away from the PCB positioning screw hole (>10mm).

<p align="left"><img width="600", src="https://user-images.githubusercontent.com/60751518/162638036-36e54dda-bee3-4446-9843-283242da371f.png"></p>

2. The installation position should be away from strong magnetic devices, such as motors, speakers and other strong magnetic devices.

3. The assembled PCB must not be cleaned with an ultrasonic cleaner.

4. This product cannot be plastic-sealed or sprayed with conformal paint. Spraying or plastic-sealing will cause the sensor stress to change and affect its performance.

<p align="left"><img width="600", src="https://user-images.githubusercontent.com/60751518/162638125-0ca03f68-734c-46a9-822c-614eb70c4dfc.png"></p>

5. The recommended oven temperature graph for reflow soldering is as follows:

<p align="left"><img width="600", src="https://user-images.githubusercontent.com/60751518/162638196-d36e6554-08e4-4799-8441-76cdf8eb8ef8.png"></p>

**Notice:** The final stage of reflow soldering requires natural cooling, and the furnace cannot be turned on for forced air cooling, otherwise the product performance will be seriously affected.

<a name="GettingStartedwithHi229"/>

## 6\. Getting Started with Hi229

<a name="ConnectthemoduletothePC"/>

### 6.1\. Connect the module to the PC

It is recommended to use the evaluation board to connect to the PC. The evaluation board has on-board USB power supply and USB to serial port functions, which can be conveniently used with the evaluation software on the PC for performance testing. See the Evaluation Boards section in the appendix for details.

<a name="ConnectthemoduletotheMCU"/>

### 6.2\. Connect the module to the MCU

The module and the MCU are connected through the serial port of TTL level. It is recommended that the RST pin of the module be connected to the GPIO of the MCU. It is convenient for MCU to force reset the module.

<p align="left"><img width="800", src="https://user-images.githubusercontent.com/60751518/162639226-0c1b1a2e-f840-4459-a5a8-f18322742678.png"></p>

**Notice:**

1. If the synchronization input (SYNC_IN) and synchronization output functions (SYNC_OUT) are not used, SYNC_IN and SYNC_OUT can be disconnected.
2. The function of the 120 ohm resistor is to facilitate debugging and prevent the level mismatch between the MCU and the module.  It can be removed. It is recommended to keep it.
3. Please refer to the manual for the voltage range of ~~VCC~~ VDD
4. The module has built-in power-on reset circuit, RST can be disconnected, but it is recommended to connect RST to a GPIO of the host to realize software reset.

<a name="ReadingWritingtheHi229"/>

### 6.3\. Reading/Writing the Hi229

<a name="Serialdataframestructure"/>

#### 6.3.1\. Serial data frame structure

After the module is powered on, the frame data is output at the factory frame rate (usually 100) by default. The frame format is as follows:

``` 
<frame header (0x5A)><frame type (0xA5)><length><CRC check><data field>
 ```

Domain name | Value | Length (bytes) | Description
--- | --- | --- | ---
PRE | 0x5A | 1 | Fixed to 0x5A
TYPE | 0xA5 | 1 | Fixed to 0xA5
LEN | 1-512 | 2 | The length of the data field in the frame, the low byte comes first. The length represents the length of the data field (PAYLOAD) and does not contain the PRE, TYPE, LEN, CRC fields.
CRC | - | 2 | Except for the CRC itself, the 16-bit CRC checksum of the frame data for all other fields (PRE, TYPE, LEN, PAYLOAD ). LSB (low byte first)
PAYLOAD | - | 1-512 | The data carried in one frame. The PAYLOAD field consists of several sub-packets.  Each data packet contains two parts: the data packet label and the data. The label determines the type and length of the data.

<p align="left"><img width="300", src="https://user-images.githubusercontent.com/60751518/162641629-a64b38ec-f923-4311-a952-dc307311a794.png"></p>

CRC implementation function:

```
/*
    currectCrc: previous crc value, set 0 if it's first section 
    src: source stream data
    lengthInBytes: length
*/
static void crc16_update(uint16_t *currectCrc, const uint8_t *src, 
uint32_t lengthInBytes)
{
    uint32_t crc = *currectCrc; 
    uint32_t j;
    for (j=0; j < lengthInBytes; ++j)
    {
        uint32_t i;
        uint32_t byte = src[j]; 
        crc ^= byte << 8;
        for (i = 0; i < 8; ++i)
        {
            uint32_t temp = crc << 1; 
            if (crc & 0x8000)
            {
                temp ^= 0x1021;
            }
            crc = temp;
        }
    }
    *currectCrc = crc;
}
```

<a name="Serialdatapacket"/>

#### 6.3.2\. Serial data packet

Record ID | Length (bytes) | Name | Remark
--- | --- | --- | ---
0x90 | 2 | User ID
0xA0 | 7 | Acceleration
0xB0 | 7 | Angular velocity
0xC0 | 7 | Magnetic Field Strength
0xD0 | 7 | Euler Angles
0xD1 | 17 | Quaternion
0xF0 | 5 | Air Pressure | Output 0
0x91 | 76 | IMUSOL (IMU data set) | Recommended

<a name="0x90(UserID)"/>

##### 6.3.2.1\. 0x90 (User ID)

A total of 2 bytes, the ID set by the user.

Byte | Type | Size | Unit | Description
--- | --- | --- | --- | ---
0 | uint8_t | 1 | - | Data packet label: 0x90
1 | uint8_t | 1 | - | User ID

<a name="0xA0(Acceleration)"/>

##### 6.3.2.2\. 0xA0 (Acceleration)

A total of 7 bytes, LSB. Output the raw acceleration of the sensor

Byte | Type | Size | Unit | Description
--- | --- | --- | --- | ---
0 | uint8_t | 1 | - | Data packet label: 0xA0
1 | int16_t | 2 | 0.001G (1G = 1 gravitational acceleration) | X-axis acceleration
3 | int16_t | 2 | 0.001G | Y-axis acceleration
5 | int16_t | 2 | 0.001G | Z-axis acceleration

<a name="0xB0(Angularvelocity)"/>

##### 6.3.2.3\. 0xB0 (Angular velocity)

A total of 7 bytes, LSB. Output the raw angular velocity of the sensor

Byte | Type | Size | Unit | Description
--- | --- | --- | --- | ---
0 | uint8_t | 1 | - | Data packet label: 0xB0
1 | int16_t | 2 | 0.1°/s | X-axis angular velocity
3 | int16_t | 2 | 0.1°/s | Y-axis angular velocity
5 | int16_t | 2 | 0.1°/s | Z-axis angular velocity

<a name="0xC0(MagneticFieldStrength)"/>

##### 6.3.2.4\. 0xC0 (Magnetic Field Strength)

A total of 7 bytes, LSB. Output the original magnetic field strength of the sensor

Byte | Type | Size | Unit | Description
--- | --- | --- | --- | ---
0 | uint8_t | 1 | - | Data packet label: 0xC0
1 | int16_t | 2 | 0.001Gauss | X-axis magnetic field strength
3 | int16_t | 2 | 0.001Gauss | Y-axis magnetic field strength
5 | int16_t | 2 | 0.001Gauss | Z-axis magnetic field strength

<a name="0xD0(EulerAngles)"/>

##### 6.3.2.5\. 0xD0 (Euler Angles)

A total of 7 bytes, LSB. The format is int16, a total of 3 values, each axis occupies 2 bytes, and the order is Pitch/Roll/Yaw. Roll, Pitch are the value obtained by multiplying the physical value by 100, and Yaw is the value obtained by multiplying it by 10.

Example: When the received Yaw = 100, it means that the heading angle is 10°

Byte | Type | Size | Unit | Description
--- | --- | --- | --- | ---
0 | uint8_t | 1 | - | Data packet label: 0xD0
1 | int16_t | 2 | 0.01° | Pitch (pitch angle)
3 | int16_t | 2 | 0.01° | Roll (roll angle)
5 | int16_t | 2 | 0.1° | Yaw (heading angle)

<a name="0xD1(Quaternion)"/>

##### 6.3.2.6\. 0xD1 (Quaternion)

A total of 17 bytes, LSB. The format is float, a total of 4 values, the order is: W X Y Z. Each value occupies 4 bytes (float), and the entire quaternion is 4 floats, LSB.

Byte | Type | Size | Unit | Description
--- | --- | --- | --- | ---
0 | uint8_t | 1 | - | Data packet label: 0xD1
1 | float | 4 | - | W
5 | float | 4 | - | X
9 | float | 4 | - | Y
13 | float | 4 | - | Z

<a name="0xF0(AirPressure)"/>

##### 6.3.2.7\. 0xF0 (Air Pressure)

A total of 5 bytes, the format is float. (Only for products with air pressure sensor)

Byte | Type | Size | Unit | Description
--- | --- | --- | --- | ---
0 | uint8_t | 1 | - | Data packet label: 0xF0
1 | float | 4 | Pa | Atmospheric pressure

<a name="0x91IMUSOL(IMUdataset)"/>

##### 6.3.2.8\. 0x91 IMUSOL (IMU data set)

A total of 76 bytes, the newly added data packet is used to replace A0, B0, C0, D0, D1 and other data packets. Integrate the sensor raw output of the IMU and the attitude solution data.

Byte | Type | Size | Unit | Description
--- | --- | --- | --- | ---
0 | uint8_t | 1 | - | Data packet label: 0x91
1 | uint8_t | 1 | - | ID
2 | - | 6 | - | Reserved
8 | uint32_t | 4 | ms | Timestamp information, accumulated from the system boot, increases by 1 per millisecond
12 | float | 12 | (1G = 1 acceleration of gravity) | Acceleration on the X, Y, and Z axis, note that the unit is different from 0xA0
24 | float | 12 | deg/s | the angular velocity of the X, Y, and Z axis, note that the unit is different from 0xB0
36 | float | 12 | uT | the magnetic field strength of X, Y, and Z axis (Hi229 support, note that the unit is different from 0xC0)
48 | float | 12 | deg | A set of Euler angles of nodes, in the order: Roll angle (Roll), Pitch angle (Pitch), heading angle (Yaw) (note that the order and unit are different from the 0xD0 data packet)
60 | float | 16 | - | WXYZ Set of node quaternions, the order is WXYZ

<a name="Factorydefaultdatapackage"/>

#### 6.3.3\. Factory default data package

The factory default definition of packet data carried in a frame is as follows:

Product | Default output data packet
--- | ---
Hi229 | 0x91

<a name="Exampleofdataframestructure"/>

#### 6.3.4\. Example of data frame structure

<a name="0x90"/>

##### 6.3.4.1\. The data frame is configured as `0x90, 0xA0,0xB0,0xC0,0xD0, 0xF0` data packets

Use the serial port assistant to sample a frame of data, a total of 41 bytes, the first 6 bytes are the frame header, length and CRC check value. The remaining 35 bytes are data fields. Suppose the data is received into the C language array `buf` . As follows:

5A A5 23 00 FD 61 **90** 00 **A0** 55 02 3D 01 E2 02 **B0** FE FF 17 00 44 00 **C0** 80 FF 60 FF 32 FF **D0** 64 F2 6C 0E BB 01 **F0** 00 00 00 00

- Step 1: Determine the frame header, get the data field length and frame CRC:

Frame header: `5A` `A5`

Frame data field length: `23` `00` : (0x00<<8) + 0x23 = 35

Frame CRC check value: `FD` `61` :(0x61<<8) + 0xFD = 0x61FD

- Step 2: Check CRC

```
    uint16_t payload_len; 
    uint16_t crc;

    crc = 0;
    payload_len = buf[2] + (buf[3] << 8);

    /* calulate 5A A5 and LEN filed crc */
    crc16_update(&crc, buf, 4);

    /* calulate payload crc */
    crc16_update(&crc, buf + 6, payload_len);
```

The obtained CRC value is 0x61FD, which is the same as the CRC value carried by the frame, and the frame CRC check is passed. 

- Step 3: Receive data

`90 00`: ID data packet, 0x90 is the data packet label, ID = 0x00. 

`A0 55 02 3D 01 E2 02`: Acceleration data packet, 0xA0 is the data packet label, and the three-axis acceleration is：

```
X-axis acceleration = (int16_t) ((0x02<<8) +0x55) = 597 (unit is mG)
Y-axis acceleration = (int16_t) ((0x01<<8)+0x3D) = 317
Z-axis acceleration = (int16_t) ((0x02<<8) +0xE2) = 738
```

`B0 FE FF 17 00 44 00`: Angular velocity data packet, 0xB0 is the data packet label, and the three-axis angular velocity is：

```
X-axis angular velocity = (int16_t)((0xFF<<8)+ 0xFE) = -2 (unit is 0.1°/s)
Y-axis angular velocity = (int16_t)((0x00<<8)+ 0x17) = 23
Z-axis angular velocity = (int16_t)((0x00<<8)+ 0x44) = 68
```

`C0 80 FF 60 FF 32 FF`: Magnetic field data packet, 0xC0 is the data packet label, and the three-axis magnetic field is：

```
X-axis angular velocity = (int16_t)((0xFF<<8)+ 0x80) = -128 (unit is 0.001GAUSS)
Y-axis angular velocity = (int16_t)((0xFF<<8)+ 0x60) = -160
Z-axis angular velocity = (int16_t)((0xFF<<8)+ 0x32) = -206
```

`D0 64 F2 6C 0E BB 01`: Euler angle data packet, 0xD0 is the data packet label

```
Pitch = (int16_t)((0xF2<<8)+ 0x64) / 100 = -3484 / 100 = -34.84°
Roll = (int16_t)((0x0E<<8)+ 0x6C) / 100 = 3692 / 100 = 36.92°
Yaw = (int16_t)((0x01<<8)+ 0xBB) / 10 = 443 /10 = 44.3°
```

`F0 00 00 00 00`: Air pressure data packet, 0xF0 is the data packet label

```
    float prs;
    prs = memcpy(&prs, &buf[37], 4);
```

Finally get the result：

```
id : 0
acc(G) : 0.597 0.317 0.738
gyr(deg/s) : -0.200 2.300 6.800
mag(uT) : -12.800 -16.000 -20.600
eul(R/P/Y) : 36.920 -34.840 44.300
```

<a name="0x91"/>

##### 6.3.4.2\. The data frame is configured as a `0x91` data packet

Use the serial port assistant to sample a frame of data, a total of 82 bytes, the first 6 bytes are the frame header, length and CRC check value. The remaining 76 bytes are data fields. Suppose the data is received into the C language array `buf`. As follows:

5A A5 4C 00 6C 51 **91** 00 A0 3B 01 A8 02 97 BD BB 04 00 9C A0 65 3E A2 26 45 3F 5C E7 30 3F E2 D4 5A C2 E5 9D A0 C1 EB 23 EE C2 78 77 99 41 AB AA D1 C1 AB 2A 0A C2 8D E1 42 42 8F 1D A8 C1 1E 0C 36 C2 E6 E5 5A 3F C1 94 9E 3E B8 C0 9E BE BE DF 8D BE

- Step 1: Determine the frame header, get the data field length and frame CRC:

Frame header: `5A` `A5`

Frame data field length: `4C` `00`: (0x00<<8) + 0x4C = 76

Frame CRC check value: `6C` `51`:(0x51<<8) + 0x6C = 0x516C

- Step 2: Check CRC

```
    uint16_t payload_len; 
    uint16_t crc;

    crc = 0;
    payload_len = buf[2] + (buf[3] << 8);

    /* calulate 5A A5 and LEN filed crc */ 
    crc16_update(&crc, buf, 4);

    /* calulate payload crc */ 
    crc16_update(&crc, buf + 6, payload_len);
```

The CRC value obtained is 0x516C. The frame CRC check is passed.

- Step 3: Receive data

The data field of the data packet starts from `0x91`. In C language, you can define a structure to easily read data:

Define the 0x91 packet structure as follows:

```
__packed typedef struct
{
    uint8_t tag; /* data packet tag:  0x91*/
    uint8_t id; /* module ID */
    uint8_t rev[6]; /* reserved */
    uint32_t ts; /* timestamp */
    float acc[3]; /* acceleration */
    float gyr[3]; /* angular velocity */
    float mag[3]; /* geomagnetic */
    float eul[3]; /* euler angles: Roll, Pitch, Yaw */
    float quat[4]; /* quaternion*/
}id0x91_t;
```

`__packed` is the compiler keyword (Keil), which means that the structure is tightly aligned by bytes, and each element of the structure corresponds to the structure definition of the 0x91 data packet. When receiving data, `memcpy` the received array directly to the structure: (notice that 4 bytes must be aligned when defining the structure), where `buf` points to the frame header and `buf [6]` points to the data field in the frame. 

```
    /* Receive data and use the 0x91 packet structure definition to interpret the data */
    __align(4) id0x91_t dat; /* struct must be 4 byte aligned */ 
    memcpy(&dat, &buf[6], sizeof(id0x91_t));
```

Finally get the dat data result：

```
id : 0
timestamp : 310205
acc : 0.224 0.770 0.691
gyr : -54.708 -20.077 -119.070
mag : 19.183 -26.208 -34.542
eul(R/P/Y) : 48.720 -21.014 -45.512
quat : 0.855 0.310 -0.310 -0.277
```

<a name="ATcommand"/>

### 6.4\. AT command

When using the serial port to communicate with the module, the module supports AT command set configuration/view module parameters. AT commands always start with ASCII code, followed by control characters, and finally ends with a carriage return and a newline `\r\n`.

Use the host computer to enter the AT command:

<p align="left"><img width="400", src="https://user-images.githubusercontent.com/60751518/163299877-ee861325-7ddf-409f-b875-5f920f93f67e.png"></p>

Use the serial port debugging assistant for testing：

<p align="left"><img width="800", src="https://user-images.githubusercontent.com/60751518/163300108-8623dc40-8638-4daf-ae11-875a119fff7e.png"></p>

The general module AT commands are as follows

Commands | Description | Power-off save (Y) | Immediately effective (Y), reset effective (R) | Condition
--- | --- | --- | --- | ---
AT+ID | Set module user ID | Y | R
AT+INFO | Print module information | N | Y
AT+ODR | Set the output rate of the module serial port | Y | R
AT+BAUD | Set the serial port baud rate | Y | R
AT+EOUT | Serial output switch | N | Y
AT+RST | Reset module | N | Y
AT+TRG | Single output trigger | N | Y | Some models support
AT+SETPTL | Set the output data packet | Y | Y | Some models support
AT+MODE | Set module operating mode | Y | R | Some models support
AT+SETYAW | Set the heading angle |
~AT+GWID~ | Set the wireless gateway ID | Y | R | Some models support

<a name="AT+ID"/>

#### 6.4.1\. AT+ID
Set the module user ID

Example `AT+ID=1`

<a name="AT+INFO"/>

#### 6.4.2\. AT+INFO
Print module information, including product model, version, firmware release date, etc.

<a name="AT+ODR"/>

#### 6.4.3\. AT+ODR
Set the output rate of the module serial port. Power-off save, reset the module to take effect

Example: Set the serial output rate to 100Hz: `AT+ODR=100`

**Notice:** When the output frame rate is set relatively high (such as 200), the default 115200 baud rate may not meet the output bandwidth requirements. In this case, the module needs to be set to a high baud rate (such as 921600), that the module can output a high frame rate stably. The output frame rate can be 1, 2, 5, 10, 20, 50, 100, 200, 400Hz.

<a name="AT+BAUD"/>

#### 6.4.4\. AT+BAUD
Set the serial port baud rate, optional value: `9600/115200/460800/921600`

Example `AT+BAUD=115200`

**Notice:** 
- When using this command, special attention should be paid. Entering an incorrect baud rate will lead to failure to communicate with the module.
- After setting the baud rate parameter, power off and save, and reset the module to take effect. The baud rate of the host computer should also be modified accordingly.
- When upgrading the firmware, you need to switch back to 115200 baud rate.

<a name="AT+EOUT"/>

#### 6.4.5\. AT+EOUT
Serial output switch

Example: 
- Open the serial port output `AT+EOUT=1` 
- Close the serial port output `AT+EOUT=0`

<a name="AT+RST"/>

#### 6.4.6\. AT+RST
Reset module

Example `AT+RST`

<a name="AT+TRG"/>

#### 6.4.7\. AT+TRG
The trigger module outputs a frame of data, which can be used with AT+ODR=0 to achieve a single trigger output.

Example `AT+TRG`

<a name="AT+SETPTL"/>

#### 6.4.8\. AT+SETPTL
Set the output protocol:

Set the data packets contained in a frame: the format is `AT+SETPTL=<ITEM_ID>,<ITEM_ID>...`

Example: Configuration module output: 91 data packets (IMUSOL) `AT+SETPTL=91`
Configuration module output: acceleration (A0), angular velocity (B0), shaping format Euler angle (D0) and quaternion (D1) `AT+SETPTL=A0,B0,D0,D1`

<a name="AT+MODE"/>

#### 6.4.9\. AT+MODE
Set the module working mode
Example
- Set the module to work in 6-axis mode (non-magnetic calibration) `AT+MODE=0`
- Set the module to work in 9-axis mode (magnetic field sensor participates in heading angle correction) `AT+MODE=1`

<a name="AT+SETYAW"/>

#### 6.4.10\. AT+SETYAW
Set the heading angle, the format is AT+SETYAW=<MODE>,<VAL>
Example
- MODE=0 Absolute mode: Set the heading angle directly to the value of VAL. For example, `AT+SETYAW=0,90` will directly set the heading angle to 90°
- MODE=1 Relative mode: Increment the original heading angle by VAL value. For example, `AT+SETYAW=1, -10.5` will increase the heading angle by -10.5°. If the original is 30°, the heading angle will become 19.5° after sending the command.
  
<a name="AppendixA-EvaluationBoard"/>
  
## 7\. Appendix A-Evaluation Board

<p align="left"><img width="800", src="https://user-images.githubusercontent.com/60751518/163308421-d58fb959-dd0f-4f45-b071-01ac47b183ff.png"></p>

<a name="IntroductiontoEvaluationBoard"/>
  
### 7.1\. Introduction to Evaluation Board

Provide power supply + USB to serial port function, which is convenient for customers to quickly evaluate products.

The data package contains the CP2104 USB-UART driver. Connect the USB cable to the computer and the module, open the host computer in the data package, and connect the serial port. By default, the module will output the factory default data packet at 115200 baud rate.

<a name="Removetheproductfromtheevaluationboard"/>
  
### 7.2\. Remove the product from the evaluation board

The module is embedded in the PLCC28 slot of the evaluation board by default. To remove the module, please follow the steps below:

- Power off, prepare a fine screwdriver or tweezers
- Pry the module from the PLCC socket or eject the circular hole on the back. 

**Notice:**

- The evaluation board is for quick verification and evaluation of module performance. It does not have any other calculation functions. 
- The USB interface is not suitable for industrial-grade scenarios or high-motion environments. If your application is a high-motion environment (motion capture, etc.), it is not recommended to use the evaluation board directly in your product.

<a name="AppendixB-FirmwareUpgradeandFactoryReset"/>
  
## 8\. Appendix B-Firmware Upgrade and Factory Reset

This product supports upgrading firmware.
Firmware upgrade steps:
- Connect the module, turn on the host computer, and set the baud rate of both the module and the host computer to 115200.  Open the firmware upgrade window
- Click the Connect button, if the module connection information appears. It means that the upgrade system is ready, click the file selector (…) to select the firmware with the extension .hex, and then click to start programming. After the download is complete,  the programming will be prompted to complete. At this time, close the serial port, power on the module again, and the module upgrade is complete.

<p align="left"><img width="800", src="https://user-images.githubusercontent.com/60751518/163308619-c866aa05-0239-4b7c-bb3a-b671b559e542.png"></p>

<a name="AppendixC-FAQ"/>
  
## 9\. Appendix C-FAQ

FAQ content is updated at any time, see: [FAQ](https://zhuanlan.zhihu.com/p/344884686)

For new product information and technical support, please pay attention to the official account of HiPNUC:

<p align="left"><img width="300", src="https://raw.githubusercontent.com/hipnuc/products/master/img/qrcode_for_gh_1d8b6b51409d_258.jpg"></p>
  
<a name="VersionHistory"/>
  
## 10\. Version History

Version | Changes | Date
--- | --- | ---
1.0 | translate into English | April 14, 2022
  
<a name="References"/>
  
## 11\. References

[^1]: Hard/soft magnetic(https://zhuanlan.zhihu.com/p/98325286)
