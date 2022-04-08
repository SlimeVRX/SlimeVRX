# Hi229 User Manual

> IMU/VRU/AHRS Attitude Measurement Module , Rev 1.0 [(PDF)](https://www.hipnuc.com/doc_gen/hi229/hi229um_cn.pdf)

<p align="left"><img width="400", src="https://user-images.githubusercontent.com/60751518/162100908-e1a732ac-b3e2-40f8-a385-436e349fcdae.png"></p>

- [Functional Overview](#FunctionalOverview)
- [Functional Description](#FunctionalDescription)
  - [Sensor Configuration](#SensorConfiguration)
  - [Digital interface and Power management](#DigitalinterfaceandPowermanagement)
- Hardware parameters
  - Size
  - Pin definition
- Coordinate system definition
- Performance
  - Attitude angle output accuracy
  - Gyroscope
  - Accelerometer
  - Magnetometer
  - Module data interface parameters
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

The Hi229 manufactured by HiPNUC is a System in Package (SiP) that integrates a triaxial accelerometer, a triaxial gyroscope, a triaxial magnetometer and a 32-bit ARM® Cortex™-M4 microcontroller running HiPNUC's sensor fusion firmware. The firmware provides sophisticated signal processing algorithms to process sensor data and provide precise real-time 3D orientation, heading, calibrated acceleration and calibrated angular velocity, as well as calibrated raw sensor data. The Hi229 has certain indoor magnetic anti-interference properties, and can still work normally under a certain intensity of magnetic field interference environment.

Typical application
- Augmented reality
- Motion capture
- Advanced system attitude measurement
- Robotics
- Self-driving car

<a name="FunctionalDescription"/>

## Functional Description

<a name="SensorConfiguration"/>

### Sensor Configuration

Sensor | Range
--- | ---
Gyroscope | ± 2000°/s
Accelerometer | ± 8G
Magnetometer | 800mG  (miligauss)

<a name="DigitalinterfaceandPowermanagement"/>

### Digital interface and Power management

- Serial port (compatible with TTL, can be directly connected to 5V or 3.3V Serial devices)
- Supply voltage: 3.3V (± 100mV)
- Maximum peak power consumption: 32mA **(đơn vị không đúng)**
