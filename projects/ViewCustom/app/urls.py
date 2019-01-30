from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt

from . import views

app_name = 'app'
urlpatterns = [
    path('', views.index, name='index'),
    path('test', views.test, name='test'),
    path('<int:pk>/', views.detail, name='detail'),
    path('post_only', views.post_only, name='post_only'),
    path('class/', include([
        path('normal_view', csrf_exempt(views.NormalView.as_view())),
        path('template_view', csrf_exempt(views.TempVi.as_view())),
        path('redirect_view', views.ReVi.as_view()),
        path('detail_view/<int:pk>', views.DeVi.as_view()),
        path('list_view', views.LiVi.as_view()),
    ])),
]

