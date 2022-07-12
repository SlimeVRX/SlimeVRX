# Key
- vision - thị giác máy tính
- occlusion - tắc nghẽn
- SOTA - State-of-the-art
- Abstract - Tóm tắt
- FPS - Frame per second
- 9 DOF
- Framework - là các đoạn code đã được viết sẵn, cấu thành nên một bộ khung và các thư viện lập trình được đóng gói.

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

## 2\. Lý thuyết về IMU:

![image](https://user-images.githubusercontent.com/99313947/178130727-5ea3a0ac-a583-45b6-8d80-46c79b8b7e9d.png)

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

![image](https://user-images.githubusercontent.com/99313947/178598082-cc409451-a4c3-4362-8e3e-d90c13fd6cc1.png)
