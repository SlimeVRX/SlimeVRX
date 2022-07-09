Tái tạo kết quả Transpose paper

10/3: Đã implement được model, tìm giải pháp thay thế cho 6 IMU công nghiệp của tác giả gốc. 

Gặp vấn đề về IMU, xin hỗ trợ từ HiPNUC

Sử dụng 6 IMU 6050 + 6 ESP8266

13/4: Nhận đồ án

Đọc dịch tài liệu IMU Hi229

26/4: Nhận board IMU Hi229

4/5: Implement cảm biến Hi229, có kết quả đầu tiên

Gặp vấn đề không đồng bộ: chuyển dữ liệu cảm biến Hi229 thành dữ liệu đầu vào Transpose model

8/5: Tạo tool auto setting AT command, sửa đổi code HiPNUC lấy đồng thời dữ liệu 6 cảm biến, nhận bản cập nhập firmware Hi229 60Hz

Tìm hiểu model hoạt động: Giả dữ liệu, tạo chuyển động quanh trục Z -45 độ (Góc Euler: Yaw, Pitch, Row =0,0,-45) ở cánh tay trái, nhận thấy cánh tay xoay theo(Link1). 

Khi xoay Rotation matrix (Góc Euler: Yaw, Pitch, Row) thì khớp xương tương ứng xoay. Vậy có thể tạo các tư thế từ Rotation matrix

12/5: xây dựng lý thuyết chuyển đổi hệ tọa độ, từ hệ tọa độ cảm biến sang hệ tọa độ SMPL.

14/5: Chạy thành công

20/5: tìm ít nhất 5 điểm mới trong bài báo

24/5: release phiên bản đầu tiên, convert model từ Pytorch to ONNX, chạy realtime trên CPU i5-5200U laptop 24 FPS

28/5: ý tưởng viết paper

6/6: UWB
