## Ước tính cơ thể người từ 6 cảm biến quán tính

Mục tiêu là ước tính cơ thể người từ 6 cảm biến quán tính chi phí thấp. Ứng dụng full body tracking trong VRChat. Đối tượng so sánh SlimeVR [Crowsupply](https://www.crowdsupply.com/slimevr/slimevr-full-body-tracker) kêu gọi 1.000.000 USD

Các phương pháp trước đây sử dụng một số lượng lớn cảm biến, hoặc đầu vào video bổ sung. Chúng tôi thực hiện một cách tiếp cận khác và hạn chế vấn đề bằng cách: (i) sử dụng mô hình cơ thể thống kê thực tế bao gồm các ràng buộc nhân trắc học và (ii) sử dụng khung tối ưu hóa chung để phù hợp với mô hình để định hướng và đo gia tốc trên nhiều khung hình. Trình theo dõi kết quả là Sparse Inertial Poser (SIP) cho phép ước tính tư thế con người 3D chỉ sử dụng 6 cảm biến (gắn vào cổ tay, chân dưới, lưng và đầu) và hoạt động cho các chuyển động tùy ý của con người.

![image](https://user-images.githubusercontent.com/99313947/177080878-94779625-96d5-4c1e-932d-d92f5cefaff5.png)

[So sánh IMU](https://docs.slimevr.dev/diy/imu-comparison.html)
- BNO085
- BNO055
- MPU6050
- MPU6500
- MPU9250
- ICM20948
- BMI160
- Hi229 xin tài trợ từ HiPNUC

Công việc thực hiện: Tái tạo lại kết quả của bài báo Transpose.
- Sử dụng cảm biến MPU6050A + ESP8266
- Sử dụng cảm biến Hi229

| Paper | Link |
| --- | --- |
| (2017) [(ARXIV)](https://arxiv.org/abs/1703.08014) Sparse Inertial Poser: Automatic 3D Human Pose Estimation from Sparse IMU | file:///C:/Users/thanh/Downloads/html/1703.08014.html |

