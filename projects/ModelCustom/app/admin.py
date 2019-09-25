from django.contrib import admin
from app.models import HocSinh, Lop

# Register your models here.
@admin.register(HocSinh)
class HocSinhAdmin(admin.ModelAdmin):
    pass

@admin.register(Lop)
class LopAdmin(admin.ModelAdmin):
    pass