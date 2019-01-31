from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt

from .models import Game
from . import views

app_name = 'app'
urlpatterns = [
    path('', views.index, name='index'),
    path('test', views.test, name='test'),
    path('<int:pk>/', views.detail, name='detail'),
    path('post_only', views.post_only, name='post_only'),
    path('class_base/', include([
        path('normal_view', csrf_exempt(views.NormalView.as_view())),
        path('template_view', csrf_exempt(views.TempVi.as_view())),
        path('redirect_view', views.ReVi.as_view()),
    ])),
    path('class_display/', include([
        path('detail_view/<int:pk>', views.DeVi.as_view(), name='detail_view'),
        path('list_view', views.LiVi.as_view(), name='list_view'),
    ])),
    path('class_edit/', include([
        path('form_view', csrf_exempt(views.FormVi.as_view()), name='form_view'),
        path('create_view', csrf_exempt(views.CreateVi.as_view()), name='create_view'),
        path('update_view/<int:pk>', csrf_exempt(views.UpdateVi.as_view()), name='update_view'),
        path('delete_view/<int:pk>', csrf_exempt(views.DeleteVi.as_view()), name='delete_view'),
    ])),
    path('class_date/', include([
        path('archive_view',
             views. ArchiveIndexVi.as_view(model=Game, date_field="release", template_name="archive_vi.html"),
             name="archive_view"),
        path('year_archive_view/<int:year>', views.YearArchiveVi.as_view(), name="year_archive_view"),
    ])),
]

