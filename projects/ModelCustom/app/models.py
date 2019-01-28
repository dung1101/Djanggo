from django.db import models
"""
A model is the single, definitive source of information about your data. It contains the essential fields and behaviors 
of the data you’re storing. Generally, each model maps to a single database table.

The basics:
    - Each model is a Python class that subclasses django.db.models.Model.
    - Each attribute of the model represents a database field.
    - With all of this, Django gives you an automatically-generated database-access API;
"""


class HocSinh(models.Model):
    ten = models.CharField(max_length=30)
    ho = models.CharField(max_length=30)
    ten_dem = models.CharField(max_length=30)
    ngay_sinh = models.DateField()
    LOP_TRUONG = 'LT'
    LOP_PHO = 'LP'
    BI_THU = 'BT'
    THANH_VIEN = 'TV'
    LUA_CHON_CHUC_VU = (
        (LOP_TRUONG, 'Lớp trưởng'),
        (LOP_PHO, 'Lớp phó'),
        (BI_THU, 'Bí thư'),
        (THANH_VIEN, "Thành viên")
    )
    chuc_vu = models.CharField(max_length=2, choices=LUA_CHON_CHUC_VU, default=THANH_VIEN)

    class Meta:
        db_table = 'hoc_sinh'


class Lop(models.Model):
    ten = models.CharField(max_length=3)
    khoi = models.IntegerField()

    class Meta:
        db_table = 'lop'

