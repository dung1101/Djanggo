# Thao tác trên database thông qua API
## Tạo bảng
Trong app tên là myapp mở file models.py và tạo class với mỗi class là 1 bảng trong csdl , mỗi thuộc tính là một cột
Ví dụ 
```
from django.db import models

# Create your models here.
class Truyen(models.Model):
    tenTruyen = models.CharField(max_length=50)
    theLoai = models.CharField(max_length=50)
    tacGia = models.CharField(max_length=50)
    ngayDang = models.DateTimeField(auto_now_add=True)
    noiDung = models.TextField(null=False)
    def __str__(self):
        return self.tenTruyen
```
Tạo bảng có 6 fields trong đó 5 fields là các biến của lớp như trên và 1 field là id (pk , auto_increment)
## Tạo migration
migration : file lưu các thay đổi về model
mở terminal và gõ `python manage.py makemigrations truyenCV`
Nếu thành công sẽ tạo một bản migration nằm trong thư mục truyenCV/migrations
## Đồng bộ với csdl
```
python manage.py migrate
```
Sau khi thành công thì trên cơ sở dũ liệu sẽ tạo bảng tương ứng với class như bên trên
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
