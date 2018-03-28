# Tạo project
## Các bước tạo project
bật cmd tại folder muốn đặt project
gõ lệnh 
```
django-admin startproject firstSite
```
(firstSite là tên project) 
## Cấu trúc project
```
mysite/
  mysite/
    __init__.py
    settings.py
    urls.py
    wsgi.py
  manage.py
```
* manage.py :command-line utility giúp tương tác với project
* settings.py :cấu hình cho project
* urls.py :danh sách các url 
* wsgi.py :
## Chạy server
```
python manage.py runserver
```
# Tạo web app
```
python manage.py startapp truyenCV
```
myapp là tên app
## install app
mở file settings.py trong folder project 
```
'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'truyenCV'
```
## Cấu trúc app
```
truyenCV/
  migrations/
  __init__.py
  admin.py
  apps.py
  models.py
  tests.py
  views.py
```
