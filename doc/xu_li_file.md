* Tạo trong app một folder `static` trong folder này sẽ chứa các thư viện cho html như css,js,image,audio,...
* import thư viên vào html
ví dụ có file css `/static/css/style.css` 
```
<head>
  {% load static %}
  <link rel="stylesheet" type="text/css" href="{% static 'css/style.css' %}" />
</head>
```
* Tao link download : `/static/download/OnlyOne.mp3` 
`<a href="{% static 'download/OnlyOne.mp3' %}" download="OnlyOne-Boa.MP3">`
