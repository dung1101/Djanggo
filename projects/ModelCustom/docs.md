# Models
> - Model quy định cấu trúc database
> - Mỗi một class tương ứng với một table, mỗi attribute tương ứng với một field trong table
> - Django cung cấp API để tương tác với db mà không sử dụng sql command 
> - Tên của table mặc định [tên app]_[tên class] tuy nhiên có thể thay đổi được sử dụng 
class Meta 
> - id field được thêm mặc định và được đặt làm khóa chính tuy nhiên có thể thay đổi được

<a href='https://docs.djangoproject.com/en/2.1/ref/models/' target='_blank'>chi tiết xem tại đây</a>
## 1) class
Tạo lớp con kế thừa lớp models.Model

Kiểu dữ liệu:
- models.CharField: kiểu ký tự
- models.IntegerField: kiểu int

## 2) Field
<a href='https://docs.djangoproject.com/en/2.1/ref/models/fields/' target='_blank'>chi tiết xem tại đây</a>
### 2.1) field option
#### `null`
Mặc định là `False`, cho phép để trống, giá trị trống sẽ lưu là 'NULL' trong db. 
Tránh sử dụng 'NULL' cho CharField và TextField vì lúc đó sẽ có 2 trường hợp cho 'no data' 
là 'NULL' và empty string. Trong hầu hết các trường hợp Django sử dụng empty string. Tuy nhiên
 có một ngoại lệ là CharField (unique=True, blank=True) khi đó lưu là empty string sẽ bị lỗi
  lúc này nên sử dụng null
#### `blank`
Mặc định là `False`, cho phép để trống, giá trị trống sẽ lưu là empty string
#### `choices`
Lựa chọn giá trị. Ta sẽ khai báo một iterable(list, tuple) với mỗi phần tử trong đó có 2 giá
trị (ví dụ `[(A,AA), (C, CC), (E, EE)]`). Các giá trị sẽ được validate và khi sử dụng form 
thì select box sẽ được tạo và chọn từ những giá trị này thay cho text thông thường.

```
# khai báo cách 1
class Student(models.Model):
    YEAR_IN_SCHOOL_CHOICES = (
        ('FR', 'Freshman'),
        ('SO', 'Sophomore'),
        ('JR', 'Junior'),
        ('SR', 'Senior'),
    )
    year_in_school = models.CharField(max_length=2, choices=YEAR_IN_SCHOOL_CHOICES)

    
# khai báo cách 2 (khuyên dùng): cách này dễ dàng để liên kết ta có thể sử dụng 
# ví dụ: Student.FRESHMAN có thể được dùng ở bất cứ đâu mà model Student được import
class Student(models.Model):
    FRESHMAN = 'FR'
    SOPHOMORE = 'SO'
    JUNIOR = 'JR'
    SENIOR = 'SR'
    YEAR_IN_SCHOOL_CHOICES = (
        (FRESHMAN, 'Freshman'),
        (SOPHOMORE, 'Sophomore'),
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior'),
    )
    year_in_school = models.CharField(
        max_length=2,
        choices=YEAR_IN_SCHOOL_CHOICES,
        default=FRESHMAN,
    )
    
    def is_upperclass(self):
        return self.year_in_school in (self.JUNIOR, self.SENIOR)
``` 
chia theo nhóm
```
MEDIA_CHOICES = (
    ('Audio', (
            ('vinyl', 'Vinyl'),
            ('cd', 'CD'),
        )
    ),
    ('Video', (
            ('vhs', 'VHS Tape'),
            ('dvd', 'DVD'),
        )
    ),
    ('unknown', 'Unknown'),
)
```

####`db_column`
Đặt tên cho field trong db mặc định sẽ là tên của attribute

#### default 
Set giá trị mặc định

#### help_text
hữu dụng cho documents

#### primary_key
`True` khai báo field là khóa chính. Mặc định Django sẽ khai báo id là khóa chính.
Mỗi bảng chỉ có một khóa chính duy nhất

#### unique
`True` khai báo giá trị là duy nhất.

### 2.2) Field types
<a href='https://docs.djangoproject.com/en/2.1/ref/models/fields/#field-types' target='_blank'>Chi tiết xem tại đây</a>

### 3) Relationship
<a href='https://docs.djangoproject.com/en/2.1/ref/models/fields/#ref-foreignkey' target='_blank'>Chi tiết xem tại đây</a>

### 3.1) `Many-to-one`

```
# Một xe chỉ có một nhà sản xuất

class Manufacturer(models.Model):
    # ...
    pass

class Car(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    # ...
```
#### 3.1.1) Option
`on_delete`: thực hiện khi đối tượng FK bị xóa
- `models.CASADE`: khi FK bị xóa thì cũng xóa cả đối tượng luôn
- `models.PROTECT`: bảo vệ cho đối tượng FK ko bị xóa
- `models.SET_NULL`: set giá trị về `null` (option null=True)
- `models.SET_DEFAULT`: set về default
- `models.SET(...)`: do something
- `models.DO_NOTHING`: Take no action. If your database backend enforces referential integrity, this will cause an 
IntegrityError unless you manually add an SQL ON DELETE constraint to the database field.

`limit_choices_to`: giới hạn FK liên kết theo yêu cầu nào đó (chỉ sử dụng cho ModelField)

```
staff_member = models.ForeignKey(
    User,
    on_delete=models.CASCADE,
    limit_choices_to={'is_staff': True},
```


