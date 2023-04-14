# Ish语法

ISH的语法与Bash的语法相似，但是有一些不同。

## 变量


### 变量定义
Bash中定义变量是：

```bash
var="value"
```

而在ISH中定义变量是：

```bash
$var="value"
```

### 变量调用
Bash中调用变量和ISH中调用变量是一样的：

```bash
echo $var
```

### 变量类型
ISH中的变量类型支持Python中的所有类型，包括`int`、`float`、`str`、`bool`、`list`、`dict`、`tuple`、`set`、`None`。

### 变量赋值
ISH中变量不仅支持赋值，也支持加减乘除等运算。具体如下：
    
```bash
$a=1
$b=$a+1
$c=$a+$b
```

## 流程控制

### if语句
Bash中的if语句是：

```bash
if [ $a -eq 1 ]; then
    echo "a=1"
elif [ $a -eq 2 ]; then
    echo "a=2"
else
    echo "a!=1 and a!=2"
fi
```

Ish沿袭了Bash的语法，但是增加了一些新的语法，如下：

```cpp
!if ($a==1)
> echo "a=1"
> echo "This is more than one line"
!elseif ($a==2)
> echo "a=2"
!else
> echo "a!=1 and a!=2"
!endif
```
您会发现，在Ish中，if语句的语法是以`!if`开始，以`!endif`结束，每一行的语句都必须以`>`开始，`!elseif`和`!else`也是以`>`开始。

也就是说，在ISH中的流程语句的关键字（条件语句）必须以`!`开头，如`!if`、`!else`、`!elseif`、`!endif`等。

### for语句
Bash中的for语句是：

```bash
for i in {1..10}
do
    echo $i
done
```

基于上面提到的规则，Ish中的for语句是：

```cpp
!for ($i;1,10,1)
> echo $i
!endfor
// 输出1-10
```

我们不难发现，for循环的条件（括号内的内容）是以`;`分隔，分隔后的内容分别是变量名（$i）、起始值、结束值、步长。

### while语句
Bash中的while语句是：

```bash
while [ $a -lt 10 ]
do
    echo $a
    a=$a+1
done
```

Ish中的while语句是：

```cpp
!while ($a<10)
> echo $a
> $a=$a+1
!endwhile
// 输出1-10
```

### 函数
Bash中的函数是：

```bash
function func()
{
    echo "This is a function"
}
```

Ish中的函数是：

```cpp
!dec func()
> echo "This is a function"
!enddec
```

## 其他

### 注释
Bash中的注释是：

```bash
# This is a comment
```

Ish中的注释是：

```txt
# This is a comment
或者
; This is a comment
```
中间都要有一个空格，且注释占一整行，注释标识符要放在第一位。
