* Kiểm tra phiên đăng nhập : `request.sesstion.has_key('username')` nếu `true` là có , `false` là không
* Tạo commbobox form : 
```
topic = forms.ChoiceField(choices=[(x.id,x.name) for x in Topics.objects.all()])
# thuộc tính choices là một list mà mỗi phần tử là 1 tuple chứa 2 giá trị
# giá trị đầu tiên của tuple là clean_data
```
* Tạo file upload
```

```
