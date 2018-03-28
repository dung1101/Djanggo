# Loại bỏ hard code
Đặt tên cho các url
truyenCV/urls.py
```
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('<int:id>', views.detail, name='detail'),
]
```
truyenCV/home.html
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
{% endblock%}
```
truyenCV/detail.html
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
    <p><a href="{% url 'home' %}">Trang chủ</a></p>
{% endblock%}
```
