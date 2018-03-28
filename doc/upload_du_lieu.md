# Tạo trang upload để tải truyện 
* trong truyenCV tạo file form.py
```
from django import forms
from .models import Truyen

class UploadForm(forms.Form):
    tenTruyen = forms.CharField(label='Tên truyện')
    tacGia = forms.CharField(label='Tác giả')
    theLoai = forms.CharField(label='Thể loại')
    noiDung = forms.CharField(label='Nội dung',widget=forms.Textarea)

    def save(self):
        Truyen.objects.create(tenTruyen=self.cleaned_data['tenTruyen'],tacGia=self.cleaned_data['tacGia'],
                                  theLoai=self.cleaned_data['theLoai'],noiDung=self.cleaned_data['noiDung'])
```
* mở truyenCV/views.py thêm hàm
```
def upload(request):
    if request.method == 'POST':
        form = UploadForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'truyenCV/success.html')
    form = UploadForm()
    return render(request, 'truyenCV/upload.html', {'form': form})
```
* tạo file upload.html trong templates/truyenCV/
```
{% extends "truyenCV/base.html" %}
{% block title %}Đăng truyện{% endblock%}
{% block body %}
    <form action="{% url 'upload' %}" method="POST">
        {% csrf_token %}
        {{form.as_p}}
        <input type="submit" value="Upload"/>
    </form>
    <br>
    <a href="{% url 'home'%}">Quay lại trang chủ</a>
{% endblock%}
```
* thêm url trong urls.py
```
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:id>', views.detail, name='detail'),
    path('upload', views.upload, name='upload'),
]
```
