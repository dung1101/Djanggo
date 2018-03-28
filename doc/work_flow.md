Khi client gửi yêu câu url thông qua http đến server, server sẽ so sánh với các url trong urls.py lần lượt. Lúc này sảy ra 2 trường hợp:
* Không có url nào match với yêu cầu của client lúc này server sẽ thông báo lỗi 404
* Có url trùng với yêu cầu thì sẽ gọi đến hàm trong views.py ứng với url đó và trả về client.
