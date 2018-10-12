# python-sql-faker
#### 轻量级、易拓展的数据库智能填充开源库（Python实现版）

## 开源库特性

+ 支持主流的MySQL、Oracle、SQL Server、SQLite数据库
+ 支持8种常见数据库字段类型的智能填充，并支持自定义拓展
+ 支持一次性插入百万级别的数据
+ 支持事务
+ 支持python2.7

## 使用示范

``` python
from sql_faker import Faker, DataType, Values, Times, DBHelper
import pymysql

# 设置数据库信息
DBHelper.db_setting(db='python_sql_faker',
                    driver=pymysql,
                    user='root',
                    passwd='123456',
                    host='127.0.0.1',
                    port=3306)

#  给user表的四个字段填充5条数据
Faker.table_name("user") \
    .param("name", DataType.USERNAME) \
    .param("age", DataType.AGE) \
    .param("address", DataType.ADDRESS) \
    .param("birthday", DataType.TIME) \
    .insert_count(5) \
    .execute()
```

上述代码将生成如下SQL语句，并在数据库中执行：

```sql
insert into user(name,age,sex,address,birthday) values('武叹霜', 21, '山西省晋城市泽州县庆达路463号', '2018-02-24 10:56:37')
insert into user(name,age,sex,address,birthday) values('顾什可', 50, '广西壮族自治区柳州市融水苗族自治县德堡路419号', '2018-04-09 08:10:22')
insert into user(name,age,sex,address,birthday) values('蔡静随', 46, '河南省郑州市巩义市广延路240号', '2018-06-11 23:02:19')
insert into user(name,age,sex,address,birthday) values('韦丸赤', 27, '河南省焦作市博爱县浦润路148号', '2018-02-22 15:52:50')
insert into user(name,age,sex,address,birthday) values('任徐', 54, '河南省新乡市延津县汉源路14号', '2018-07-07 03:48:51')
```



## 依赖添加

本开源库另外依赖了DBUtils和pymysql库，需要一起进行pip安装。

``` python
pip install sql-faker
pip install DBUtils
pip install pymysql
```

**注意**：默认使用MySQL数据库，如需更换成Oracle、SQL Server、SQLite等DBUtils连接池支持的数据库，可另行添加依赖，并在DBHelper.db_setting(driver=驱动对象)方法中指定数据库驱动。



## 数据库连接

#### 一、连接属性设置

在进行插入数据之前需要设置数据库属性，如代码所示：

``` python
from sql_faker import DBHelper
import pymysql

# 设置数据库信息
DBHelper.db_setting(db='python_sql_faker',
                    driver=pymysql, # 设置连接驱动
                    user='root',
                    passwd='123456',
                    host='127.0.0.1',
                    port=3306)
```


可设置的属性如下表：

|  属性名   |   说明    |    默认值    |
| :----: | :-----: | :-------: |
|   db   |  数据库名   |     无     |
| driver | 数据库驱动对象 |  pymysql  |
|  user  | 数据库用户名  |   root    |
| passwd |  数据库密码  |   12345   |
|  host  |  主机地址   | localhost |
|  port  |   端口号   |   3306    |



#### 二、特殊情况

1. 当数据库属性值都等于默认值时，可只设置数据库名：

``` python
DBHelper.db_setting('python_sql_faker')
```



#### 三、支持的驱动类型

```python
# 支持的驱动类型，可在DBHelper.db_setting(driver=驱动对象)方法指定数据库驱动
# 1.首先在控制台进行pip安装
pip install pymysql # mysql
pip install pymssql # sqlserver
pip install cx_Oracle # oracle
pip install sqlite3 # sqlite3

# 2.之后导入所需驱动，设置到driver属性中
DBHelper.db_setting(db='python_sql_faker',
                    driver=cx_Oracle) # 设置连接驱动
```



**注意** ：数据库配置只需要设置一次，之后可以多次调用Faker进行插入数据操作。



## 数据插入

### 一、属性介绍
可设置的属性如下表：

|         属性名          |          说明           |
| :------------------: | :-------------------: |
|  table_name(数据库表名)   |        设置数据库表名        |
| param(字段名, 数据生成器类型①) | 设置数据库字段名，以及对应的数据生成器类型 |
|  insert_count(插入条数)  |       设置插入数据条数        |
|      execute( )      | 生成SQL，显示在控制台，并在数据库中执行 |
|   only_show_sql( )   |     生成SQL，并显示在控制台     |
|      ignored( )      |        不执行任何操作        |

注意：① 数据生成器类型，必须是DataType枚举值，或实现了RandomData接口的类。

使用示例：
``` java
// 给user表的四个字段填充5条数据
Faker.table_name("user") \
    .param("name", DataType.USERNAME) \
    .param("age", DataType.AGE) \
    .param("sex", DataType.SEX) \
    .param("birthday", DataType.TIME) \
    .insert_count(5) \
    .execute()

// 给user表的两个字段生成5条SQL，并显示在控制台
Faker.table_name("user") \
    .param("name", DataType.USERNAME) \
    .param("age", DataType.AGE) \
    .insert_count(5) \
    .only_show_sql()

// 不执行任何操作，不生成SQL，不显示在控制台
Faker.table_name("user") \
    .param("name", DataType.USERNAME) \
    .param("age", DataType.AGE) \
    .insert_count(5) \
    .ignored()
```



### 二、插入数据的方式

本开源库一共支持三种插入数据的方式，可以混合使用。

#### 1. 使用DataType指定数据类型

DataType一共支持8种枚举类型，如下表所示：

|   属性名    |  说明  |         类型         |         示例值         |
| :------: | :--: | :----------------: | :-----------------: |
|    ID    | 用户ID |   19位的数字型UUID字符串   | 1049120504188764160 |
| USERNAME | 用户名  |    长度为2到4个字的中文名    |         武叹霜         |
|   TIME   |  时间  | 一年前到现在的时间范围内任意一个时刻 | 2018-03-01 12:41:00 |
|  PHONE   | 手机号  |       11位手机号       |     13192668109     |
| ADDRESS  |  地址  |    国内地址，详细到门牌号     |  四川省绵阳市盐亭县北利路738号   |
|   AGE    |  年龄  |     18到60岁的数字      |         19          |
|   SEX    |  性别  |     字符，0：男，1：女     |         '1'         |
|  EMAIL   |  邮箱  |      常见邮箱字符串       |  Alex705@gmail.com  |

使用示例：

```java
// 给user表的8个字段填充1条数据
Faker.table_name("user") \
    .param("id", DataType.ID) \
    .param("name", DataType.USERNAME) \
    .param("birthday", DataType.TIME) \
    .param("phone", DataType.PHONE) \
    .param("address", DataType.ADDRESS) \
    .param("age", DataType.AGE) \
    .param("sex", DataType.SEX) \
    .param("email", DataType.EMAIL) \
    .insert_count(1) \
    .execute()
```
对应生成的SQL语句如下：

```sql
insert into 
user(
  id, name, birthday,
  phone, address, age,
  sex, email
) 
values(
  '1049120504188764160', '武叹霜', '2018-03-01 12:41:00',
  '13192668109', '四川省绵阳市盐亭县北利路73号', 19,
   '1', 'Alex705@gmail.com'
)
```



#### 2. 使用 Values.of()系列方法生成取值范围

Values类共有以下8种生成取值范围方法，如下表：


|                方法名                |                  取值范围                   |         示例值         |
| :-------------------------------: | :-------------------------------------: | :-----------------: |
|         Values.of(可变长参数)          |             从可变长参数中任意抽取一个值              |  "优品", "良品", "次品"   |
|   Values.of_int_range(起始值,结束值)    |          在[起始值, 结束值]的范围内取一个整数           |         33          |
| Values.of_float_range(起始值,结束值,精度) | 在[起始值, 结束值]的范围内取一个浮点数，默认精确到小数点后2位，最多10位 |     123.333333f     |
|   Values.ofTimeRange(开始时间，结束时间)   |       在[开始时间, 结束时间]的范围内取一个时间，精确到秒       | 2018-03-14 13:21:11 |

另外，Times类中还有用于设定时间的两个方法：

|          方法名          |     说明      |
| :-------------------: | :---------: |
|    Times.of(年,月,日)    | 用于生成时间，精确到日 |
| Times.of(年,月,日,时,分,秒) | 用于生成时间，精确到秒 |



使用示例：



```java
// 给product表的9个字段填充1条数据
Faker.table_name("product")\
      .param("type", Values.of("优品", "良品", "次品"))\
      .param("person_count", Values.of_int_range(20, 50))\
      .param("enter_price", Values.of_float_range(12.33, 34.57))\
      .param("outcome_price", Values.of_float_range(100.004132, 240.281424, 6))\
      .param("firstTime", Values.of_time_range(Times.of(2018,3,22), Times.of(2018,10,22)))\
      .param("secondTime",
             Values.of_time_range(
                Times.of(2018,3,22,11,23,24),
                Times.of(2018,10,22,22,15,17)
             )
       )\
      .insert_count(1)\
      .only_show_sql()
```

对应生成的SQL语句如下：

```sql
insert into 
product(
  type, person_count, total_count,
  enter_price, outcome_price, speed,
  salary, firstTime, secondTime
) 
values(
  '良品', 33, 777777777,
  22.22, 123.333333, 788.31,
  1820.4231, '2018-03-14 00:00:00', '2018-03-14 13:21:11'
)
```



#### 3. 继承RandomData类，重写create()方法，提供可随机生成的返回值

RandomData类的代码如下：

```java
class RandomData:
    """随机值抽象类，子类必须实现create方法"""
    __metaclass__ = ABCMeta

    @abstractmethod
    def create(self):
        pass
```

继承该类，并重写create( )方法提供一个可随机生成的返回值，该返回值就是数据库字段对应插入的值。

使用示例：

1. 创建一个自定义类EnglishNameRandom，继承RandomData类，并提供一个可随机生成的返回值。

``` python
import random
from sql_faker import Faker, DataType, Values, Times, DBHelper, RandomData

# 英文名数据生成器
class EnglishNameRandom(RandomData):
    def create(self):
        # 使用choice()方法从列表中随机抽取一个值，作为返回值
        return random.choice(['jack', 'andy', 'kim']) 
```

2. 在Faker中给字段指定使用EnglishNameRandom类型的生成器。

```java
// 指定name字段使用EnglishNameRandom类进行随机值的生成
Faker.table_name("user")\
       .param("name", EnglishNameRandom)\
       .param("age", Values.of_int_range(20, 50))\
       .param("address", DataType.ADDRESS)\
       .insert_count(5)\
       .execute()
```

对应生成的SQL语句如下：
```sql
insert into user(name, age, address) 
values('Andy Wang', 23, '四川省绵阳市盐亭县北利路73号')
```


PS：如果有任何建议，可以在Issues中提出，如添加DataType的默认类型等。



## License

The python-sql-faker is released under MIT License.