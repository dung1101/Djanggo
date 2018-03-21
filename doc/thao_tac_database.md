# Thao tác trên database thông qua QuerySet API
## Tạo bảng
Trong app tên là myapp mở file models.py và tạo class với mỗi class là 1 bảng trong csdl , mỗi thuộc tính là một cột
Ví dụ 
```
from django.db import models

class Reporter(models.Model):
    full_name = models.CharField(max_length=70)
    def __str__(self):
      return self.full_name

class Article(models.Model):
    pub_date = models.DateField()
    headline = models.CharField(max_length=200)
    content = models.TextField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)
    def __str__(self):
      return self.headline

```
Tạo 2 bảng:
* Bảng 1 : có 1 cột là full_name kiểu Char và tối đa là 70 ký tự, còn 1 cột là id thì tự tạo và đó là pk
* Bảng 2 : có 4 cột và 1 cột id(pk), reporter là khóa phụ của bảng liên kết với bảng 1 
## Tạo migration
migration : chuyển đổi các câu lệnh sql tương ứng để tạo bảng
mở terminal và gõ
```
python manage.py makemigration myapp
```
Nếu thành công sẽ tạo một bản migration nằm trong thư mục myapp/migrations
Ta có thể xem file này để xem câu lệnh sql đã chuyển đổi
## Đồng bộ với csdl
```
python manage.py migrate
```
Sau khi thành công thì trên cơ sở dũ liệu sẽ tạo 2 bảng tương ứng với 2 class như bên trên
## Làm việc với cơ sở dữ liệu thông qua python API
### Mở shell
```
python manage.py shell
```
### Thêm các đối tượng cho bảng
```
>>>from myapp.models import Reporter
#cách 1
>>>r = Reporter(full_name='Sinionth')
>>>r.save()
#cách 2
>>>r =Reporter.objects.create(full_name='Sinionth')
```
### show các đối tượng
```
#show tất cả các đối tượng
>>>Reporter.objects.all()

#show đối tượng theo ý muốn
>>>Reporter.objects.filter(full_name__startswith="si")
>>>Reporter.objects.filter(full_name__contains="ni")
>>>Reporter.objects.filter(id=10)
```
## Lấy đối tượng (chỉ 1)
```
#lấy đối tượng
>>>r=Reporter.objects.get(full_name__startswith="si")
>>>r=Reporter.objects.get(full_name__contains="ni")
>>>r=Reporter.objects.get(fullname='sini')
#nếu đối tượng không tồn tại thì tạo
>>>r.objects.get_or_create(full_name="sinionth")
```
#xóa đối tượng 
```
>>>r.delete()
```
Tài liệu tham khảo
https://docs.djangoproject.com/en/2.0/ref/models/querysets/#django.db.models.query.QuerySet.create
