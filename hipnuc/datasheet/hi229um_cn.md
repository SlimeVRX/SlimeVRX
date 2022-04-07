# Hi229 User Manual

> IMU/VRU/AHRS Attitude Measurement Module , Rev 1.0 [(PDF)](https://www.hipnuc.com/doc_gen/hi229/hi229um_cn.pdf)

<p align="left"><img width="400", src="https://user-images.githubusercontent.com/60751518/162100908-e1a732ac-b3e2-40f8-a385-436e349fcdae.png"></p>

- [Introduction](#Introduction)
- Key features
  - Key features of integrated sensors
  - Digital interface and Power supply
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

<a name="Introduction"/>

# Introduction

The HI229 launched by 超核电子 is a low-cost, high-performance, small size, and low-latency attitude reference unit (AHRS). This product integrates a triaxial accelerometer, a triaxial gyroscope, a triaxial magnetometer and a microcontroller.
