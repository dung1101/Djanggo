# 1.Khách hàng
## 1.1.Đăng nhập:
### Kiểm tra phiên và hạn chế anonymous truy cập vào những trang cần đăng nhập
Khi đăng nhập thành công sẽ tạo một biến cho session để kiểm tra phiên
```
request.session['username'] = username
# username ở đây là username của tài khoản đăng nhập để kiểm tra xem ai đang đăng nhập
# request.session['username'] có thẩy thay bằng request.session['agent'] để phân biệt agent và KH
```
### Kiểm tra phiên đăng nhập : `request.sesstion.has_key('username')` nếu `true` là có , `false` là không
## 1.2.Đăng ký tài khoản
### Kích hoạt tài khoản bằng mail
## 1.3.Tạo ticket
### Tạo commbobox form : 
```
topic = forms.ChoiceField(choices=[(x.id,x.name) for x in Topics.objects.all()])
# thuộc tính choices là một list mà mỗi phần tử là 1 tuple chứa 2 giá trị 
# giá trị đầu tiên của tuple là clean_data mà ta sẽ lấy được khi gửi form
```
### Đính kèm file 
Tạo trường đính kèm trong form
```
attach = forms.FileField(required=False, widget=forms.FileInput(attrs={
        'class': 'form-control',
        'placeholder': 'attach',
        'id': 'i_file',
    })
    )
# required = False : khi kiểm tra form.is_valid thì nếu ta bỏ trống file đính kèm vẫn hợp lệ
```
Xử lý trong html
Trong thẻ <form> thêm thuộc tính `enctype="multipart/form-data"`
Truyền giá trị vào form ngoài `request.POST` còn có thêm `request.FILES`
Giới hạn kích thước file ở client
Giới hạn kích thước file ở server
sử dụng `request.FILES['attach']._size` để lấy kích thước của file tính bằng bit
Lưu file lên server 
```
# cấu hình file settings.py 
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
# hàm để lưu file
def handle_uploaded_file(f):
    path = "media/photos/"+f.name
    file = open(path, 'wb+')
    for chunk in f.chunks():
        file.write(chunk)
    file.close()
```
### close ticket
xử lý trong html
```
#tạo button để close ticket
<form >
  <button id="close_{{forloop.counter}}" type="button">close</button>
</form>
# script để xử lý sự kiện click buton
<script type="text/javascript">
  var btn = document.getElementById("close_{{forloop.counter}}");
  btn.onclick = function(){
  if(confirm("Are you sure ?")){
    # sử dụng button như thẻ <a> bắt buộc phải đặt <button> trong <form>
    location.href="{% url 'user:close_ticket' tk.id %}"
  }
  };
</script>
```
xử lý trong views.py
```
def close_ticket(request,id):
    if request.session.has_key('username'):
        ticket = Tickets.objects.get(id=id)
        ticket.status = 3
        ticket.save()
        return redirect("/user")
    else:
        return redirect("/")
```






