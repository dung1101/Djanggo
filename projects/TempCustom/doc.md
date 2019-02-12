# Template

### 1) Configuration
default configuration

```
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```
    
`BACKEND`: khai báo engine django.DjangoTemplates hoặc jinja2.Jinja2

`DIRS`: danh sách các thư mục template

`APP_DIRS`: nếu khai báo bằng true sẽ tìm kiếm template trong app

`OPTIONS`: <a href='https://docs.djangoproject.com/en/2.1/ref/templates/api/#built-in-template-context-processors' target='_blank'>
Chi tiết xem tại đây</a>

Ví dụ
```
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR + '/home/html/example.com',
            BASE_DIR + '/home/html/default',
        ],
    },
    {
        'BACKEND': 'django.template.backends.jinja2.Jinja2',
        'DIRS': [
            BASE_DIR + '/home/html/jinja2',
        ],
    },
]
``` 

### 2) Django template language
<a href='https://docs.djangoproject.com/en/2.1/ref/templates/language/' target='_blank'>Chi tiết xem tại đây</a>

### 3) Built-in template tags and filters
<a href='https://docs.djangoproject.com/en/2.1/ref/templates/builtins/#ref-templates-builtins-tags' target='_blank'>
Chi tiết xem tại đây</a>

### 4) Humanize
> A set of Django template filters useful for adding a “human touch” to data.

> To activate these filters, add 'django.contrib.humanize' to your INSTALLED_APPS setting. 
Once you’ve done that, use {% load humanize %} in a template, and you’ll have access to the following filters.

<a href='https://docs.djangoproject.com/en/2.1/ref/contrib/humanize/' target='_blank'>Chi tiết xem tại đây</a>

### 5) Custom tag
<a href='https://docs.djangoproject.com/en/2.1/howto/custom-template-tags/' target='_blank'>Chi tiết xem tại đây</a>


