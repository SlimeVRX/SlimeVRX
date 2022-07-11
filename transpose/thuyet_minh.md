# Key
- vision - thị giác máy tính
- occlusion - tắc nghẽn
- SOTA - State-of-the-art
- Abstract - Tóm tắt
- FPS - Frame per second

# Ước tính cơ thể người từ 6 cảm biến quán tính chi phí thấp trong thời gian thực

## Abstract: Tóm tắt

Khả năng ghi lại chuyển động của con người từ các cảm biến quán tính đã cho thấy tiềm năng lớn so với các phương pháp tiếp cận dựa trên thị giác máy tính vì không gặp phải hạn chế về không gian hoạt động và tắc nghẽn do các bộ phận cơ thể bị che khuất. Các nghiên cứu SOTA gần đây sử dụng cảm biến quán tính chuyên dụng của Xsens và Noitom có giá thành rất cao đồng thời yêu cầu máy tính sử dụng GPU dẫn đến việc triển khai trở nên tốn kém và khó phổ biến. Việc ghi lại chuyển động thời gian thực sử dụng cảm biến quán tính chi phí thấp và triển khai trên máy tính cấu hình thấp chỉ sử dụng CPU là một thách thức. Để đạt được mục đích này, chúng tôi trình bày tái tạo kết quả của bài báo Transpose sử dụng 6 cảm biến quán tính Hi229 chi phí thấp và tối ưu hóa mạng Neural Network đạt tốc độ 24 khung hình / giây trên CPU i5-5200U trong thời gian thực. Các thí nghiệm chứng minh rằng các cảm biến quán tính chi phí thấp có thể được sử dụng để ghi lại chuyển động với độ chính xác và ổn định theo thời gian.

Keywords: IMU, Pose Estimation, Inverse Kinematics, Real-time, Low-cost

## 1\. Introduction: Giới thiệu

### 1.1\. Background: Khái quát

Chụp chuyển động của con người (Mocap) nhằm mục đích tái tạo lại các chuyển động cơ thể con người 3D, đóng một vai trò quan trọng trong các ứng dụng khác nhau như chơi Game, thể thao, Y học, VR/AR và sản xuất phim. Cho đến nay, các giải pháp Mocap dựa trên thị giác máy tính chiếm phần lớn trong chủ đề này. Một trong những cách tiếp cận là dựa trên điểm đánh dấu, các điểm đánh dấu quang học được gắn trên cơ thể người và sử dụng nhiều máy ảnh để theo dõi các điểm đánh dấu để ghi lại chuyển động. Ví dự như hệ thống [Vicon](https://www.vicon.com/) được áp dụng rộng rãi và được xem xét là đủ chính xác cho việc sử dụng trong công nghiệp. Tuy nhiên, cách tiếp cận này yêu cầu cơ sở hạ tầng đắt tiền, điều này khiến chúng không được sử dụng ở cấp độ người tiêu dùng. Gần đây, một số cách tiếp cận khác sử dụng một vài máy ảnh RGB hoặc RGB-D [Chen et al. 2020];[Habibie et al. 2019];[Mehtaet al. 2020];[Tome et al. 2018];[Trumble et al. 2016];[Xiang et al. 2019]. So với cách tiếp cận sử dụng điểm đánh dấu, các cách tiếp cận này yêu cầu cơ sở hạ tần thấp hơn nhiều. Vì các đặc điểm của con người được trích xuất từ hình ảnh, do đó các phương pháp này thường hoạt động kém hiệu quả đối với môi trường ánh sáng khó khăn. Hơn nữa, tất cả các phương pháp tiếp cận dựa trên thị giác máy tính đều bị tắc nghẽn do các bộ phận cơ thể bị che khuất. Vấn đề này có thể được giải quyết bằng cách tăng số lượng camera. Điều này càng làm cho hệ thống trở nên nặng nề và tốn kém. Nhưng nó thường không thực tế trong một số ứng dụng. Ví dụ, rất khó bố trí máy ảnh trong một phòng sinh hoạt có nhiều đồ đạc, vật dụng, những đồ vật này có thể làm chủ thể bị che khuất từ bất kỳ hướng nào. Một hạn chế khác của phương pháp tiếp cận dựa trên tầm nhìn là bị hạn chế trong một không gian cố định. Đối với các hoạt động hàng ngày như đi bộ hoặc chạy trong phạm vi lớn, cần phải có camera chuyển động để ghi lại đủ thông tin, điều này rất khó đạt được [Xu et al. 2016]. Những nhược điểm này là những thiếu sót nghiêm trọng đối với nhiều ứng dụng, dẫn đến các hạn chế khi sử dụng giải pháp dựa trên thị giác máy tính.

Trái ngược với các hệ thống dựa trên thị giác, việc ghi lại chuyển động bằng cảm biến quán tính không gặp phải hạn chế về không gian hoạt động và tắc nghẽn do các bộ phận cơ thể bị che khuất. Nó cũng không yêu cầu thiết lập cơ sở hạ tầng phức tạp. Các đặc điểm này làm cho nó phù hợp hơn với các mục đích sử dụng ở cấp độ người tiêu dùng. Do đó, ghi lại chuyển động bằng cảm biến quán tính ngày càng được chú trọng hơn trong những năm gần đây. Hầu hết các nghiên cứu liên quan đều sử dụng Đơn vị đo lường quán tính (IMU) để ghi lại quán tính chuyển động, nó tiết kiệm, nhẹ, đáng tin cậy và thường được sử dụng trong một số lượng lớn các thiết bị đeo như đồng hồ, dây đeo tay và kính. Hệ thống Mocap quán tính thương mại [Xsens](https://www.xsens.com/) sử dụng 17 IMU để ước tính chuyển động quay của khớp. Mặc dù chính xác, sử dụng nhiều IMU gây bất tiện và ngăn cản người sử dụng di chuyển tự do. Mặt khác, các yêu cầu về cơ sở vật chất đối với một hệ thống như vậy vẫn nằm ngoài khả năng chấp nhận của người tiêu dùng bình thường. Nghiên cứu của SIP [Marcard et al 2017] chứng minh rằng việc tái tạo lại chuyển động của con người chỉ từ 6 IMU là hoàn toàn khả thi. Tuy nhiên, là một phương pháp dựa trên tối ưu hóa, nó cần phải truy cập vào toàn bộ chuỗi và mất nhiều thời gian để xử lý. Nghiên cứu SOTA gần đây, DIP [Huang et al 2018] cũng sử dụng 6 IMU đạt được hiệu suất thời gian thực với chất lượng tốt hơn bằng cách sử dụng biRNN. Tuy nhiên, nó vẫn không thành công ở các tư thế khó và tốc độ 30 khung hình / giây không đủ để chụp các chuyển động nhanh, rất phổ biến trong các ứng dụng thực tế. Quan trọng hơn, nó chỉ ước tính tư thế cơ thể mà không có ước tính chuyển động trong không gian 3D, vốn quan trọng trong nhiều ứng dụng như VR và AR. TransPose [Yi et al 2021] đã giải quyết vấn đề này và đạt được tiến bộ đầu tiên ước lượng dịch chuyển trong không gian 3D và ước tính tư thế cơ thể trong thời gian thực trong khi cũng chỉ sử dụng 6 IMU. Vì bản thân IMU không có khả năng đo khoảng cách trực tiếp. Một số công trình trước đây [Liu et al 2011]; [Vlasic et al 2007] sử dụng các cảm biến siêu âm bổ sung để tính toán chuyển động trong không gian 3D, chi phí cao và có thể bị tắc nghẽn. Các giải pháp khả thi khác sử dụng định vị GPS, cách này không đủ chính xác và chỉ hoạt động khi ghi chuyển động ngoài trời.

### 1.2\. Motivation: Động lực

Các nghiên cứu SOTA gần đây sử dụng cảm biến quán tính chuyên dụng của Xsens và Noitom có giá thành rất cao đồng thời yêu cầu máy tính sử dụng GPU dẫn đến việc triển khai trở nên tốn kém và khó phổ biến. Không có một cách tiếp cận nào sử dụng cảm biến quán tính chi phí thấp. Việc ghi lại chuyển động thời gian thực sử dụng cảm biến quán tính chi phí thấp và triển khai trên máy tính cấu hình thấp chỉ sử dụng CPU là một thách thức. Vì vậy, chúng tôi giới thiệu cách tiếp cận của mình, tái tạo kết quả của bài báo TransPose, ước tính vị trí trong không gian 3D và tư thế cơ thể từ 6 IMU Hi229 chi phí thấp với CPU i5-5200U ở tốc độ 24 khung hình / giây thời gian thực.

### 1.3\. Objectives and Contributions:  Mục tiêu và đóng góp

Mục tiêu của nghiên cứu này tập trung vào việc triển khai lại kết quả bài báo Transpose sử dụng cảm biến quán tính chi phí thấp và chạy trên máy tính cấu hình thấp chỉ sử dụng CPU không cần GPU.

Trong luận án này chúng tôi có 2 đóng góp:
- Chuyển đổi hệ tọa độ cảm biến IMU, Transpose paper sử dụng cảm biến chuyên dụng của Noitom. Chúng tôi sử dụng cảm biến Hi229 chi phí thấp nên phải viết lại chuyển đổi hệ tọa độ để phù hợp với đầu vào Transpose model. Mở rộng, chúng tôi có thể thử nghiệm với bất kỳ IMU.
- Chuyển đổi model từ framework Pytorch sang ONNX tối ưu cho việc triển khai. Chúng tôi đã giảm yêu cầu phần cứng để triển khai từ cấu hình máy tính có GPU RTX 2080 sang cấu hình máy tính chỉ cần CPU i5-5200U Laptop đạt 24 khung hình / giây trong thời gian thực.

### 1.4\. Organization: Cấu trúc thuyết minh

Bài viết này được cấu trúc như sau. Chương 2 giới thiệu các nghiên cứu tài liệu liên quan đến luận án. Chương 3 trình bày chi tiết các chiến lược của chúng tôi, bao gồm kiến trúc mô phỏng tùy chỉnh và phương pháp giảng dạy. Chương 4 trình bày việc thực hiện thiết kế và các thí nghiệm. Chương 5 kết thúc luận án và đề xuất nghiên cứu trong tương lai.

Bài viết này được cấu trúc như sau. Chương 2 giới thiệu các nghiên cứu tài liệu liên quan đến luận án. Chương 3 ... Chương 4 ...

## 2\. Related work: Các nghiên cứu liên quan:

Chụp chuyển động của con người (mocap) đã có lịch sử nghiên cứu lâu đời. Nhiều nghiên cứu đã được dành cho chủ đề này, chủ yếu có thể được phân loại thành các phương pháp tiếp cận quang học, quán tính và lai. Vì phương pháp của chúng tôi chỉ yêu cầu các phép đo IMU làm đầu vào, nên chúng tôi không thảo luận về các phương pháp tiếp cận dựa trên hình ảnh thuần túy [15, 16, 24, 27, 40, 48, 58]. Ở đây, chúng tôi tập trung vào các giải pháp mocap lai và quán tính.

### 2.1\. Optical-inertial Hybrid Motion Capture: Chụp chuyển động kết hợp cảm biến quán tính và thị giác máy tính 

Khi các giải pháp mocap dựa trên hình ảnh bị hiện tượng tắc nghẽn, việc kết hợp hình ảnh với IMU, nhằm mục đích đạt được khả năng theo dõi chuyển động mạnh mẽ hơn, gần đây đã thu hút nhiều sự chú ý. Điều này có thể đạt được bằng cách tối ưu hóa dựa trên [22, 36–38,43,65], tối ưu hóa tư thế người để phù hợp với cả các đặc điểm hình ảnh và phép đo quán tính hoặc ước tính dựa trên tính năng [13, 62] trong đó hồi quy tư thế của con người từ các tính năng kết hợp có nguồn gốc từ hình ảnh và IMU. Zhang và cộng sự. [87] đề xuất khai thác IMU trong ước tính tư thế 2D bằng cách kết hợp các đặc điểm hình ảnh của từng cặp khớp được liên kết bởi IMU. Một số hoạt động kết hợp IMU với hình ảnh độ sâu [18, 23, 90] hoặc điểm đánh dấu quang học 1 để thực hiện chụp chuyển động / hiệu suất của con người. Tuy nhiên, các phương pháp này vẫn còn hạn chế đáng kể trong điều kiện ánh sáng yếu và tắc nghẽn, đồng thời yêu cầu phải di chuyển trong tầm nhìn của máy ảnh. Phương pháp của chúng tôi không yêu cầu đầu vào hình ảnh và do đó không có những hạn chế này.

### 2.2\. Motion Capture from Inertial Sensors: Chụp chuyển động từ cảm biến quán tín. 

Phương pháp tiếp cận mocap quán tính không bị tắc nghẽn hoặc hạn chế không gian di chuyển. Các giải pháp thương mại [34, 71] và nghiên cứu mở rộng [14] dựa vào 17 IMU để thực hiện chụp chuyển động. Họ thường yêu cầu mặc một bộ đồ bó sát với các IMU dày đặc, điều này gây bất tiện và cản trở. Rõ ràng là nên có một bộ IMU giảm bớt trên cơ thể. Tuy nhiên, việc chụp chuyển động từ các cảm biến quán tính thưa thớt là rất mơ hồ và khó khăn. Một số nghiên cứu [31, 59, 64] sử dụng cảm biến siêu âm để có thêm thông tin vị trí nhằm giải quyết một số điểm mơ hồ, nhưng việc sử dụng cảm biến khoảng cách sẽ hạn chế phạm vi hoạt động. Các kết quả đầu tiên thuần túy quán tính [47, 57, 60]  sử dụng gia tốc kế thưa thớt để tái tạo lại tư thế của con người bằng cách tìm kiếm cơ sở dữ liệu. Schwarz và cộng sự. [50] sử dụng các phép đo định hướng thưa thớt để thực hiện ước tính tư thế dành riêng cho từng người. Để cải thiện độ chính xác, các nghiên cứu gần đây [12, 20, 44, 66, 73] sử dụng cả phép đo gia tốc và định hướng. Marcard và cộng sự. [66] trình bày một phương pháp ngoại tuyến để chụp chuyển động của con người chỉ từ 6 IMU, đạt được độ chính xác đầy hứa hẹn. Huang và cộng sự. [20] đề xuất phương pháp học sâu đầu tiên, sử dụng mạng nơ-ron lặp lại hai chiều (biRNN) để ước tính tư thế con người từ 6 IMU trong thời gian thực. Tuy nhiên, phương pháp của họ không cho phép xác định vị trí của người đó trong không gian 3D. Phương pháp hiện đại nhất, TransPose [73], giới thiệu khung ước lượng dịch và tư thế thời gian thực đầu tiên, giúp đạt được chất lượng chụp chính xác trong khi cũng chỉ sử dụng 6 IMU.

Tuy nhiên, tất cả các tác phẩm này đều có độ trễ không đáng kể do nhu cầu thông tin trong tương lai vốn có, không thể chụp ổn định các tư thế mơ hồ và có nhiều hiện vật phi vật lý như rung và trượt chân. Ngược lại, phương pháp của chúng tôi không dựa vào bất kỳ thông tin nào trong tương lai và không bị chậm trễ trong khi thậm chí đạt được độ chính xác cao hơn. Ngoài ra, chúng tôi là người đầu tiên kết hợp tối ưu hóa chuyển động dựa trên vật lý với chụp chuyển động quán tính thưa thớt và chúng tôi cho thấy rằng một thiết kế được tổ chức cẩn thận như vậy sẽ cải thiện đáng kể độ chính xác vật lý của chuyển động.

## 3\. Method: Phương pháp

Nhiệm vụ của chúng tôi là ước tính các tư thế và bản dịch của chủ đề trong thời gian thực bằng cách sử dụng 6 IMU. Như được hiển thị trong Hình 3, 6 IMU được gắn trên xương chậu, chân dưới bên trái và bên phải, cẳng tay trái và phải và đầu. Sau đây, chúng tôi đề cập đến các khớp nối này ngoại trừ xương chậu, được đặt tên là khớp gốc. Chúng tôi chia nhiệm vụ này thành hai nhiệm vụ: Chuyển đổi hệ tọa độ từ hệ tọa độ local của từng cảm biến thành hệ tọa độ global liên hệ tất cả các cảm biến (Phần 3.2) và chuyển đổi framework neuralnetwork nghiên cứu Python sang framework ONNX chuyên cho việc tối ưu cho triển khai (Phần 3.3).

![image](https://user-images.githubusercontent.com/99313947/178130401-fe8f0574-9933-4405-8f33-716dbce70e4a.png)
Hình 3. Vị trí IMU. 6 IMU được gắn trên cẳng tay trái và phải, cẳng chân trái và phải, đầu và xương chậu. Chúng tôi yêu cầu các cảm biến được kết dính chặt chẽ xung quanh các khớp với các hướng tùy ý.

### 3.1\. System Input: Đầu vào hệ thống

Chúng tôi lấy số đo vòng quay và gia tốc của mỗi IMU làm đầu vào tổng thể của hệ thống. Chúng tôi sắp xếp các phép đo này vào cùng một hệ quy chiếu và chuẩn hóa chúng để thu được vectơ đầu vào nối liền là 𝒙 (0) = [Rroot, · · ·, Rrarm, Rroot, · · ·, Rrarm] ∈ R 72 trong đó 𝒂 ∈ R 3 là gia tốc và 𝑹 ∈ R 3 × 3 là ma trận quay. Chúng tôi sử dụng 𝒙 (0) (𝑡) để chỉ các phép đo của khung thứ 𝑡 và chỉ số trên (0) có nghĩa là nó là đầu vào tổng thể. Vui lòng tham khảo Phụ lục A để biết thêm chi tiết về tiền xử lý cảm biến.

### 3.2\. Convert Local - Global:

![image](https://user-images.githubusercontent.com/99313947/178130727-5ea3a0ac-a583-45b6-8d80-46c79b8b7e9d.png)

### 3.3\. Convert Pytorch - ONNX:

![image](https://user-images.githubusercontent.com/99313947/178130684-6cc7fc80-11de-4426-b7db-3b272c8770e8.png)



