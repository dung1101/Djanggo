# Admin
## Tạo tài khoản admin
Mở shell 
```
python manage.py createsuperuser
```
## Truy cập vào trang admin
```
127.0.0.1:8000/admin
```
nhập user passwd
## Tùy chỉnh trang admin
mở file admin.py
```
from django.contrib import admin
from .models import Truyen

class AdminTruyen(admin.ModelAdmin):
    # hiển thị trên trang admin
    list_display = ['tenTruyen', 'tacGia', 'theLoai', 'ngayDang']
    # bảng lọc
    list_filter = ['ngayDang']
    # thêm thanh tìm kiếm dựa vào tenTruyen
    search_fields = ['tenTruyen']
admin.site.register(Truyen,AdminTruyen)
```
