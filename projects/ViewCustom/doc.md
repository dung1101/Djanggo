# View
<a href='https://docs.djangoproject.com/en/2.1/topics/http/' target='_blank'>Chi tiết xem tại đây</a>

## 1) URL
Django xử lý request ntn ?
- Xác định root URLconf module được khai báo ở setting: `ROOT_URLCONF = 'ViewCustom.urls'`. 
- Django load module và tìm kiếm biến `urlpatterms`
- Tìm từng url và dừng lại khi gặp url đầu tiên trùng với request url 
- Khi url trùng thì sẽ gọi đến view ứng với url đó
- Nếu không có url nào trùng hoặc trong quá trình xảy ra lỗi Django sẽ trả về thông tin lỗi 

### 1.1) Path converters
```
from django.urls import path

from . import views

urlpatterns = [
    path('articles/2003/', views.special_case_2003),
    path('articles/<int:year>/', views.year_archive),
    path('articles/<int:year>/<int:month>/', views.month_archive),
    path('articles/<int:year>/<int:month>/<slug:slug>/', views.article_detail),
]
```
- `str`: trùng với bất kỳ non_string nào ngoại trừ `/` 
- `int`: trùng với số >= 0
- `slug`: Matches any slug string consisting of ASCII letters or numbers, plus the hyphen and underscore characters. 
For example, building-your-1st-django-site.
- `uuid`: Matches a formatted UUID. To prevent multiple URLs from mapping to the same page, dashes must be included and
 letters must be lowercase. For example, 075194d3-6885-417e-a8a8-6c931e272f00. Returns a UUID instance.
- `path`: Matches any non-empty string, including the path separator, '/'. This allows you to match against 
a complete URL path rather than just a segment of a URL path as with str.

### 1.2) Registering custom path converters
```
class FourDigitYearConverter:
    regex = '[0-9]{4}'
    
    # handles converting the matched string into the type that should be passed to the view function
    def to_python(self, value):
        return int(value)
    
    #  handles converting the Python type into a string to be used in the URL
    def to_url(self, value):
        return '%04d' % value
```
```
from django.urls import path, register_converter

from . import converters, views

register_converter(converters.FourDigitYearConverter, 'yyyy')

urlpatterns = [
    path('articles/2003/', views.special_case_2003),
    path('articles/<yyyy:year>/', views.year_archive),
    ...
]
```

### 1.3) Using regular expressions
```
from django.urls import path, re_path

from . import views

urlpatterns = [
    path('articles/2003/', views.special_case_2003),
    re_path(r'^articles/(?P<year>[0-9]{4})/$', views.year_archive),
    re_path(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', views.month_archive),
    re_path(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<slug>[\w-]+)/$', views.article_detail),
]
```

### 1.4) Error handling
Khi gặp lỗi Django sẽ trả về trang error mặc định. Có thể custom lại. (Hoạt động khi Debug=False)
- Khai báo trong URLconf 
```
handler404 = 'mysite.views.my_custom_page_not_found_view'
handler500 = 'mysite.views.my_custom_error_view'
handler403 = 'mysite.views.my_custom_permission_denied_view'
handler400 = 'mysite.views.my_custom_bad_request_view'
```
- Viết các custom view

### 1.5) Including other URLconfs
- thêm module thay cho từng path riêng lẻ
```
from django.urls import include, path

urlpatterns = [
    # ... snip ...
    path('community/', include('aggregator.urls')),
    path('contact/', include('contact.urls')),
    # ... snip ...
]

-------------------------------------------------------
from django.urls import include, path

from apps.main import views as main_views
from credit import views as credit_views

extra_patterns = [
    path('reports/', credit_views.report),
    path('reports/<int:id>/', credit_views.report),
    path('charge/', credit_views.charge),
]

urlpatterns = [
    path('', main_views.homepage),
    path('help/', include('apps.help.urls')),
    path('credit/', include(extra_patterns)),
]
```
- Gom các path giống nhau
```
from django.urls import path
from . import views

urlpatterns = [
    path('<page_slug>-<page_id>/history/', views.history),
    path('<page_slug>-<page_id>/edit/', views.edit),
    path('<page_slug>-<page_id>/discuss/', views.discuss),
    path('<page_slug>-<page_id>/permissions/', views.permissions),
]

--------------------------------------------------------------------

from django.urls import include, path
from . import views

urlpatterns = [
    path('<page_slug>-<page_id>/', include([
        path('history/', views.history),
        path('edit/', views.edit),
        path('discuss/', views.discuss),
        path('permissions/', views.permissions),
    ])),
]
``` 

### 1.6) Passing extra options to view functions
```
urlpatterns = [
    path('blog/<int:year>/', views.year_archive, {'foo': 'bar'}),
]
```
In this example, for a request to /blog/2005/, Django will call views.year_archive(request, year=2005, foo='bar').

```
# main.py
from django.urls import include, path

urlpatterns = [
    path('blog/', include('inner'), {'blog_id': 3}),
]

# inner.py
from django.urls import path
from mysite import views

urlpatterns = [
    path('archive/', views.archive),
    path('about/', views.about),
]
```

### 1.7) Reverse resolution of URLs
```
urlpatterns = [
    path('articles/<int:year>/', views.year_archive, name='news-year-archive'),
]
```
- In templates: Using the url template tag.
```
<a href="{% url 'news-year-archive' 2012 %}">2012 Archive</a>
{# Or with the year in a template context variable: #}
<ul>
{% for yearvar in year_list %}
<li><a href="{% url 'news-year-archive' yearvar %}">{{ yearvar }} Archive</a></li>
{% endfor %}
</ul>
```
- In Python code: Using the reverse() function.
```
from django.http import HttpResponseRedirect
from django.urls import reverse

def redirect_to_year(request):
    year = 2006
    return HttpResponseRedirect(reverse('news-year-archive', args=(year,)))
```
- In higher level code related to handling of URLs of Django model instances: The get_absolute_url() method.

### 1.8) Reversing namespaced URLs
```
from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    ...
]
```
- In templates
```
{% url 'polls:index' %}
```

- In Python
```
reverse('polls:index')
```

## 2) Writing view
### 2.1) Simple view
```
def index(request):
    return HttpResponse("Index")
```
### 2.2) Returning errors
```
from django.http import HttpResponse, HttpResponseNotFound

def my_view(request):
    # ...
    if foo:
        return HttpResponseNotFound('<h1>Page not found</h1>')
    else:
        return HttpResponse('<h1>Page was found</h1>')
        
def detail(request, poll_id):
    try:
        p = Poll.objects.get(pk=poll_id)
    except Poll.DoesNotExist:
        raise Http404("Poll does not exist")
    return render(request, 'polls/detail.html', {'poll': p})
```

## 3) View decorator
### 3.1) Allowed HTTP methods
- `require_http_methods(request_method_list)`
```
from django.views.decorators.http import require_http_methods

@require_http_methods(["GET", "POST"])
def my_view(request):
    # I can assume now that only GET or POST requests make it this far
    # ...
    pass
```
- `require_GET()`: only get
- `require_POST()`: only post
- `require_safe()`: only get and head

### 3.2) Conditional view processing
<a href='https://docs.djangoproject.com/en/2.1/topics/conditional-view-processing/' target='_blank'>Chi tiết xem tại đây</a>

### 3.3) Gzip compression

### 3.4) Vary headers
<a href='https://docs.djangoproject.com/en/2.1/topics/cache/#using-vary-headers' target='_blank'>Chi tiết xem tại đây</a>

### 3.5) Caching

## 4) File Upload
<a href='https://docs.djangoproject.com/en/2.1/topics/http/file-uploads/' target='_blank'>Chi tiết xem tại đây</a>

## 5) Shortcut function
<a href='https://docs.djangoproject.com/en/2.1/topics/http/shortcuts/' target='_blank'>Chi tiết xem tại đây</a>

### 5.1) render()
`render(request, template_name, context=None, content_type=None, status=None, using=None)`

Kết hợp template và context dictionary trả về dưới dạng một HttpResponse

- `request`
- `template_name`: tên của template
- `context`: giá trị trả về dưới dạng dict
- `content_type`: kiểu dữ liệu
- `status`: status code
- `using`: tên của template engine(django, jinja2, ...)

```
from django.shortcuts import render

def my_view(request):
    # View code here...
    return render(request, 'myapp/index.html', {
        'foo': 'bar',
    }, content_type='application/xhtml+xml')
``` 

### 5.2) render_to_response()
`render_to_response(template_name, context=None, content_type=None, status=None, using=None)`

tương tự như render

### 5.3) redirect()
`redirect(to, permanent=False, *args, **kwargs)`

chuyển hướng trang
```
# using namespace
    redirect('some-view-name', foo='bar')
    
# hardcore
    return redirect('/some/url/')

# full url 
    return redirect('https://example.com/')
```
### 5.4) get_object_or_404()
`get_object_or_404(klass, *args, **kwargs)`
Lấy một đối tượng và trả về 404 nếu ko tồn tại

- `klass`: model class, manager or queryset
- `kwargs`: 
```
from django.shortcuts import get_object_or_404

def my_view(request):
    obj = get_object_or_404(MyModel, pk=1)
    
# tương đương với

from django.http import Http404

def my_view(request):
    try:
        obj = MyModel.objects.get(pk=1)
    except MyModel.DoesNotExist:
        raise Http404("No MyModel matches the given query.")
```
Một số ví dụ
```
queryset = Book.objects.filter(title__startswith='M')
get_object_or_404(queryset, pk=1)


get_object_or_404(Book, title__startswith='M', pk=1)


get_object_or_404(Book.dahl_objects, title='Matilda')


author = Author.objects.get(name='Roald Dahl')
get_object_or_404(author.book_set, title='Matilda')
```

### 5.5) get_list_or_404()
`get_list_or_404(klass, *args, **kwargs)`
Trả về một danh sách hoặc 404 nếu ko có giá trị
```
from django.shortcuts import get_list_or_404

def my_view(request):
    my_objects = get_list_or_404(MyModel, published=True)
```

### 5.6) Class-based views
<a href='https://docs.djangoproject.com/en/2.1/topics/class-based-views/' target='_blank'>Khái niệm xem tại đây</a>

<a href='https://docs.djangoproject.com/en/2.1/ref/class-based-views/' target='_blank'>Sử dụng xem tại đây</a>

### 5.7) Advanced

<a href='https://docs.djangoproject.com/en/2.1/howto/outputting-csv/' target='_blank'>CSV</a>

<a href='https://docs.djangoproject.com/en/2.1/howto/outputting-pdf/' target='_blank'>PDF</a>

### 5.8) Middleware
> Middleware is a framework of hooks into Django’s request/response processing. It’s a light, low-level “plugin” system
 for globally altering Django’s input or output.<br>
Each middleware component is responsible for doing some specific function. For example, Django includes 
a middleware component, AuthenticationMiddleware, that associates users with requests using sessions.

<a href='https://docs.djangoproject.com/en/2.1/ref/middleware/' target='_blank'>Available middleware</a>

 