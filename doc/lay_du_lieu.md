# 1.Tạo trang chủ liệt kê danh sách truyện
* Mở truyenCVviews.py
```
from django.shortcuts import render
from .models import Truyen

def home(request):
    content = {'truyen':Truyen.objects.all()}
    return render(request,'truyenCV/home.html',content)
```
* Trong thư mục `./templates/truyenCV/`
Tạo file base.html
```
<!DOCTYPE html>
<html lang="en">
<head>
    <title>{% block title %}{% endblock%}</title>
</head>
<body>
{% block header %}{% endblock%}
{% block body %}{% endblock%}
</body>
</html>
```
Tạo file home.html 
```
{% extends "truyenCV/base.html" %}
{% block title %}Trang chủ{% endblock%}
{% block header %}
    <h1>Truyện Convert</h1>
{% endblock%}
{% block body %}
    <ol>
    {% for tr in truyen %}
        <li><a href="/truyenCV/detail/{{tr.id}}">{{tr.tenTruyen}}</a></li>
    {% endfor %}
    </ol>
{% endblock%}
```
* Thêm đường dẫn trong file truyenCV/urls.py
```
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    ]
```
# 2.Hiển thị chi tiết bài viết
* Mở views.py
```
from django.shortcuts import render
from .models import Truyen

def home(request):
  ...
def detail(request, id):
    content = {'truyen':Truyen.objects.get(id=id)}
    return render(request,'truyenCV/detail.html',content)
```
* Tạo file detail.html trong thư mục `./templates/truyenCV/`
```
{% extends "truyenCV/base.html" %}
{% block title %}{{ truyen.tenTruyen }}{% endblock%}
{% block header %}
    <h1>{{ truyen.tenTruyen }}</h1>
    <h2>Tác giả: {{ truyen.tacGia }}</h2>
    <h2>Thể loại: {{ truyen.theLoai }}</h2>
    <h4>Ngày đăng: {{truyen.ngayDang}}</h4>
{% endblock%}
{% block body %}
    <p>{{ truyen.noiDung }}</p>
    <p><a href="/truyenCV">Trang chủ</a></p>
{% endblock%}
```
* Thêm url 
```
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:id>', views.detail, name='detail'),
]
```
