# Dive into Deep Learning
Đắm mình vào học sâu

* [6\. Getting Started with Hi229](#GettingStartedwithHi229)
  * [6.1\. Connect the module to the PC](#ConnectthemoduletothePC)
    * [6.3.1\. Serial data frame structure](#Serialdataframestructure)
      * [6.3.2.1\. 0x90 (User ID)](#0x90(UserID))

- [Giới thiệu từ nhóm dịch](00.0gioithieutunhomdich.md)
- Lời nói đầu
- Cài đặt
- Ký hiệu
1. Giới thiệu
1.1. Một ví dụ truyền cảm hứng
1.2. Các thành phần chính: Dữ liệu, Mô hình và Thuật toán
1.3. Các dạng Học Máy
1.4. Nguồn gốc
1.5. Con đường tới Học Sâu
1.6. Các câu chuyện thành công
1.7. Tóm tắt
1.8. Bài tập
1.9. Thảo luận
1.10. Những người thực hiện
2. Sơ bộ
2.1. Thao tác với Dữ liệu
2.2. Tiền xử lý dữ liệu
2.3. Đại số tuyến tính
2.4. Giải tích
2.5. Tính vi phân Tự động
2.6. Xác suất
2.7. Tài liệu
2.8. Những người thực hiện
3. Mạng nơ-ron Tuyến tính
3.1. Hồi quy Tuyến tính
3.2. Lập trình Hồi quy Tuyến tính từ đầu
3.3. Cách lập trình súc tích Hồi quy Tuyến tính
3.4. Hồi quy Softmax
3.5. Bộ dữ liệu Phân loại Ảnh (Fashion-MNIST)
3.6. Lập trình Hồi quy Sofmax từ đầu
3.7. Cách lập trình súc tích Hồi quy Softmax
3.8. Những người thực hiện
4. Perceptron Đa tầng
4.1. Perceptron đa tầng
4.2. Lập trình Perceptron Đa tầng từ đầu
4.3. Cách lập trình súc tích Perceptron Đa tầng
4.4. Lựa Chọn Mô Hình, Dưới Khớp và Quá Khớp
4.5. Suy giảm trọng số
4.6. Dropout
4.7. Lan truyền xuôi, Lan truyền ngược và Đồ thị tính toán
4.8. Ổn định Số học và Khởi tạo
4.9. Cân nhắc tới Môi trường
4.10. Dự đoán Giá Nhà trên Kaggle
4.11. Những người thực hiện
5. Tính toán Học sâu
5.1. Tầng và Khối
5.2. Quản lý Tham số
5.3. Khởi tạo trễ
5.4. Các tầng Tuỳ chỉnh
5.5. Đọc/Ghi tệp
5.6. GPU
5.7. Những người thực hiện
6. Mạng Nơ-ron Tích chập
6.1. Từ Tầng Kết nối Dày đặc đến phép Tích chập
6.2. Phép Tích chập cho Ảnh
6.3. Đệm và Sải Bước
6.4. Đa kênh Đầu vào và Đầu ra
6.5. Gộp (Pooling)
6.6. Mạng Nơ-ron Tích chập (LeNet)
6.7. Những người thực hiện
7. Mạng Nơ-ron Tích chập Hiện đại
7.1. Mạng Nơ-ron Tích chập Sâu (AlexNet)
7.2. Mạng sử dụng Khối (VGG)
7.3. Mạng trong Mạng (Network in Network - NiN)
7.4. Mạng nối song song (GoogLeNet)
7.5. Chuẩn hoá theo batch
7.6. Mạng phần dư (ResNet)
7.7. Mạng Tích chập Kết nối Dày đặc (DenseNet)
7.8. Những người thực hiện
8. Mạng Nơ-ron Hồi tiếp
8.1. Mô hình chuỗi
8.2. Tiền Xử lý Dữ liệu Văn bản
8.3. Mô hình Ngôn ngữ và Tập dữ liệu
8.4. Mạng nơ-ron Hồi tiếp
8.5. Lập trình Mạng nơ-ron Hồi tiếp từ đầu
8.6. Lập trình súc tích Mạng nơ-ron Hồi tiếp
8.7. Lan truyền Ngược qua Thời gian
8.8. Những người thực hiện
9. Mạng Nơ-ron Hồi tiếp Hiện đại
9.1. Nút Hồi tiếp có Cổng (GRU)
9.2. Bộ nhớ Ngắn hạn Dài (LSTM)
9.3. Mạng Nơ-ron Hồi tiếp Sâu
9.4. Mạng Nơ-ron Hồi tiếp Hai chiều
9.5. Dịch Máy và Tập dữ liệu
9.6. Kiến trúc Mã hoá - Giải mã
9.7. Chuỗi sang Chuỗi
9.8. Tìm kiếm Chùm
9.9. Những người thực hiện
10. Cơ chế Tập trung
10.1. Cơ chế Tập trung
10.2. Chuỗi sang Chuỗi áp dụng Cơ chế Tập trung
10.3. Kiến trúc Transformer
10.4. Những người thực hiện
11. Thuật toán Tối ưu
11.1. Tối ưu và Học sâu
11.2. Các Thách thức của Tối ưu trong Học sâu
11.3. Các vùng Cực tiểu
11.4. Các điểm Yên ngựa
11.5. Tiêu biến Gradient
11.6. Tính lồi
11.7. Hạ Gradient
11.8. Hạ Gradient Ngẫu nhiên
11.9. Hạ Gradient Ngẫu nhiên theo Minibatch
11.10. Động lượng
11.11. Adagrad
11.12. RMSProp
11.13. Adadelta
11.14. Adam
11.15. Định thời Tốc độ Học
11.16. Những người thực hiện
12. Hiệu năng Tính toán
12.1. Trình biên dịch và Trình thông dịch
12.2. Tính toán Bất đồng bộ
12.3. Song song hóa Tự động
12.4. Phần cứng
12.5. Huấn luyện đa GPU
12.6. Cách lập trình Súc tích đa GPU
12.7. Máy chủ Tham số
12.8. Những người thực hiện
13. Thị giác Máy tính
13.1. Tăng cường Ảnh
13.2. Tinh Chỉnh
13.3. Phát hiện Vật thể và Khoanh vùng Đối tượng (Khung chứa)
13.4. Khung neo
13.5. Phát hiện Vật thể Đa tỷ lệ
13.6. Tập dữ liệu Phát hiện Đối tượng
13.7. Phát hiện Nhiều khung Một lượt (SSD)
13.8. CNN theo Vùng (R-CNN)
13.9. Phân vùng theo Ngữ nghĩa và Tập dữ liệu
13.10. Tích chập Chuyển vị
13.11. Mạng Tích chập Đầy đủ
13.12. Truyền tải Phong cách Nơ-ron
13.13. Phân loại ảnh (CIFAR-10) trên Kaggle
13.14. Nhận diện Giống Chó (ImageNet Dogs) trên Kaggle
13.15. Những người thực hiện
14. Xử lý Ngôn ngữ Tự nhiên: Tiền Huấn luyện
14.1. Embedding Từ (word2vec)
14.2. Huấn luyện Gần đúng
14.3. Tập dữ liệu để Tiền Huấn luyện Embedding Từ
14.4. Tiền huấn luyện word2vec
14.5. Embedding từ với Vector Toàn cục (GloVe)
14.6. Embedding từ con
14.7. Tìm kiếm từ Đồng nghĩa và Loại suy
14.8. Biểu diễn Mã hóa hai chiều từ Transformer (BERT)
14.9. Tập dữ liệu để Tiền huấn luyện BERT
14.10. Tiền Huấn luyện BERT
14.11. Những người thực hiện
15. Xử lý Ngôn ngữ Tự nhiên: Ứng dụng
15.1. Tác vụ Phân tích Cảm xúc và Bộ Dữ liệu
15.2. Phân tích Cảm xúc: Sử dụng Mạng Nơ-ron Hồi tiếp
15.3. Phân tích Cảm xúc: Sử dụng Mạng Nơ-ron Tích Chập
15.4. Suy luận ngôn ngữ tự nhiên và Tập dữ liệu
15.5. Suy luận Ngôn ngữ Tự nhiên: Sử dụng Cơ chế Tập trung
15.6. Tinh chỉnh BERT cho các Ứng dụng Cấp Chuỗi và Cấp Token
15.7. Suy luận Ngôn ngữ Tự nhiên: Tinh chỉnh BERT
15.8. Những người thực hiện
16. Hệ thống Đề xuất
16.1. Tổng quan về Hệ thống Đề xuất
16.2. Tập dữ liệu MovieLens
16.3. Phân rã Ma trận
16.4. AutoRec: Dự đoán Đánh giá với Bộ tự Mã hóa
16.5. Cá nhân hóa Xếp hạng trong Hệ thống Đề xuất
16.6. Lọc Cộng tác Nơ-ron cho Cá nhân hóa Xếp hạng
16.7. Hệ thống Đề xuất có Nhận thức về Chuỗi
16.8. Hệ thống Đề xuất Giàu Đặc trưng
16.9. Máy Phân rã ma trận
16.10. Máy Phân rã Ma trận Sâu
16.11. Những người thực hiện
17. Mạng Đối sinh
17.1. Mạng Đối sinh
17.2. Mạng Đối sinh Tích chập Sâu
18. Phụ lục: Toán học cho Học Sâu
18.1. Các phép toán Hình học và Đại số Tuyến tính
18.2. Phân rã trị riêng
18.3. Giải tích một biến
18.4. Giải tích Nhiều biến
18.5. Giải tích Tích phân
18.6. Biến Ngẫu nhiên
18.7. Hợp lý Cực đại
18.8. Các Phân phối Xác suất
18.9. Bộ phân loại Naive Bayes
18.10. Thống kê
18.11. Lý thuyết Thông tin
18.12. Những người thực hiện
19. Phụ lục: Công cụ cho Học Sâu
19.1. Sử dụng Jupyter
19.2. Sử dụng Amazon SageMaker
19.3. Sử dụng Máy ảo AWS EC2
19.4. Sử dụng Google Colab
19.5. Lựa chọn Máy chủ & GPU
19.6. Đóng góp cho Quyển sách
19.7. Tài liệu API của d2l
19.8. Những người thực hiện
Tài liệu tham khảo
Bảng thuật ngữ
