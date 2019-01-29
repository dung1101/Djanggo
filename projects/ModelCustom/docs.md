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

### 2.3) Custom Field
<a href='https://docs.djangoproject.com/en/2.1/ref/models/fields/#field-types' target='_blank'>Chi tiết xem tại đây</a>


### 3) Relationship
<a href='https://docs.djangoproject.com/en/2.1/howto/custom-model-fields/' target='_blank'>Chi tiết xem tại đây</a>

### 3.1) `Many-to-one`: ForeignKey

```
# Một xe chỉ có một nhà sản xuất

class Manufacturer(models.Model):
    # ...
    pass

class Car(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    # ...
```
#### ForeignKey Arguments
`on_delete`: thực hiện khi đối tượng FK bị xóa
- `models.CASADE`: khi FK bị xóa thì cũng xóa cả đối tượng luôn
- `models.PROTECT`: bảo vệ cho đối tượng FK ko bị xóa
- `models.SET_NULL`: set giá trị về `null` (option null=True)
- `models.SET_DEFAULT`: set về default
- `models.SET(...)`: do something
- `models.DO_NOTHING`: Take no action. If your database backend enforces referential integrity, this will cause an 
IntegrityError unless you manually add an SQL ON DELETE constraint to the database field.

`limit_choices_to`: giới hạn FK liên kết theo yêu cầu nào đó (chỉ sử dụng cho ModelForm)

```
staff_member = models.ForeignKey(
    User,
    on_delete=models.CASCADE,
    limit_choices_to={'is_staff': True},
```

`related_name`: dùng để query ngược từ object FK
ví dụ 
```
class Map(db.Model):
    members = models.ManyToManyField(User, related_name='maps', verbose_name=_('members'))
```
Ta có field members liên kết đến bảng User như vậy ta có thể sử dụng câu lệnh `User.maps.all()`
để query. Nếu ta không dùng related_name thì Django co set mặc định là `User.map_set.all()`
Nếu có một đối tượng curent_user ta có thể query bằng `current_user.maps.all()` ...

`related_query_name`: dùng để query ngược bằng object FK
ví dụ
```
class Tag(models.Model):
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name="tags",
        related_query_name="tag",
    )
    name = models.CharField(max_length=255)

# That's now the name of the reverse filter
Article.objects.filter(tag__name="important")
# Lấy những bài báo mà có Tag.name="important"
```

`to_field`: liên kết đến field nào của FK mặc định là PK,
nếu thay đổi thì field đó unique=True

### 3.2) `Many-to-many`: ManyToManyField
```
class Player(models.Model):
    name = models.CharField(max_length=30)
    
    
# Một team có nhiều player
class Team(models.Model):
    members = models.ManyToManyField(Player)
```

Django sẽ tự sinh ra một table với tên là team_members với
3 fields là `id(PK), team_id(FK), player_id(FK)`

#### ManyToManyField Arguments 
`related_name`, `related_query_name`, `limit_choices_to` giống
ForeignKey

`symmetrical`: dùng khi FK đến chính bản thân
```
class Person(models.Model):
    friends = models.ManyToManyField("self")

--------------------------------------------
p = Person.objects.get(id=1)
p.friends.all()
--------------------------------------------
<QuerySet [<Person: Person object (2)>, 
           <Person: Person object (3)>, 
           <Person: Person object (4)>,
           <Person: Person object (5)>]>
```

`through`: Django tự động tạo ra table mới khi có liên kết nhiều
nhiều tuy nhiên có thể tạo manual sử dụng `through`
```
from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person, through='Membership')

    def __str__(self):
        return self.name

class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)
```
`through_field`
```
class Person(models.Model):
    name = models.CharField(max_length=50)

class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(
        Person,
        through='Membership',
        through_fields=('group', 'person'),
    )

class Membership(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    inviter = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name="membership_invites",
    )
    invite_reason = models.CharField(max_length=64)
```
table Membership có 2 FK đến Person nên Django sẽ ko biết cái
nào thuộc m-to-m relationship nên `through` chỉ rõ field nào
là m-to-m

`db_table`: đặt tên cho table mà Django tự sinh ra.

### 3.3) `one-to-one`: OneToOneField
Giống ForeignKeyField với unique=True, tuy nhiên khổn
thể query ngược từ FK. Thường dùng để mở rộng table
```
class Engine(models.Model):
    name = models.CharField(max_length=25)


class Car(models.Model):
    name = models.CharField(max_length=25)
    engine = models.OneToOneField(Engine)
```

## 4) class Meta
### 4.1) Attributes
<a href='https://docs.djangoproject.com/en/2.1/ref/models/options/' target='_blank'>Chi tiết xem tại đây</a>

## 5) Model methods
<a href='https://docs.djangoproject.com/en/2.1/ref/models/instances/#model-instance-methods' target='_blank'>Chi tiết xem tại đây</a>

### 5.1) Create objects
`__init__`: không nên ghi đè `__init__` method thay vào đó có thể sử dụng 2 cách sau:
```
# cách 1
class Book(models.Model):
    title = models.CharField(max_length=100)

    @classmethod
    def create(cls, title):
        book = cls(title=title)
        # do something with the book
        return book

book = Book.create("Pride and Prejudice")

# cách 2
class BookManager(models.Manager):
    def create_book(self, title):
        book = self.create(title=title)
        # do something with the book
        return book

class Book(models.Model):
    title = models.CharField(max_length=100)

    objects = BookManager()

book = Book.objects.create_book("Pride and Prejudice")

``` 

### 5.2) Validating objects
- `clean_fields()`: validate the model fields
- `clean()`: validate whole model
- `validate_unique()`: Validate the field uniqueness
- `full_clean()`:

### 5.3) Save & Delete
```
class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def save(self, *args, **kwargs):
        if self.name == "Yoko Ono's blog":
            return # Yoko shall never have her own blog!
        else:
            super().save(*args, **kwargs)  # Call the "real" save() method.
```

## 6) Model inheritance
```
class CommonInfo(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()

    class Meta:
        abstract = True

class Student(CommonInfo):
    home_group = models.CharField(max_length=5)
```