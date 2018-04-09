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
* Sử dụng câu lệnh để tạo model tự động `python manage.py inspectdb > [appname]/models.py`
Mặc định ispectdb tạo ra unmanaged models nghĩa là Django không có quyền như là tạo chỉnh sửa với table<br />
Để cho phép django làm điều này cần thay `managed = False` = `managed = True` trong class META của model<br />
Ví dụ
```
class Person(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=70)
    class Meta:
       managed = True
       db_table = 'CENSUS_PERSONS'
```
* `python manage.py migrate [appname]`
