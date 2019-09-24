## 1) Database optimization
### 1.1) Profile first 
Trước tiên xác định query đang làm gì. Các cách xác định câu lệnh SQL:
```
QuerySet.explain()
# or
QuerySet.query
# or 
from django.db import connection 
connection.queries  #với 1 db. 
connection['db_alias'] #với nhiều db 
#trả về  1 list các dict với time(tgian xl), sql(câu lệnh SQL)
``` 

### 1.2) Use standard DB optimization techniques
- Indexes: sử dụng Meta.indexes hoặc Field.db_index để  đánh index, ưu tiên các field hay dùng để filter, exclude, order_by
- Sử dụng kiểu dữ liệu phù hợp

### 1.3) Understand QuerySets
#### 1.3.1) Understand QuerySet evaluation
- that QuerySets are lazy: hành động tạo một QuerySet không thực hiện bất kỳ hành động nào đến db cả cho đến khi "QuerySet is evaluated"
  ```
  >>> q = Entry.objects.filter(headline__startswith="What")
  >>> q = q.filter(pub_date__lte=datetime.date.today())
  >>> q = q.exclude(body_text__icontains="food")
  >>> print(q)
  ``` 
  chỉ khi câu lệnh print(q) thực thi lúc này mới truy vấn đến db.
- when QuerySets are evaluated:
  - Iteration: QuerySet là iterable và nó sẽ thực thi truy vấn db ở lần đầu tiên iterate. Ví dụ:
    ```
    for e in Entry.objects.all():
      print(e.headline)
    ```
  - Slicing: unevaluated
  - Pickling/Caching: evaluated 
  - repr(): evaluated
  - len(): evaluated
  - list(): evaluated
    ```
    entry_list = list(Entry.objects.all())
    ``` 
  - bool(): evaluated 
    ```
    if Entry.objects.filter(headline="Test"):
        print("There is at least one Entry with the headline Test")
    ```
- how the data is held in memory: Mỗi QuerySet đều có cache để giảm truy cập đến db. Lần đầu tiên khi QuerySet is evaluated kết quả sẽ được lưu vào cache.
  ```
  >>> print([e.headline for e in Entry.objects.all()])
  >>> print([e.pub_date for e in Entry.objects.all()])
  # trường hợp này sẽ thực thi truy vấn 2 lần để tối ưu ta sử dụng các bên dưới
  >>> queryset = Entry.objects.all()
  >>> print([p.headline for p in queryset]) # Evaluate the query set.
  >>> print([p.pub_date for p in queryset]) # Re-use the cache from the evaluation.
  ```
  ```
  >>> queryset = Entry.objects.all()
  >>> print(queryset[5]) # Queries the database
  >>> print(queryset[5]) # Queries the database again

  >>> queryset = Entry.objects.all()
  >>> [entry for entry in queryset] # Queries the database
  >>> print(queryset[5]) # Uses cache
  >>> print(queryset[5]) # Uses cache
  ```
  ```
  >>> entry = Entry.objects.get(id=1)
  >>> entry.authors.all()   # query performed
  >>> entry.authors.all()   # query performed again
  # để xử lý vấn đề này hãy xử dụng select_related hoặc prefetch_related
  ```

#### 1.3.2) Use the with template tag
Để cache hoạt động nên sử dụng với with template tag 

#### 1.3.3) Use iterator()
Khi queryset trả về nhiều object thì việc cache sẽ chiếm nhiều dung lượng bộ nhớ, trong trường hợp này iterator() có thể giúp (?). QuerySet.iterator() sẽ đọc kết quả trực tiếp mà ko cache lại

#### 1.3.4) Use explain()
QuerySet.explain() sẽ cho bạn thông tin chi tiết về câu lênh truy vấn, index và join đc sử dụng.

### 2) Do database work in the database rather than in Python
- At the most basic level, use filter and exclude to do filtering in the database.
- Use F expressions to filter based on other fields within the same model.
- Use annotate to do aggregation in the database.

#### 2.1) Use RawSQL
chú ý SQL injection  
```
from django.db.models.expressions import RawSQL
queryset.annotate(val=RawSQL("select col from sometable where othercol = %s", (someparam,)))
``` 

#### 2.2) Use raw SQL 
Django cung cấp 2 cách sử dụng raw SQL:
- Manager.raw(): 
  ```
  for p in Person.objects.raw('SELECT id, first_name FROM myapp_person'):
      print(p.first_name, p.last_name) 
  ```
  ở trường hợp trên sẽ không chỉ thực hiện 1 query, với mỗi last_name của đối tượng p sẽ thực hiện một query do câu raw query chỉ lấy id và first_name. Mặc định câu raw query của Django phải có field id. 
- custom SQL:
  ```
  from django.db import connection

  def my_custom_sql(self):
      with connection.cursor() as cursor:
          cursor.execute("UPDATE bar SET foo = 1 WHERE baz = %s", [self.baz])
          cursor.execute("SELECT foo FROM bar WHERE baz = %s", [self.baz])
          row = cursor.fetchone() 
          # hoặc cursor.fetchall() hoặc dictfetchall(cursor) hoặc 
          # namedtuplefetchall(cursor) 
      return row
  ```

### 3) Retrieve individual objects using a unique, indexed column
```
entry = Entry.objects.get(id=10)
# will be quicker than:
entry = Entry.objects.get(headline="News Item Title")
# because id is indexed by the database and is guaranteed to be unique.

# Doing the following is potentially quite slow:
>>> entry = Entry.objects.get(headline__startswith="News")
```

### 4) Retrieve everything at once if you know you will need it
Use QuerySet.select_related() and prefetch_related()

### 5) Don’t retrieve things you don’t need
#### 5.1) Use QuerySet.values() and values_list()
- Chỉ lấy những field cần thiết 
  ```
  >>>hs = HocSinh.objects.all()
  >>>print(hs.query)
  SELECT "hoc_sinh"."id", "hoc_sinh"."ten", "hoc_sinh"."ho", "hoc_sinh"."ten_dem", "hoc_sinh"."ngay_sinh", "hoc_sinh"."chuc_vu" FROM "hoc_sinh"

  >>>hs = HocSinh.objects.all().values('ten')
  >>>print(hs.query)
  SELECT "hoc_sinh"."ten" FROM "hoc_sinh"
  ```
- Sử dụng khi chỉ muốn lấy kết quả là 1 dict hoặc list mà ko phải là 1 model object 
#### 5.2) Use QuerySet.defer() and only()
- Sử  dụng defer để  loại bỏ những field ko cần.
  ```
  >>> hs = HocSinh.objects.all().defer('ten_dem', 'ho', 'chuc_vu')
  >>> print(hs.query)
  SELECT "hoc_sinh"."id", "hoc_sinh"."ten", "hoc_sinh"."ngay_sinh" FROM "hoc_sinh"
  ```
- Sử  dụng only thì ngược lại với defer là lấy những field cần
  ```
  >>> hs = HocSinh.objects.all().only('id','ten', 'ngay_sinh')
  >>> print(hs.query)
  SELECT "hoc_sinh"."id", "hoc_sinh"."ten", "hoc_sinh"."ngay_sinh" FROM "hoc_sinh"
  ```

#### 5.3) Use QuerySet.count()
if you only want the count, rather than doing `len(queryset)`.

#### 5.4) Use QuerySet.exists()
if you only want to find out if at least one result exists, rather than `if queryset`

#### 5.5) Don’t overuse count() and exists()
Trong trường hợp muốn lấy data từ QuerySet thì nếu sử dụng count và exists sẽ thực hiện query đến data base, thay vào đó ta hoàn toàn có thể  sử dụng data đã Cache

#### 5.6) Use QuerySet.update() and delete()
Sử  dụng để update và xóa nhiều đối tượng thay vi từng đối tượng một sẽ làm tăng số lần tương tác với db

#### 5.7) Use foreign key values directly
Nếu chỉ muốn lấy giá trị FK
```
entry.blog_id
# instead of:
entry.blog.id
```

#### 5.8) Don’t order results if you don’t care
Không nên sắp xếp kết quả nếu bạn ko thật sự cần để tăng hiệu năng. Trong trường hợp model định nghĩa sẵn `Meta.ordering` ban có thể xử dụng order_by()và ko truyền vào tham số nào để loại bỏ sắp xếp.

### 6) Use bulk methods
Sử dụng để giảm số `SQL statements`

#### 6.1) Create in bulk
Sử dụng bulk_create để giảm số query 
```
Entry.objects.bulk_create([
    Entry(headline='This is a test'),
    Entry(headline='This is only a test'),
])

#is preferable to:

Entry.objects.create(headline='This is a test')
Entry.objects.create(headline='This is only a test')
```

#### 6.2) Update in bulk 
new in ver 2.2
```
entries = Entry.objects.bulk_create([
    Entry(headline='This is a test'),
    Entry(headline='This is only a test'),
])

# The following example:

entries[0].headline = 'This is not a test'
entries[1].headline = 'This is no longer a test'
Entry.objects.bulk_update(entries, ['headline'])

# is preferable to:

entries[0].headline = 'This is not a test'
entries.save()
entries[1].headline = 'This is no longer a test'
entries.save()
```

#### 6.3) Insert in bulk
Khi insert object vào M2M sử dụng add() với nhiều objects để giảm số query
```
my_band.members.add(me, my_friend)

#is preferable to:

my_band.members.add(me)
my_band.members.add(my_friend)
```