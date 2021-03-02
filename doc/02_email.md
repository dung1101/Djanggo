# email
update 02/03/2021 django ver 3.1

Bước 1: Tạo mật khẩu ứng dụng cho tài khoản Gmail
1. Đầu tiên, bạn cần truy cập vào link: https://myaccount.google.com/ sau đó đăng nhập tài khoản Gmail của bạn.
1. Vào mục Bảo Mật và bật xác minh 2 bước ( nếu trạng thái này đang tắt ).
1. Ngay sau đó, ta thực hiện lấy Mật khẩu ứng dụng.
1. Nhấn vào ô chọn ứng dụng.
1. Chọn tùy chọn “Khác ( Tên tùy chỉnh )“
1. Đặt tên bất kỳ, ví dụ: ở đây là Gửi Mail SMTP.
1. Cuối cùng chúng ta bấm nút “Tạo“. Mật khẩu ứng dụng sẽ được hiển thị, bạn chỉ cần lưu lại mật khẩu này để sử dụng cấu hình SMTP trên website.

Bước 2: Config django settings
```
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'youruser'
EMAIL_HOST_PASSWORD = 'yourappilicationpassword'
EMAIL_USE_TLS = True
```

Bước 3: Gửi mail
```
from django.core.mail import send_mail

send_mail('subject', 'body', 'youruser@gmail.com', [receiver1@gmail.com, receiver2@gmail.com, ])
```
