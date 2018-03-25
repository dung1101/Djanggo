# Liệt kê danh sách
Mở views.py
```
from django.shortcuts import render
from .models import Truyen

def home(request):
    content = {'truyen':Truyen.objects.all()}
    return render(request,'truyenCV/home.html',content)
```
Tạo file home.html trong thư mục ./templates/truyenCV/
```
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Home</title>
</head>
<body>
  <h1>Truyện Convert</h1>
    {% for tr in truyen %}
    <a href="./{{tr.id}}">{{tr.tenTruyen}}</a>
    <br />
    {% endfor %}
</body>
</html>
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
