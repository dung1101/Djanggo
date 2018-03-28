# Liệt kê danh sách
Mở views.py
```
from django.shortcuts import render
from .models import Truyen

def home(request):
    content = {'truyen':Truyen.objects.all()}
    return render(request,'truyenCV/home.html',content)
```
Trong thư mục `./templates/truyenCV/`
* Tạo file base.html
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
* Tạo file home.html 
```
{% extends "truyenCV/base.html" %}
{% block title %}Trang chủ{% endblock%}
{% block header %}
    <h1>Truyện Convert</h1>
{% endblock%}
{% block body %}
    <ol>
    {% for tr in truyen %}
        <li><a href="{% url 'detail' tr.id %}">{{tr.tenTruyen}}</a></li>
    {% endfor %}
    </ol>
    <a href="{% url 'register' %}">Đăng ký tài khoản</a>
    <a href="{% url 'upload' %}">Đăng truyện</a>
{% endblock%}
```

# Hiển thị bài viết
Mở views.py
```
from django.shortcuts import render
from .models import Truyen

def home(request):
  ...
def truyen(requst,id):
    content = {'truyen':Truyen.objects.get(id=id)}
    return render(requst,'truyenCV/baseTruyen.html',content)
```
Tạo file baseTruyen.html trong thư mục ./templates/truyenCV/
```
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{{ truyen.tenTruyen }}</title>
</head>
<body>
  <h1>{{ truyen.tenTruyen }}</h1>
  <h2>Tác giả: {{ truyen.tacGia }}</h2>
  <h2>Thể loại: {{ truyen.theLoai }}</h2>
  <h4>Ngày đăng: {{truyen.ngayDang}}</h4>
  <p>{{ truyen.noiDung }}</p>
</body>
</html>
```
