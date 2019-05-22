#### khi thay đổi hình ảnh trong temple thì phải xóa cache của trình duyệt

#### lý do tại sao phải sử dụng webserver(apache, nginx):
`python manage.py runserver` sử dụng django built-in server, server này được xây dựng để sử dụng trên local dev không sử dụng trên môi trường product. Nó không thể xử lý một lượng lớn lưu lượng truy câp.

#### Web Server Gateway Inteface(WSGI) là gì
Một webserver truyền thống không thể hiểu hay có bất kỳ cách nào để chạy ứng dụng Python. Vì vậy WSGI ra đời để giải quyết vấn đề này. 
Nó sẽ đứng giữa webserver và app làm nhiệm vụ cầu nối. 

#### Custom django command
[https://simpleisbetterthancomplex.com/tutorial/2018/08/27/how-to-create-custom-django-management-commands.html](https://simpleisbetterthancomplex.com/tutorial/2018/08/27/how-to-create-custom-django-management-commands.html)

#### Admin page
[Action](https://docs.djangoproject.com/en/2.2/ref/contrib/admin/actions/)

[Admin](https://docs.djangoproject.com/en/2.2/ref/contrib/admin/)

[Reversing URL](https://docs.djangoproject.com/en/2.2/ref/contrib/admin/#reversing-admin-urls)

[Datetime Format](https://docs.djangoproject.com/en/2.2/ref/settings/#datetime-input-formats)
