# python 学习总结

本次总结整理主要以milvus使用脚本为主。

## 一、milvus_toolkit.py整理

1、枚举列表的格式

```python
topk_scope = [1,1, 20, 50, 100, 300, 500, 800, 1000]
```

2、字符串变量赋值用单引号

```python
IDMAP_FOLDER_NAME = 'idmap'
```

3、函数体的格式

```python
def connect_server():
    print("connect to milvus")
    status = MILVUS.connect(host=SERVER_ADDR, port=SERVER_PORT, timeout=1000 * 1000 * 20)
    handle_status(status=status)
    return status
# 函数体执行结束以后可以返回值也可以不返回值
```

4、利用字典对变量进行赋值

```python
param = {'table_name': table_name, 'dimension': dim, 'index_file_size':index_file_size, 'metric_type':metric_type}
```

5、Python字符串、元组、列表、访问元素方法是一样的

```python
 print(MILVUS.server_version()[1])
```

6、python中对文件的操作

（1）将文件夹的内容保存到列表，并将列表进行字典排序

```python
import os
filenames = os.listdir(NQ_FOLDER_NAME)
filenames.sort()
# filenames
# ['1.csv', '2.csv', '3.csv', 'a.csv', 'b.csv', 'c.csv']
```

7、如何将npy形式的数据文件读成列表存储

```python
data = np.load(file_name)
vec_list = data.tolist()
```

8、如何将csv形式的数据文件读成列表存储

```python
import pandas as pd
data = pd.read_csv(file_name, header=None)
data = np.array(data)
vec_list = data.tolist()
```

9、列表的截取

```
L=['Google', 'Runoob', 'Taobao']
L[2] # 读取列表第三个元素
L[1:] # 读取从第二个元素开始后的所有元素
```

10、循环结构

```python
for filename in filenames: # filenames是列表
        vec_list = load_vec_list(NQ_FOLDER_NAME + '/' + filename)
        
for i in range(10): #从0-9
        sqrt_sum = np.sum(np.power(vetors[i], 2))
```

11、判断

```python
if IS_CSV:
        import pandas as pd
        data = pd.read_csv(file_name, header=None)
        data = np.array(data)
    else:
        data = np.load(file_name)
```

12、对文件的读写

```python
file = open(filename, "w+")
file.write('nq,topk,total_time,avg_time' + '\n')

line = str(nq) + ',' + str(k) + ',' + str(round(time_cost, 4)) + ',' + str(round(time_cost / nq, 4)) + '\n'
file.write(line)

file.write('\n')

file.close()


# 可以利用with语句简化读写文件
# 读
with open('/path/to/file', 'r') as f:
    print(f.read())
# 如果文件很小，read()一次性读取最方便；如果不能确定文件大小，反复调用read(size)比较保险；如果是配置文件，调用readlines()最方便：
for line in f.readlines():
    print(line.strip()) 
    
# 写
with open('/Users/michael/test.txt', 'w') as f:
    f.write('Hello, world!')
```

13、创建和删除文件夹

```python
# 创建
if not os.path.exists(PE_FOLDER_NAME):
        os.mkdir(PE_FOLDER_NAME)

# 删除
if os.path.exists(IDMAP_FOLDER_NAME + table_name + IDMAP_NAME):
                os.remove(IDMAP_FOLDER_NAME + table_name + IDMAP_NAME)   
```

14、代码执行入口

```python
def main:
    print()
if __name__ == '__main__':
    main()
```



## 二、milvus_load.py整理

1、向列表里面添加元素

```python
vectors_ids.append(int(location))
```

2、向量归一化

（1）利用map reduce

```python
vec = vec_list[i]
square_sum = reduce(lambda x, y: x + y, map(lambda x: x * x, vec))
sqrt_square_sum = np.sqrt(square_sum)
coef = 1 / sqrt_square_sum
vec = list(map(lambda x: x * coef, vec))
vec_list[i] = vec
```

map reduce lambda参考链接：https://blog.csdn.net/edogawachia/article/details/79751093

（2）利用sklearn包

```python
import sklearn.preprocessing
# 随机生成向量
vector_tmp = [[random.random() for i in range(dimension)] for i in range(nq)]
vectors = sklearn.preprocessing.normalize(vector_tmp, axis=1, norm="l2").tolist()
```

3、python读取大型的.bvecs文件

```python
def load_bvecs_data(fname, base_len, idx):
    begin_num = base_len * idx
    # print(fname, ": ", begin_num)
    x = np.memmap(fname, dtype='uint8', mode='r')
    d = x[:4].view('int32')[0]
    data = x.reshape(-1, d + 4)[begin_num:(begin_num + base_len), 4:]
    data = (data + 0.5) / 255
    # data = normaliz_data(data)
    return data
```



## 三、milvus_search.py整理



## 四、python练习题

1、python中range函数的用法

python range() 函数可创建一个整数列表，一般用在 for 循环中。

**函数语法**

```
range(start, stop[, step])
```

参数说明：

- start: 计数从 start 开始。默认是从 0 开始。例如range（5）等价于range（0， 5）;
- stop: 计数到 stop 结束，但不包括 stop。例如：range（0， 5） 是[0, 1, 2, 3, 4]没有5
- step：步长，默认为1。例如：range（0， 5） 等价于 range(0, 5, 1)

**实例**

>>>range(10)        # 从 0 开始到 10
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> range(1, 11)     # 从 1 开始到 11
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> range(0, 30, 5)  # 步长为 5
[0, 5, 10, 15, 20, 25]
>>> range(0, 10, 3)  # 步长为 3
[0, 3, 6, 9]
>>> range(0, -10, -1) # 负数
[0, -1, -2, -3, -4, -5, -6, -7, -8, -9]
>>> range(0)
[]
>>> range(1, 0)
[]

以下是 range 在 for 中的使用，循环出runoob 的每个字母:

```python
>>>x = 'runoob'
>>> for i in range(len(x)) :
...     print(x[i])
... 
r
u
n
o
o
b
>>>
```

2、python中的split() 

语法：

```python
str.split(str="", num=string.count(str)).
```

参数：

- str -- 分隔符，默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等。
- num -- 分割次数。默认为 -1, 即分隔所有。

返回值：

返回分割后的字符串列表。