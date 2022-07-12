# Key
- vision - thị giác máy tính
- occlusion - tắc nghẽn
- SOTA - State-of-the-art
- Abstract - Tóm tắt
- FPS - Frame per second
- 9 DOF

# Ước tính cơ thể người từ 6 cảm biến quán tính chi phí thấp trong thời gian thực

## Abstract: Tóm tắt

Khả năng ghi lại chuyển động của con người từ các cảm biến quán tính đã cho thấy tiềm năng lớn so với các phương pháp tiếp cận dựa trên thị giác máy tính vì không gặp phải hạn chế về không gian hoạt động và tắc nghẽn do các bộ phận cơ thể bị che khuất. Các nghiên cứu SOTA gần đây sử dụng cảm biến quán tính chuyên dụng của Xsens và Noitom có giá thành rất cao đồng thời yêu cầu máy tính sử dụng GPU dẫn đến việc triển khai trở nên tốn kém và khó phổ biến. Việc ghi lại chuyển động thời gian thực sử dụng cảm biến quán tính chi phí thấp và triển khai trên máy tính cấu hình thấp chỉ sử dụng CPU là một thách thức. Để đạt được mục đích này, chúng tôi trình bày tái tạo kết quả của bài báo Transpose sử dụng 6 cảm biến quán tính Hi229 chi phí thấp và tối ưu hóa mạng Neural Network đạt tốc độ 24 khung hình / giây trên CPU i5-5200U trong thời gian thực. Các thí nghiệm chứng minh rằng các cảm biến quán tính chi phí thấp có thể được sử dụng để ghi lại chuyển động với độ chính xác và ổn định theo thời gian.

Keywords: IMU, Pose Estimation, Inverse Kinematics, Real-time, Low-cost

## 1\. Introduction: Giới thiệu

### 1.1\. Background: Khái quát

Chụp chuyển động nhằm mục đích tái tạo lại các chuyển động cơ thể con người 3D, đóng một vai trò quan trọng trong các ứng dụng khác nhau như chơi Game, thể thao, Y học, VR/AR và sản xuất phim. Cho đến nay, các giải pháp chụp chuyển động dựa trên thị giác máy tính chiếm phần lớn trong chủ đề này. Một trong những cách tiếp cận là dựa trên điểm đánh dấu, các điểm đánh dấu quang học được gắn trên cơ thể người và sử dụng nhiều máy ảnh để theo dõi các điểm đánh dấu để ghi lại chuyển động. Ví dự như hệ thống [Vicon](https://www.vicon.com/) được áp dụng rộng rãi và được xem xét là đủ chính xác cho việc sử dụng trong công nghiệp. Tuy nhiên, cách tiếp cận này yêu cầu cơ sở hạ tầng đắt tiền, điều này khiến chúng không được sử dụng ở cấp độ người tiêu dùng. Gần đây, một số cách tiếp cận khác sử dụng một vài máy ảnh RGB hoặc RGB-D [Chen et al. 2020];[Habibie et al. 2019];[Mehtaet al. 2020];[Tome et al. 2018];[Trumble et al. 2016];[Xiang et al. 2019]. So với cách tiếp cận sử dụng điểm đánh dấu, các cách tiếp cận này yêu cầu cơ sở hạ tần thấp hơn nhiều. Vì các đặc điểm của con người được trích xuất từ hình ảnh, do đó các phương pháp này thường hoạt động kém hiệu quả đối với môi trường ánh sáng khó khăn. Hơn nữa, tất cả các phương pháp tiếp cận dựa trên thị giác máy tính đều bị tắc nghẽn do các bộ phận cơ thể bị che khuất. Vấn đề này có thể được giải quyết bằng cách tăng số lượng camera. Điều này càng làm cho hệ thống trở nên nặng nề và tốn kém. Nhưng nó thường không thực tế trong một số ứng dụng. Ví dụ, rất khó bố trí máy ảnh trong một phòng sinh hoạt có nhiều đồ đạc, vật dụng, những đồ vật này có thể làm chủ thể bị che khuất từ bất kỳ hướng nào. Một hạn chế khác của phương pháp tiếp cận dựa trên tầm nhìn là bị hạn chế trong một không gian cố định. Đối với các hoạt động hàng ngày như đi bộ hoặc chạy trong phạm vi lớn, cần phải có camera chuyển động để ghi lại đủ thông tin, điều này rất khó đạt được [Xu et al. 2016]. Những nhược điểm này là những thiếu sót nghiêm trọng đối với nhiều ứng dụng, dẫn đến các hạn chế khi sử dụng giải pháp dựa trên thị giác máy tính.

Trái ngược với các hệ thống dựa trên thị giác, việc ghi lại chuyển động bằng cảm biến quán tính không gặp phải hạn chế về không gian hoạt động và tắc nghẽn do các bộ phận cơ thể bị che khuất. Nó cũng không yêu cầu thiết lập cơ sở hạ tầng phức tạp. Các đặc điểm này làm cho nó phù hợp hơn với các mục đích sử dụng ở cấp độ người tiêu dùng. Do đó, ghi lại chuyển động bằng cảm biến quán tính ngày càng được chú trọng hơn trong những năm gần đây. Hầu hết các nghiên cứu liên quan đều sử dụng Đơn vị đo lường quán tính (IMU) để ghi lại quán tính chuyển động, nó tiết kiệm, nhẹ, đáng tin cậy và thường được sử dụng trong một số lượng lớn các thiết bị đeo như đồng hồ, dây đeo tay và kính. Hệ thống chụp chuyển động quán tính thương mại [Xsens](https://www.xsens.com/) sử dụng 17 IMU để ước tính chuyển động quay của khớp. Mặc dù chính xác, sử dụng nhiều IMU gây bất tiện và ngăn cản người sử dụng di chuyển tự do. Mặt khác, các yêu cầu về cơ sở vật chất đối với một hệ thống như vậy vẫn nằm ngoài khả năng chấp nhận của người tiêu dùng bình thường. Nghiên cứu của SIP [Marcard et al 2017] chứng minh rằng việc tái tạo lại chuyển động của con người chỉ từ 6 IMU là hoàn toàn khả thi. Tuy nhiên, là một phương pháp dựa trên tối ưu hóa, nó cần phải truy cập vào toàn bộ chuỗi và mất nhiều thời gian để xử lý. Nghiên cứu SOTA gần đây, DIP [Huang et al 2018] cũng sử dụng 6 IMU đạt được hiệu suất thời gian thực với chất lượng tốt hơn bằng cách sử dụng biRNN. Tuy nhiên, nó vẫn không thành công ở các tư thế khó và tốc độ 30 khung hình / giây không đủ để chụp các chuyển động nhanh, rất phổ biến trong các ứng dụng thực tế. Quan trọng hơn, nó chỉ ước tính tư thế cơ thể mà không có ước tính chuyển động trong không gian 3D, vốn quan trọng trong nhiều ứng dụng như VR và AR. TransPose [Yi et al 2021] đã giải quyết vấn đề này và đạt được tiến bộ đầu tiên ước lượng dịch chuyển trong không gian 3D và ước tính tư thế cơ thể trong thời gian thực trong khi cũng chỉ sử dụng 6 IMU. Vì bản thân IMU không có khả năng đo khoảng cách trực tiếp. Một số công trình trước đây [Liu et al 2011]; [Vlasic et al 2007] sử dụng các cảm biến siêu âm bổ sung để tính toán chuyển động trong không gian 3D, chi phí cao và có thể bị tắc nghẽn. Các giải pháp khả thi khác sử dụng định vị GPS, cách này không đủ chính xác và chỉ hoạt động khi ghi chuyển động ngoài trời.

### 1.2\. Related work: Các nghiên cứu liên quan:

Chụp chuyển động đã có lịch sử nghiên cứu lâu đời, nhiều nghiên cứu đã được dành cho chủ đề này. Các phương pháp chụp chuyển động có thể được phân loại theo các thông số đầu vào, bao gồm các phương pháp kết hợp nhiều loại cảm biến. Có thể được phân loại thành: các phương pháp dựa trên thị giác máy tính, các phương pháp kết hợp thị giác máy tính và cảm biến quán tính và các phương pháp chỉ sử dụng cảm biến quán tính. 

#### 1.2.1\. Phương pháp chụp chuyển động dựa trên thị giác máy tính

Chụp chuyển động thương mại sử dụng một số lượng lớn các điểm đánh dấu và nhiều camera được hiệu chỉnh. Nhiều phương pháp đòi hỏi độ chính xác cao được tiến hành ngoại tuyến [25] [33]. Gần đây, các nghiên cứu thời gian thực cũng đã được đề xuất. VNect [4] là một nghiên cứu đại diện về ước tính tư thế con người động học 3D trong thời gian thực (30 Hz), kết hợp các mạng Neural Network phức tạp. Các kỹ thuật học sâu đã cải thiện đáng kể phương pháp ước tính tư thế, Deep-Pose [62] đề xuất nghiên cứu ước tính tư thế 2D lớn đầu tiên của con người áp dụng mạng Neural Network sâu (DNN), các mạng phức tạp (ConvNets) dựa trên phân tích chụp chuyển động không đánh dấu.

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

Phương pháp đề xuất triển khai lại kết quả của bài báo Transpose sử dụng cảm biến quán tính chi phí thấp và chạy trên máy tính cấu hình thấp chỉ sử dụng CPU không cần GPU. 6 cảm biến quán tính Hi229 9-DOF chi phí thấp được sử dụng thay thế 6 cảm biến chuyên dụng Noitom được trình bày trong bài báo Transpose. Ngoài ra, chúng tôi triển khai lại cấu trúc mạng Neural Network từ Pytorch framwork sang ONNX framwork tối ưu cho việc trển khai trên CPU. Trong luận án này, trước tiên chúng tôi giới thiệu kiến thức liên quan về IMU và mô tả ~giải thích~ phương pháp chuyển đổi hệ tọa độ IMU từ hệ tọa độ local riêng từng cảm biến sang global toàn bộ cảm biến (Phần 3.1). Sau đó, chúng tôi giới thiệu nền tảng kến thức liên quan về mạng Neural Network và trình bày phương pháp chuyển đổi cấu trúc mạng Neural Network từ Pytorch framwork sang ONNX framwork (Phần 3.2)

Bài viết này được cấu trúc như sau. Chương 2 giới thiệu các nghiên cứu tài liệu liên quan đến luận án. Chương 3 ... Chương 4 ...

## 2\. Lý thuyết về IMU:
### 2.1\. Tổng quan về cảm biến quán tính IMU:
#### 2.1.1\. Cảm biến quán tính IMU là gì?:

Inertial Measurement Unit = Đơn vị đo lường quán tính, có chức năng cung cấp thông tin về tốc độ góc và góc nghiêng của hệ thống. Dựa trên nguyên lý hoạt động của 2 cảm biến accelemeter (gia tốc kế) và gyroscope ( con quay hồi chuyển ). Tuy nhiên khái niệm này được sử dụng khá lỏng lẻo: do vậy IMU có thể hiểu là đơn vị đo lường quán tính của hệ thống, cung cấp các giá trị cảm biến sau khi đã xử lý giúp cho hệ thống hoạt động tốt nhất.

IMU  cơ bản sẽ bao gồm 6-DOF (6 Degrees Of Freedom) tức là 6 trục độc lập (3 của accel và 3 của gyro). Tuy vậy đôi khi như thế vẫn là không đủ, những dự án phức tạp như là điều khiển máy bay hoặc robot có thể sẽ cần đến 9-DOF (thêm một cảm biến từ trường 3 trục – magnetometer – hoạt động gần giống một la bàn để định hướng), hoặc 10-DOF (thêm một áp kế – barometer – dùng để đo độ cao) hoặc thậm chí 11-DOF (thêm module GPS để xác định vị trí).

#### 2.1.2\. Ứng dụng của IMU:

Các cảm biến IMU được sử dụng trong các ứng dụng như: robot tự cân bằng, quadcopter, điện thoại thông minh hay đề tài chúng em đang nghiên cứu là ước tính cơ thể người…. Cảm biến IMU giúp chúng ta có được vị trí của vật thể gắn với cảm biến trong không gian ba. Chúng được sử dụng để phát hiện hướng của điện thoại thông minh hoặc trong các tiện ích như Fitbit, sử dụng cảm biến IMU để theo dõi chuyển động.
Module cảm biến IMU có thể được tích hợp gồm hai hoặc nhiều cảm biến như:
•	Cảm biến gia tốc (Accelemeter)
•	Cảm biến góc quay (Gyroscope)
•	Cảm biến từ trường (Magnetometer)

#### 2.1.3\. Nguyên lý hoạt động của từng loại cảm biến:

##### 2.1.3.1\ Cảm biến gia tốc kế Accelemeter:

Khi bạn đặt một con chip IMU để im không chuyển động, giá trị trả về gyro = [0.0, 0.0, 0.0] do không có bất cứ chuyển động quay nào cả. Gyro chỉ đo tốc độ quay chứ không đo trực tiếp góc quay, nên khi bạn quay module một góc nào đó rồi dừng, giá trị của gyro sẽ tăng lên rồi hạ xuống về 0.

##### 2.1.3.2\ Cảm biến con quay hồi chuyển Gyroscope:

Nguyên tắc để đo góc dùng gia tốc kế là phân tích sự tác dụng của trọng lực lên các trục ta có thể dùng nó để tính các góc lệch roll và pitch.

##### 2.1.3.3\ Cảm biến từ trường Magnetometer:

[Hình]

Cảm biến từ trường đa phần hoạt động dựa trên hiệu ứng Hall. Ta cấp nguồn cho dòng eletron chạy qua mạch, có một tấm dẫn điện như trên hình.

[Hình]

Khi xung quanh nó có từ trường, lực Lorent sẽ làm dòng eletron chạy trong mạch nó di chuyển lệch đi về 2 phía. Nếu ta đo điện áp thì sẽ biết được độ lớn của nguồn từ trường này.

Nếu chọn trục z là trục vuông góc với mặt đất thì góc yaw là góc khi xoay trục z. Nó thường được ứng dụng để đo góc yaw bằng công thức đơn giản. Trên thực tế ta có thể tính toán góc yaw bằng gyroscope, nhưng nếu ta kết hợp thêm cảm biến từ trường nó sẽ cho kết quả chính xác hơn, lấp đi nhược điểm khi dùng gyroscope.


#### 2.1.4\. Đặc tính của một số loại cảm biến:

##### 2.1.4.1\ Cảm biến gia tốc kế Accelemeter:

Vấn đề thường gặp phải nhất của gyro là drift = độ trôi, nó thay đổi chậm theo thời gian. Nguyên nhân bởi vì do các tác động cơ khí, rung động tác động lên gyro, sau một thời gian sử dụng thì giá trị trôi này tích lũy lên đáng kể, làm giá trị đo góc không còn chính xác.

Dù vậy, điểm mạnh của gyro là ít bị nhiễu hơn accelemeter, nghĩa là giá trị tức thời của nó đáng tin cậy.

##### 2.1.4.2\ Cảm biến con quay hồi chuyển Gyroscope:

Accel luôn có offset trên mỗi trục làm cho giá trị đo được thường lệch đi so với thực tế một chút. Ngoài ra, giá trị đó được theo accel thường nhạy với rung động cơ khí nhỏ khiến cho giá trị tức thời của nó không đáng tin cậy, do đó chúng ta chỉ sử dụng giá trị trung bình của acc thì nó mới có hữu hiệu, vì nếu để lâu dài thì accel không bị trôi như gyro.

#### 2.1.5\. Các giải thuật tính toán IMU

### 2.2\. Cảm biến Hi229

#### 2.2.1\. Mô tả chung

Hi229 do HiPNUC sản xuất là Hệ thống trong gói (SiP) tích hợp gia tốc kế ba trục, con quay hồi chuyển ba trục, từ kế ba trục và vi điều khiển 32-bit ARM® Cortex ™ -M4 chạy chương trình cơ sở kết hợp cảm biến của HiPNUC. Phần sụn cung cấp các thuật toán xử lý tín hiệu phức tạp để xử lý dữ liệu cảm biến và cung cấp định hướng 3D thời gian thực chính xác, tiêu đề, gia tốc đã hiệu chỉnh và vận tốc góc đã hiệu chỉnh, cũng như dữ liệu cảm biến thô đã được hiệu chỉnh. Hi229 có một số đặc tính chống nhiễu từ trường nhất định trong nhà và vẫn có thể hoạt động bình thường trong môi trường nhiễu từ trường cường độ nhất định.

#### 2.2.2\. Các tính năng chính
#### 2.2.3\. Các tính năng chính của cảm biến tích hợp
Ứng dụng tiêu biểu
Kết nối Hi229

Đặc điểm hoạt động
Độ chính xác góc


### 3.1\. Convert Local - Global:

![image](https://user-images.githubusercontent.com/99313947/178130727-5ea3a0ac-a583-45b6-8d80-46c79b8b7e9d.png)



3.2.1.1.4 Đặc tính của một số loại cảm biến


### 3.1.2\. Cảm biến quán tính Hi229:

### 3.1.3\. Chuyển đổi hệ tạo độ:

### 3.2\. Convert Pytorch - ONNX:

![image](https://user-images.githubusercontent.com/99313947/178130684-6cc7fc80-11de-4426-b7db-3b272c8770e8.png)

Chúng tôi lấy số đo vòng quay và gia tốc của mỗi IMU làm đầu vào tổng thể của hệ thống. Chúng tôi sắp xếp các phép đo này vào cùng một hệ quy chiếu và chuẩn hóa chúng để thu được vectơ đầu vào nối liền là 𝒙 (0) = [Rroot, · · ·, Rrarm, Rroot, · · ·, Rrarm] ∈ R 72 trong đó 𝒂 ∈ R 3 là gia tốc và 𝑹 ∈ R 3 × 3 là ma trận quay. Chúng tôi sử dụng 𝒙 (0) (𝑡) để chỉ các phép đo của khung thứ 𝑡 và chỉ số trên (0) có nghĩa là nó là đầu vào tổng thể. Vui lòng tham khảo Phụ lục A để biết thêm chi tiết về tiền xử lý cảm biến.

