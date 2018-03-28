# tạo trang đăng ký tài khoản
* thêm vào forms.py
```
...
import re
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import Use

class UploadForm(forms.Form):
....

class RegistrationForm(forms.Form):
    username = forms.CharField(label='Username', max_length=16)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Re-type Password', widget=forms.PasswordInput)

    def clean_password2(self):
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1 == password2 and password1:
                return password2
        raise forms.ValidationError("Mat khau khong hop le")
    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.search(r'^\w+$', username):
            raise forms.ValidationError("username chua ky tu dac biet")
        try:
            User.objects.get(username=username)
        except ObjectDoesNotExist:
            return username
        raise forms.ValidationError("username da ton tai")

    def save(self):
        User.objects.create_user(username=self.cleaned_data['username'],password=self.cleaned_data['password1'])

```
* thêm vào views.py
```
def register(request):
    if request.method =='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'truyenCV/success.html')
    form = RegistrationForm()
    return render(request,'truyenCV/register.html',{'form': form})
```
* Tạo register.html
```
{% extends "truyenCV/base.html" %}
{% block title %}Đăng ký tài khoản{% endblock%}
{% block body %}
    <center>
        <form action="{% url 'register' %}" method="POST">
            {% csrf_token %}
            {{form.as_p}}
            <input type="submit" value="Register"/>
        </form>
        <br>
        <a href="{% url 'home'%}">Quay lại trang chủ</a>
    </center>
{% endblock%}
```
* thêm vào urls.py<br>
`path('register', views.register, name='register'),`
