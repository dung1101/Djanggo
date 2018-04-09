* Trong file setting.py thay đổi thông tin db bằng db đã có<br />
Ví dụ
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'GameBall',
        'USER': 'client',
        'PASSWORD': '123',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```
* Sử dụng câu lệnh để tạo model `python manage.py inspectdb > models.py`
