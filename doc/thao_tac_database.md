# Thao tác trên database thông qua API
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
Mở shell
```
python manage.py shell
```
|Hàm|Mô tả|Ví dụ|
|---|-----|-----|
|filter()|trả về các phần tử phù hợp với đk|Reporter.objects.filter(full_name__startswith="si")|
|||Reporter.objects.filter(full_name__contains="ni")|
|exclude()|trả về các phần tử không phù hợp với đk|Reporter.objects.exclude(full_name__startswith="si")|
|||Reporter.objects.exclude(full_name__contains="ni")|
|||Reporter.objects.exclude(id=10)|
|order_by()|sắp xếp|Reporter.objects.filter(full_name__contains="ni").order_by('id')|
|reverse()|đảo|Reporter.objects.filter(full_name__contains="ni").order_by('id').reverse()|
|distinct()|lại bỏ dupplicate|Reporter.objects.filter(full_name__contains="ni").order_by('id').distinct('full_name')|
|all()|trả về tất cả các đối tượng|Reporter.objects.all()|
|create()|thêm đối tượng|Reporter.objects.create(full_name='Sinionth')|
|save()|lưu đối tượng|r = Reporter(full_name='Sinionth')|
|||r.save()|
|get()|lấy đối tượng|r=Reporter.objects.get(full_name__startswith="si")|
|get_or_create()|nếu đối tượng ko tồn tại thì tạo|r.objects.get_or_create(full_name="sinionth")|
|delete()|xóa đối tượng|r.delete()|

Tài liệu tham khảo
https://docs.djangoproject.com/en/2.0/ref/models/querysets/#django.db.models.query.QuerySet.create
https://docs.djangoproject.com/en/2.0/topics/db/queries/
