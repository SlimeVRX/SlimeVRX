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
- Coordinate system definition
- Sensor calibration
  - Accelerometer and Gyroscope
  - Magnetometer
    - More about magnetometer interference
    - Difference between 6-axis and 9-axis mode
    - ~~Mobile Robot Case~~
- Mounting and Soldering
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
Heading angle error in movement (9-axis mode, after magnetic calibration and no nearby magnetic interference) | 3°

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
