# Key
- vision - thị giác máy tính
- occlusion - tắc nghẽn
- SOTA - State-of-the-art
- Abstract - Tóm tắt
- FPS - Frame per second
- 9 DOF
- Framework - là các đoạn code đã được viết sẵn, cấu thành nên một bộ khung và các thư viện lập trình được đóng gói.

# Edit Word
Download: [thuyetminh_supermain_1447.docx](https://github.com/SlimeVRX/SlimeVRX/files/9100046/thuyetminh_supermain_1447.docx)


# Ước tính cơ thể người từ 6 cảm biến quán tính chi phí thấp trong thời gian thực

## Abstract: Tóm tắt

Khả năng ghi lại chuyển động của con người từ các cảm biến quán tính đã cho thấy tiềm năng lớn so với các phương pháp tiếp cận dựa trên thị giác máy tính vì không gặp phải hạn chế về không gian hoạt động và tắc nghẽn do các bộ phận cơ thể bị che khuất. Các nghiên cứu SOTA gần đây sử dụng cảm biến quán tính chuyên dụng của Xsens và Noitom có giá thành rất cao đồng thời yêu cầu máy tính sử dụng GPU dẫn đến việc triển khai trở nên tốn kém và khó phổ biến. Việc ghi lại chuyển động thời gian thực sử dụng cảm biến quán tính chi phí thấp và triển khai trên máy tính cấu hình thấp chỉ sử dụng CPU là một thách thức. Để đạt được mục đích này, chúng tôi trình bày tái tạo kết quả của bài báo Transpose sử dụng 6 cảm biến quán tính Hi229 chi phí thấp và tối ưu hóa mạng nơ-ron đạt tốc độ 24 khung hình / giây trên CPU i5-5200U trong thời gian thực. Các thí nghiệm chứng minh rằng các cảm biến quán tính chi phí thấp có thể được sử dụng để ghi lại chuyển động với độ chính xác và ổn định theo thời gian.

Keywords: IMU, Pose Estimation, Inverse Kinematics, Real-time, Low-cost

## 1\. Introduction: Giới thiệu

### 1.1\. Background: Khái quát

Chụp chuyển động nhằm mục đích tái tạo lại các chuyển động cơ thể con người 3D, đóng một vai trò quan trọng trong các ứng dụng khác nhau như chơi Game, thể thao, Y học, VR/AR và sản xuất phim. Cho đến nay, các giải pháp chụp chuyển động dựa trên thị giác máy tính chiếm phần lớn trong chủ đề này. Một trong những cách tiếp cận là dựa trên điểm đánh dấu, các điểm đánh dấu quang học được gắn trên cơ thể người và sử dụng nhiều máy ảnh để theo dõi các điểm đánh dấu để ghi lại chuyển động. Ví dự như hệ thống [Vicon](https://www.vicon.com/) được áp dụng rộng rãi và được xem xét là đủ chính xác cho việc sử dụng trong công nghiệp. Tuy nhiên, cách tiếp cận này yêu cầu cơ sở hạ tầng đắt tiền, điều này khiến chúng không được sử dụng ở cấp độ người tiêu dùng. Gần đây, một số cách tiếp cận khác sử dụng một vài máy ảnh RGB hoặc RGB-D [Chen et al. 2020];[Habibie et al. 2019];[Mehtaet al. 2020];[Tome et al. 2018];[Trumble et al. 2016];[Xiang et al. 2019]. So với cách tiếp cận sử dụng điểm đánh dấu, các cách tiếp cận này yêu cầu cơ sở hạ tần thấp hơn nhiều. Vì các đặc điểm của con người được trích xuất từ hình ảnh, do đó các phương pháp này thường hoạt động kém hiệu quả đối với môi trường ánh sáng khó khăn. Hơn nữa, tất cả các phương pháp tiếp cận dựa trên thị giác máy tính đều bị tắc nghẽn do các bộ phận cơ thể bị che khuất. Vấn đề này có thể được giải quyết bằng cách tăng số lượng camera. Điều này càng làm cho hệ thống trở nên nặng nề và tốn kém. Nhưng nó thường không thực tế trong một số ứng dụng. Ví dụ, rất khó bố trí máy ảnh trong một phòng sinh hoạt có nhiều đồ đạc, vật dụng, những đồ vật này có thể làm chủ thể bị che khuất từ bất kỳ hướng nào. Một hạn chế khác của phương pháp tiếp cận dựa trên tầm nhìn là bị hạn chế trong một không gian cố định. Đối với các hoạt động hàng ngày như đi bộ hoặc chạy trong phạm vi lớn, cần phải có camera chuyển động để ghi lại đủ thông tin, điều này rất khó đạt được [Xu et al. 2016]. Những nhược điểm này là những thiếu sót nghiêm trọng đối với nhiều ứng dụng, dẫn đến các hạn chế khi sử dụng giải pháp dựa trên thị giác máy tính.

Trái ngược với các hệ thống dựa trên thị giác, việc ghi lại chuyển động bằng cảm biến quán tính không gặp phải hạn chế về không gian hoạt động và tắc nghẽn do các bộ phận cơ thể bị che khuất. Nó cũng không yêu cầu thiết lập cơ sở hạ tầng phức tạp. Các đặc điểm này làm cho nó phù hợp hơn với các mục đích sử dụng ở cấp độ người tiêu dùng. Do đó, ghi lại chuyển động bằng cảm biến quán tính ngày càng được chú trọng hơn trong những năm gần đây. Hầu hết các nghiên cứu liên quan đều sử dụng Đơn vị đo lường quán tính (IMU) để ghi lại quán tính chuyển động, nó tiết kiệm, nhẹ, đáng tin cậy và thường được sử dụng trong một số lượng lớn các thiết bị đeo như đồng hồ, dây đeo tay và kính. Hệ thống chụp chuyển động quán tính thương mại [Xsens](https://www.xsens.com/) sử dụng 17 IMU để ước tính chuyển động quay của khớp. Mặc dù chính xác, sử dụng nhiều IMU gây bất tiện và ngăn cản người sử dụng di chuyển tự do. Mặt khác, các yêu cầu về cơ sở vật chất đối với một hệ thống như vậy vẫn nằm ngoài khả năng chấp nhận của người tiêu dùng bình thường. Nghiên cứu của SIP [Marcard et al 2017] chứng minh rằng việc tái tạo lại chuyển động của con người chỉ từ 6 IMU là hoàn toàn khả thi. Tuy nhiên, là một phương pháp dựa trên tối ưu hóa, nó cần phải truy cập vào toàn bộ chuỗi và mất nhiều thời gian để xử lý. Nghiên cứu SOTA gần đây, DIP [Huang et al 2018] cũng sử dụng 6 IMU đạt được hiệu suất thời gian thực với chất lượng tốt hơn bằng cách sử dụng biRNN. Tuy nhiên, nó vẫn không thành công ở các tư thế khó và tốc độ 30 khung hình / giây không đủ để chụp các chuyển động nhanh, rất phổ biến trong các ứng dụng thực tế. Quan trọng hơn, nó chỉ ước tính tư thế cơ thể mà không có ước tính chuyển động trong không gian 3D, vốn quan trọng trong nhiều ứng dụng như VR và AR. TransPose [Yi et al 2021] đã giải quyết vấn đề này và đạt được tiến bộ đầu tiên ước lượng dịch chuyển trong không gian 3D và ước tính tư thế cơ thể trong thời gian thực trong khi cũng chỉ sử dụng 6 IMU. Vì bản thân IMU không có khả năng đo khoảng cách trực tiếp. Một số công trình trước đây [Liu et al 2011]; [Vlasic et al 2007] sử dụng các cảm biến siêu âm bổ sung để tính toán chuyển động trong không gian 3D, chi phí cao và có thể bị tắc nghẽn. Các giải pháp khả thi khác sử dụng định vị GPS, cách này không đủ chính xác và chỉ hoạt động khi ghi chuyển động ngoài trời.

### 1.2\. Related work: Các nghiên cứu liên quan:

Chụp chuyển động đã có lịch sử nghiên cứu lâu đời, nhiều nghiên cứu đã được dành cho chủ đề này. Các phương pháp chụp chuyển động có thể được phân loại theo các thông số đầu vào, bao gồm các phương pháp kết hợp nhiều loại cảm biến. Có thể được phân loại thành: các phương pháp dựa trên thị giác máy tính, các phương pháp kết hợp thị giác máy tính và cảm biến quán tính và các phương pháp chỉ sử dụng cảm biến quán tính. 

#### 1.2.1\. Phương pháp chụp chuyển động dựa trên thị giác máy tính

Chụp chuyển động thương mại sử dụng một số lượng lớn các điểm đánh dấu và nhiều camera được hiệu chỉnh. Nhiều phương pháp đòi hỏi độ chính xác cao được tiến hành ngoại tuyến [25] [33]. Gần đây, các nghiên cứu thời gian thực cũng đã được đề xuất. VNect [4] là một nghiên cứu đại diện về ước tính tư thế con người động học 3D trong thời gian thực (30 Hz), kết hợp các mạng nơ-ron phức tạp. Các kỹ thuật học sâu đã cải thiện đáng kể phương pháp ước tính tư thế, Deep-Pose [62] đề xuất nghiên cứu ước tính tư thế 2D lớn đầu tiên của con người áp dụng mạng nơ-ron sâu (DNN), các mạng phức tạp (ConvNets) dựa trên phân tích chụp chuyển động không đánh dấu.

#### 1.2.2\. Phương pháp chụp chuyển động kết hợp thị giác máy tính và cảm biến quán tính

Khi các giải pháp chụp chuyển động dựa trên thị giác máy tính bị hiện tượng tắc nghẽn, việc kết hợp hình ảnh với IMU mang lại khả năng theo dõi chuyển động mạnh mẽ hơn. Điều này có thể đạt được bằng cách hồi quy tư thế của con người từ các tính năng kết hợp có nguồn gốc từ hình ảnh và IMU. [Zhang et al] đề xuất khai thác IMU trong ước tính tư thế 2D bằng cách kết hợp các đặc điểm hình ảnh của từng cặp khung xương được trích xuất từ hình ảnh liên kết với IMU. Một số hoạt động kết hợp IMU với hình ảnh độ sâu [18, 23, 90] hoặc điểm đánh dấu quang học để thực hiện chụp chuyển động. Tuy nhiên, các phương pháp này vẫn còn hạn chế đáng kể trong điều kiện ánh sáng yếu và tắc nghẽn, đồng thời yêu cầu phải di chuyển trong tầm nhìn của máy ảnh. Phương pháp của chúng tôi không yêu cầu đầu vào hình ảnh và do đó không có những hạn chế này.

#### 1.2.3\. Phương pháp chụp chuyển động dựa trên cảm biến quán tính

Các phương pháp sử dụng cảm biến quán tính là một cách tiếp cận khác để ghi lại chuyển động. Các giải pháp thương mại [Xsens MVN] thực hiện theo dõi chuyển động toàn thân bằng cách sử dụng 17 cảm biến IMU thực hiện các phép đo từ sự kết hợp của gia tốc kế, con quay hồi chuyển và từ kế. So với các phương pháp dựa trên tầm nhìn, chụp chuyển động IMU có tiềm năng sử dụng thực tế trong các tình huống ngoài phòng thí nghiệm vì nó không bị hạn chế về không gian hoạt động. Tuy nhiên, việc sử dụng một số lượng lớn các cảm biến quán sẽ làm chi phí tăng lên cao và tốn thời gian để thiết lập. Do đó, các nghiên cứu hiện nay đã tìm cách sử dụng một số lượng nhỏ cảm biến, mặc dù hiệu suất suy giảm. Một số nghiên cứu [43,44] đã xây dựng tư thế của con người chỉ bằng cách sử dụng năm gia tốc kế bằng cách truy xuất các tư thế được ghi sẵn với gia tốc từ cơ sở dữ liệu chụp chuyển động. Trong các nghiên cứu này, sự không ổn định đo lường của các cảm biến và kích thước của cơ sở dữ liệu đã ảnh hưởng lớn đến hiệu suất của phương pháp. Gần đây, nghiên cứu đã được tiến hành về việc giảm số lượng cảm biến bằng cách sử dụng các cảm biến quán tính có thể đo gia tốc và hướng đồng thời. Một công trình tiên phong trong lĩnh vực này, Sparse Inertial Poser (SIP) [14], đã trình bày một mô hình tối ưu hóa chung tái tạo tư thế của mô hình cơ thể SMPL [45] bằng cách sử dụng 6 IMU nhưng không dựa vào cơ sở dữ liệu. Cải tiến từ SIP, Deep Inertial Poser (DIP) [15] đã áp dụng phương pháp học sâu để chạy trong thời gian thực. DIP sử dụng BiRNN với các ô LSTM. Cách tiếp cận này có tiềm năng ước tính tư thế 3D thời gian thực trong môi trường VR, điều này đã cung cấp cho chúng tôi động lực lớn. Tuy nhiên, DIP không thể ước tính chuyển động trong không gian 3D của người dùng, đây là một thành phần bắt buộc của theo dõi chuyển động. [Yi et al] đề xuất TransPose để ước tính chuyển động trong không gian 3D bằng cách sử dụng phương pháp dựa trên chân hỗ trợ và phương pháp dựa trên RNN. TransPose đạt được hiệu suất SOTA về độ chính xác ước tính tư thế chỉ sử dụng 6 IMU.

### 1.3\. Motivation: Động lực

Các nghiên cứu SOTA gần đây sử dụng cảm biến quán tính chuyên dụng của Xsens và Noitom có giá thành rất cao đồng thời yêu cầu máy tính sử dụng GPU dẫn đến việc triển khai trở nên tốn kém và khó phổ biến. Không có một cách tiếp cận nào sử dụng cảm biến quán tính chi phí thấp. Việc ghi lại chuyển động thời gian thực sử dụng cảm biến quán tính chi phí thấp và triển khai trên máy tính cấu hình thấp chỉ sử dụng CPU là một thách thức. Vì vậy, chúng tôi giới thiệu cách tiếp cận của mình, tái tạo kết quả của bài báo TransPose, ước tính vị trí trong không gian 3D và tư thế cơ thể từ 6 IMU Hi229 chi phí thấp với CPU i5-5200U ở tốc độ 24 khung hình / giây thời gian thực.

### 1.4\. Objectives and Contributions:  Mục tiêu và đóng góp

Mục tiêu của nghiên cứu này tập trung vào việc triển khai lại kết quả bài báo Transpose sử dụng cảm biến quán tính chi phí thấp và chạy trên máy tính cấu hình thấp chỉ sử dụng CPU không cần GPU.

Trong luận án này chúng tôi có 2 đóng góp:
- Chuyển đổi hệ tọa độ cảm biến IMU, Transpose paper sử dụng cảm biến chuyên dụng của Noitom. Chúng tôi sử dụng cảm biến Hi229 chi phí thấp nên phải viết lại chuyển đổi hệ tọa độ để phù hợp với đầu vào Transpose model. Mở rộng, chúng tôi có thể thử nghiệm với bất kỳ IMU.
- Chuyển đổi model từ framework Pytorch sang ONNX tối ưu cho việc triển khai. Chúng tôi đã giảm yêu cầu phần cứng để triển khai từ cấu hình máy tính có GPU RTX 2080 sang cấu hình máy tính chỉ cần CPU i5-5200U Laptop đạt 24 khung hình / giây trong thời gian thực.

### 1.5\. Organization: Cấu trúc thuyết minh

Bài viết này được cấu trúc như sau. Chương 2 giới thiệu các nghiên cứu tài liệu liên quan đến luận án. Chương 3 trình bày chi tiết các chiến lược của chúng tôi, bao gồm kiến trúc mô phỏng tùy chỉnh và phương pháp giảng dạy. Chương 4 trình bày việc thực hiện thiết kế và các thí nghiệm. Chương 5 kết thúc luận án và đề xuất nghiên cứu trong tương lai.

Phương pháp đề xuất triển khai lại kết quả của bài báo Transpose sử dụng cảm biến quán tính chi phí thấp và chạy trên máy tính cấu hình thấp chỉ sử dụng CPU không cần GPU. 6 cảm biến quán tính Hi229 9-DOF chi phí thấp được sử dụng thay thế 6 cảm biến chuyên dụng Noitom được trình bày trong bài báo Transpose. Ngoài ra, chúng tôi triển khai lại cấu trúc mạng nơ-ron từ Pytorch framwork sang ONNX framwork tối ưu cho việc trển khai trên CPU. Trong luận án này, trước tiên chúng tôi giới thiệu kiến thức liên quan về IMU và mô tả ~giải thích~ phương pháp chuyển đổi hệ tọa độ IMU từ hệ tọa độ local riêng từng cảm biến sang global toàn bộ cảm biến (Phần 3.1). Sau đó, chúng tôi giới thiệu nền tảng kến thức liên quan về mạng nơ-ron và trình bày phương pháp chuyển đổi cấu trúc mạng nơ-ron từ Pytorch framwork sang ONNX framwork (Phần 3.2)

Bài viết này được cấu trúc như sau. Chương 2 giới thiệu các nghiên cứu tài liệu liên quan đến luận án. Chương 3 ... Chương 4 ...

## 2\. Tổng quan về IMU:

![image](https://user-images.githubusercontent.com/99313947/178130727-5ea3a0ac-a583-45b6-8d80-46c79b8b7e9d.png)

### 2.1\. IMU là gì?

Đơn vị đo lường quán tính - IMU là một loại cảm biến đặc biệt đo gia tốc, tốc độ góc và từ trường. IMU cơ bản sẽ bao gồm một gia tốc kế 3 trục và một con quay hồi chuyển 3 trục được gọi là IMU 6 trục. Tuy vậy đôi khi như thế vẫn là không đủ, những dự án phức tạp như là điều khiển máy bay hoặc robot có thể sẽ cần đến IMU 9 trục - thêm một cảm biến từ trường 3 trục hoạt động gần giống một la bàn để định hướng, hoặc IMU 10 trục - thêm một áp kế dùng để đo độ cao hoặc thậm chí 11 trục - thêm module GPS để xác định vị trí.

Về mặt kỹ thuật, thuật ngữ IMU chỉ dùng để chỉ cảm biến, nhưng IMU thường được ghép nối với phần mềm kết hợp cảm biến, kết hợp dữ liệu từ nhiều cảm biến để cung cấp các phép đo Orientation và Heading. Trong cách sử dụng phổ biến, thuật ngữ IMU có thể được sử dụng để chỉ sự kết hợp giữa cảm biến và phần mềm tổng hợp cảm biến, sự kết hợp này còn được gọi là AHRS (Attitude Heading Reference System).

### 2.2\. Nguyên lý hoạt động của từng loại cảm biến:

### 2.2.1\. Cảm biến gia tốc kế:

Gia tốc là một cảm biến quán tính được sử dụng phổ biến để đo gia tốc tuyến tính.

![image](https://user-images.githubusercontent.com/99313947/178685244-c6d9a6fa-1bbd-495f-bf77-49b53e085df2.png)

Gia tốc kế đo gia tốc cảm nhận theo ba trục, vì vậy khi đặt gia tốc kế nằm ngang và đứng yên trên trái đất, trị số đọc là 0,0,1G. Khi gia tốc kế nhận được gia tốc 1G theo chiều dương của trục X, trị số đọc là 1,0,1G

Trọng lực hướng xuống theo phương thẳng đứng, khi đặt gia tốc kế nằm ngang và đứng yên trên trái đất, trị số đọc là 0,0,1G, tại sao không phải 0,0,-1G. Điều này là do gia tốc kế cảm nhận được lực tác động ta từ bên ngoài đặt gia tốc kế như mô hình lò xo chứ không phải là một trường hấp dẫn.

![image](https://user-images.githubusercontent.com/99313947/178685691-80ec569e-48b8-4ed1-94ea-91bee845ab99.png)

Mô hình gia tốc kế

### 2.2.2\. Cảm biến con quay hồi chuyển:

Khi bạn đặt một con chip IMU để im không chuyển động, giá trị trả về gyro = [0.0, 0.0, 0.0] do không có bất cứ chuyển động quay nào cả. Gyro chỉ đo tốc độ quay chứ không đo trực tiếp góc quay, nên khi bạn quay module một góc nào đó rồi dừng, giá trị của gyro sẽ tăng lên rồi hạ xuống về 0.

Con quay hồi chuyển đo vận tốc góc ba trục, nói thẳng ra là nó đo chuyển động quay quanh mỗi trục, nó còn được gọi là cảm biến vận tốc góc và cũng là một thiết bị quán tính. Khi IMU để im không chuyển động, giá trị trả về Gyroscope = [0.0, 0.0, 0.0] do không có bất cứ chuyển động quay nào, khi quay module một góc nào đó rồi dừng, giá trị của Gyroscope sẽ tăng lên rồi hạ xuống về 0.

![image](https://user-images.githubusercontent.com/99313947/178686484-b9832622-3251-4476-9b3e-52e194b03971.png)

Gia tốc kế + Con quay hồi chuyển được gọi là IMU, hay được gọi là cảm biến IMU 6 trục

### 2.2.3\. Cảm biến trường địa từ:

Cảm biến trường địa từ đo cường độ từ trường theo ba trục bao gồm từ trường địa từ và các từ trường gây nhiễu khác gần đó chẳng hạn như nam châm, vật kim loại,...

![image](https://user-images.githubusercontent.com/99313947/178687032-9984eb12-86ad-49b3-ab10-5942a6bd95e6.png)

Được gọi là cảm biến 9 trục, hoặc MARG (Magnetic, Angular Rate, and Gravity sensors). Nếu được kết hợp với một vi máy tính chip đơn, nó sẽ có sức mạnh xử lý + thuật toán thích hợp, nó có thể được gọi là AHRS.

### 2.2.4\. Từ trường của trái đất:

Sự phân bố hình học của từ trường trái đất rất không đều. Các đường sức từ bắt đầu từ cực nam và quay trở lại cực bắc của từ trường

![image](https://user-images.githubusercontent.com/99313947/178705645-1577e28b-cee5-48f4-a4ac-bac48a93cbbf.png)

Chú ý đến chiều của các đường sức từ: từ cực nam đến cực bắc của đường sức từ.

Đối với bán cầu bắc, hướng của địa từ nghiêng xuống và đối với bán cầu nam, hướng của địa từ nghiêng lên trên.

![image](https://user-images.githubusercontent.com/99313947/178705874-41752473-736a-4045-85bb-7e1ac3eecebd.png)

Một trường địa từ điển hình ở bán cầu bắc

Dòng Cường độ là giá trị đọc của cảm biến từ trường 3 trục, là vectơ không gian ba chiều. Mô đun của Cường độ từ trường

![image](https://user-images.githubusercontent.com/99313947/178706904-a368b25b-a170-4bf6-ba9c-35be9049609e.png)

- Declination - độ từ thiên: Góc giữa từ trường Trái đất và hướng bắc địa lý.
- Inclination - độ từ khuynh: Góc giữa từ trường Trái đất và phương nằm ngang.
- Chuyển đổi đơn vị: Đơn vị phổ biến: MicroTesla (uT), MilliGauss (mGauss)
- 1 uT = 10 mGauss, phạm vi của trường địa từ: 250 - 650 mGauss hoặc 25 - 64 uT

Trong hệ tọa độ NED

![image](https://user-images.githubusercontent.com/99313947/178708119-2fffdddd-4886-49f7-950c-18beef83756c.png)

Công thức tính vectơ trường địa từ
Với:
- ![image](https://user-images.githubusercontent.com/99313947/178708225-40a00f7b-6359-4e73-b689-62dcc4376b6d.png) Độ từ thiên
- ![image](https://user-images.githubusercontent.com/99313947/178708323-6f9af4f5-0878-43cb-b027-34158260268b.png) Độ từ khuynh
- ![image](https://user-images.githubusercontent.com/99313947/178708406-1b8a9362-edd2-4a5f-8ed5-af0b232db074.png) Độ lớn của từ trường trái đất

Ví dụ, các thông số chi tiết về địa từ trường của Đà Nẵng được kiểm tra thông qua trang web của [NOAA](https://www.ngdc.noaa.gov/geomag/calculators/magcalc.shtml#igrfwmm) là:

![image](https://user-images.githubusercontent.com/99313947/178709653-bca5ca07-7867-431d-a8cc-0c7e3af9b131.png)

Có thể thấy, tổng cường độ từ trường tại khu vực Đà Nẵng là ~ 43uT, thành phần thẳng đứng: 16uT, thành phần ngang: 40uT, Inclination: 21 °, Declination: -1 °

## 3\. Chuyển đổi hệ tọa độ cảm biến quán tính IMU

Vì mỗi cảm biến quán tính có hệ tọa độ riêng, nên trước tiên chúng ta cần chuyển đổi các phép đo quán tính thô thành cùng một hệ quy chiếu, được gọi là Hiệu chuẩn - calibration, và sau đó biến đổi quán tính khớp lá - leaf joint về không gian của khớp gốc - root và thay đổi tỉ lệ thành kích thước phù hợp cho đầu vào mạng nơ-ron, được gọi là Chuẩn hóa - normalization. Các cảm biến có thể được đặt với các góc quay tùy ý trong quá trình thiết lập và phương pháp của chúng tôi tự động tính toán các ma trận chuyển tiếp cho từng cảm biến trước khi ghi lại chuyển động. Quá trình này yêu cầu đối tượng giữ tư thế chữ T trong vài giây. Trong phần này, chúng tôi giải thích chi tiết về tiền xử lý cảm biến trong phương pháp của chúng tôi, bao gồm các công việc Hiệu chuẩn [Phần A.1] và Chuẩn hóa [Phần A.2]

### 3.1\. Hiệu chuẩn:

![image](https://user-images.githubusercontent.com/99313947/178522537-1677cddd-e524-4dec-8fa6-d66794033109.png)

Quy ước:
-	V: hệ mô phỏng SMPL (Virtual)
-	S: hệ khớp xương (Arm)
-	I: hệ cảm biến (IMU)
-	E: hệ trục trái đất (Global)
-	M: ma trận xoay (Rotation matrix)

Do vị trí và trạng thái của cảm biến lúc đặt lên người là ở trạng thái tự do nên sẽ không có một cơ sở nào để mô hình có thể hiểu được các giá trị của mô hình nên ta cần phải canh chỉnh lại cũng như chuyển đổi giá trị trong hệ trục trái đất sang hệ trục dùng trong mô phỏng. Giả dữ liệu thí nghiệm, ta nhận thấy rằng cảm biến gắn trên một khớp xương nào đó sẽ tạo ra một góc quay cố định. Và sự quay trên cảm biến cũng kéo theo sự quay trên khớp xương. Từ đó tìm ra sự phụ thuộc của góc quay đó tìm góc quay của khớp xương trong hệ mô phỏng.

Trước khi chụp chuyển động, trước tiên chúng tôi đặt một IMU với các trục của khung tọa độ cảm biến của nó căn chỉnh với các trục tương ứng của khung tọa độ SMPL, tức là đặt IMU với X - trục bên trái, Y - trục lên trên và Z - trục về phía trước trong thế giới thực. Trong hệ trục trái đất trục X hướng về phía Bắc, trục Y hướng về phía Tây và trục Z hướng lên. Do hệ trục mô phỏng SMPL không trùng với hệ trục trái đất nên ta có ma trận xoay từ trái đất sang mô phỏng SMPL:

![image](https://user-images.githubusercontent.com/99313947/178567904-9b5f5ab5-6cfa-401d-813c-c3ae41ff6d1d.png)

Một vector trong khớp xương có thể được thể hiện bằng một vector khác trong hệ mô phỏng bằng cách nhân với ma trận xoay của khớp xương ở phía trước.

![image](https://user-images.githubusercontent.com/99313947/178571166-6c1ff95b-ac03-4bf7-9b29-335fbd990479.png) (1)

Tiếp theo, chúng tôi đặt từng IMU lên phần cơ thể tương ứng với các hướng tùy ý và giữ yên ở tư thế chữ T trong vài giây.
Chúng tôi đọc các phép đo IMU và tính toán gia tốc trung bình và định hướng của mỗi cảm biến. Ta có các ma trận xoay của cảm biến được tính ra từ các giá trị Quaternion trên cảm biến:

![image](https://user-images.githubusercontent.com/99313947/178567330-60e4fd36-5be7-463f-a799-f89d98abcf66.png)

Cảm biến với khớp xương có một góc quay với ma trận xoay cố định ![image](https://user-images.githubusercontent.com/99313947/178572002-df961eef-6094-44c7-80f1-79a1cd3815a5.png) nên khi ở một tư thế bất kì thì vector trong khung xương có thể được tính từ vector của cảm biến với. Giả định rằng các góc giữa cảm biến và xương là hằng số. 

![image](https://user-images.githubusercontent.com/99313947/178572199-761748d6-a077-40ec-b7bc-6f08b548f5d3.png) (2)

Ở tư thế chữ T thì vector trong khớp xương trùng với vector trong hệ mô phỏng nên ta có:

![image](https://user-images.githubusercontent.com/99313947/178572292-94e109a5-6a2b-401c-b3dc-c18ab8976cfd.png) (3)

Để chuyển đổi từ hệ trái đất sang hệ mô phỏng ta dùng công thức:

![image](https://user-images.githubusercontent.com/99313947/178572460-6c1e268d-452f-43e1-85ed-fe7edd17635a.png) (4)

Trong hệ trục trái đất, vector có thể được tính từ vector của cảm biến với góc quay của nó.

![image](https://user-images.githubusercontent.com/99313947/178572525-e5bcdb5c-60d7-4485-b208-90a67c5700cb.png) (5)

Từ (3) và (4) ta có:

![image](https://user-images.githubusercontent.com/99313947/178572578-b1a144b3-1fd6-41ca-b7fc-4bc33d1b326c.png) (6)

Từ (5) và (6) ta có:

![image](https://user-images.githubusercontent.com/99313947/178572659-ec5d7d8a-5f2f-4893-9561-d305cf9947c7.png) (7)

Từ (2) và (7) ta có:

![image](https://user-images.githubusercontent.com/99313947/178572710-f95b1a25-f14b-4bb9-86ea-8052291bee54.png) (8)

Từ (1), (4) và (5) ta có:

![image](https://user-images.githubusercontent.com/99313947/178572797-bf97390d-6a13-408d-903b-1dde82d9286a.png) (9)

Từ (8) và (9) ta có:

![image](https://user-images.githubusercontent.com/99313947/178572874-ead84c6d-e14a-472b-b8d5-7d1e1f43e36d.png)

Do đó ta có ma trận xoay của khớp xương trong hệ mô phỏng được tính từ ma trận xoay của cảm biến:

![image](https://user-images.githubusercontent.com/99313947/178572962-753779a1-1219-4752-9c2a-a8cd093a3290.png)

### 3.2\. Chuẩn hóa:

Chúng tôi giải thích quy trình chuẩn hóa của chúng tôi trong phần này. Đối với mỗi khung hình, đầu vào thô là gia tốc
[𝒂root, · · ·, 𝒂rarm] ∈ R 3x6 và định hướng (Orientation) [Rroot, · · ·, Rrarm] ∈ R 3x3x6 đo bằng IMU. Chúng tôi chuyển các phép đo này từ hệ tọa độ riêng của chúng sang hệ quy chiếu SMPL, thu được 𝒂 và R như được mô tả trong [Phần A.1] . Sau đó, chúng tôi căn chỉnh các phép đo quán tính khớp lá - leaf joint đối với gốc - root và Chuẩn hóa các phép đo khớp gốc - root. Cuối cùng, chúng tôi thay đổi tỉ lệ gia tốc để phù hợp kích thước mạng nơ-ron.


## 4\. Lý thuyết mạng nơ-ron:

![image](https://user-images.githubusercontent.com/99313947/178130684-6cc7fc80-11de-4426-b7db-3b272c8770e8.png)

## 5\. Chuyển đổi mạng nơ-ron từ Pytorch sang ONNX:

Bên cạnh việc nghiên cứu ra các mô hình học sâu ngày càng chính xác thì việc triển khai mô hình cũng không kém phần quan trọng và gặp nhiều thách thức. Đặc biệt trong việc chuyển từ mô hình được viết bằng Framework này sang Framework khác vì mỗi thư viện có các hàm và kiểu dữ liệu khác nhau. Pytorch thường được sử dụng trong nghiên cứu thử nghiệm mô hình vì dễ sử dụng và cộng đồng nghiên cứu cũng dùng Pytorch nhiều rất tiện việc tra cứu. ONNX là một công cụ tối ưu để triển khai các mô hình suy luận hiệu suất cao.

## 5.1\. ONNX là gì?

![image](https://user-images.githubusercontent.com/99313947/178598082-cc409451-a4c3-4362-8e3e-d90c13fd6cc1.png)

ONNX là viết tắt của Open Neural Network Exchange, là một công cụ đóng vai trò như một trung gian hỗ trợ chuyển đổi mô hình học máy từ các framework khác nhau về dạng ONNX cung cấp nhờ đó giúp chúng ta chuyển đổi dễ dàng giữa các framework khác nhau. ONNX hỗ trợ chuyển đổi giữa nhiều framework phổ biến hiện nay như Keras, Tensorfow, Scikit-learn, Pytorch và XGBoost.

Vậy ONNX cung cấp:

- Cung cấp đồ thị biểu diễn chuẩn: Mỗi framework khác nhau sẽ có đồ thị biểu diễn tính toán khác nhau. ONNX cung cấp một đồ thị chuẩn được biểu diễn bằng nhiều nút tính toán có thể biểu diễn đồ thị của tất cả framework.
- Cung cấp kiểu dữ liệu chuẩn: ONNX cung cấp các kiểu dữ liệu chuẩn bao gồm int8,int16, float16, ...
- Cung cấp các hàm chuẩn: ONNX cung cấp các hàm có thể chuyển đổi với các hàm tương ứng trong framework mong muốn. Ví dụ hàm softmax trong torch sẽ được chuyển tương ứng thành hàm softmax trong ONNX.

## 5.2\. Chuyển mô hình Transpose từ Pytorch sang ONNX

- Bước 1: Import thư viện và khởi tạo cấu hình cần thiết

```
!git clone https://github.com/SlimeVRX/TransPose.git
!pip install chumpy
!pip install onnx
!pip install onnxruntime

%cd TransPose
```

- Bước 2: Xây dựng mô hình và tải pretrained weight

```
import torch
from net import TransPoseNet
from config import paths
from utils import normalize_and_concat
import os
import articulate as art


device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
net = TransPoseNet().to(device)

imu = torch.randn(26, 72).to(device)
rnn_state_0 = torch.randn(2, 1, 256).to(device)
rnn_state_1 = torch.randn(2, 1, 256).to(device)
rnn_state = tuple([rnn_state_0, rnn_state_1])
```

```
net
TransPoseNet(
  (pose_s1): RNN(
    (rnn): LSTM(256, 256, num_layers=2, bidirectional=True)
    (linear1): Linear(in_features=72, out_features=256, bias=True)
    (linear2): Linear(in_features=512, out_features=15, bias=True)
    (dropout): Dropout(p=0.2, inplace=False)
  )
  (pose_s2): RNN(
    (rnn): LSTM(64, 64, num_layers=2, bidirectional=True)
    (linear1): Linear(in_features=87, out_features=64, bias=True)
    (linear2): Linear(in_features=128, out_features=69, bias=True)
    (dropout): Dropout(p=0.2, inplace=False)
  )
  (pose_s3): RNN(
    (rnn): LSTM(128, 128, num_layers=2, bidirectional=True)
    (linear1): Linear(in_features=141, out_features=128, bias=True)
    (linear2): Linear(in_features=256, out_features=90, bias=True)
    (dropout): Dropout(p=0.2, inplace=False)
  )
  (tran_b1): RNN(
    (rnn): LSTM(64, 64, num_layers=2, bidirectional=True)
    (linear1): Linear(in_features=87, out_features=64, bias=True)
    (linear2): Linear(in_features=128, out_features=2, bias=True)
    (dropout): Dropout(p=0.2, inplace=False)
  )
  (tran_b2): RNN(
    (rnn): LSTM(256, 256, num_layers=2)
    (linear1): Linear(in_features=141, out_features=256, bias=True)
    (linear2): Linear(in_features=256, out_features=3, bias=True)
    (dropout): Dropout(p=0.2, inplace=False)
  )
)
```
- Bước 3: Chuyển mô hình về dạng ONNX

Một số tham số của hàm export:

- model: mô hình đã được load weight
- dummy input: một tensor hoặc một tuple chứa nhiều tensor tượng trưng cho đầu vào của model
- save_path: đường dẫn nơi lưu mô hình sau khi convert
- Input names: đặt tên cho tham số đầu vào
- output_names: đặt tên cho các giá trị trả về
- export_params: Xác định có dùng pretrained weight hay không ? Có đặt là True
- verbose: Bằng True thì sẽ in ra đồ thị mô hình dưới dạng con người có thể đọc được

Export mô hình Transpose
```
# Model conversion to onnx
model_onnx_path_3 = "model_33.onnx"
torch.onnx.export(
    net, 
    args=(imu, rnn_state),
    f=model_onnx_path_3,
    export_params=True,
    opset_version=11,
    input_names=["sequence_1", "sequence_2", "sequence_3"],
    output_names=["output"],
    dynamic_axes={
        "sequence_1": {0: "batch_size"},
        "sequence_2": {0: "batch_size"},
        "sequence_3": {0: "batch_size"},
        "output": {0: "batch_size"}
    }
)
```
Sử dụng phần mềm Netron để xem mạng nơ-ron sau khi chuyển đổi

- Trước 

![weights](https://user-images.githubusercontent.com/99313947/178601341-d55ac6e7-51be-4c0b-9483-f19a654ed2d7.png)

- Sau

![model_11](https://user-images.githubusercontent.com/99313947/178601331-9a28c136-390c-42e0-862a-5262c89b5d81.png)
