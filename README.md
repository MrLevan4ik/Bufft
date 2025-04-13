# Bufft, Bufft Assembly/Bytecode, BVM
##### Эзотерический язык программирования, который пытается быть похожим на ассемблер. Написан MrLevan4ik и BTXD.

---
## Посвящение в язык
**Bufft Assembly** - это язык, на котором пишется код  
**Bufft Bytecode** -  это декодированный код, передающийся напрямую в интерпретатор

Комментарии начинаются с символа ; и работают только в Bufft Assembly (Bufft Bytecode не поддерживает комментарии)

---
## Инструкции Bufft Assembly
##### Переменные
`INT NAME VALUE` - Создание переменной типа int
```bufft
INT X 5
INT Y 4
```

`STR NAME VALUE` - Создание переменной типа str
```bufft
STR X hello
STR Y world
```
---
##### Арифметика
`ADD NAME NAME2` - Добавляет значение переменной `NAME2` к переменной `NAME` (только int)
```bufft
INT X 5
INT Y 2
ADD X Y
```
`SUB NAME NAME2` - Отнимает значение переменной `NAME2` от переменной `NAME` (только int)
```bufft
INT X 5
INT Y 2
SUB X Y
```
`MUL NAME NAME2` - Умножает значение переменной `NAME` на переменную `NAME2` (только int)
```bufft
INT X 5
INT Y 2
MUL X Y
```
`DIV NAME NAME2` - Делит значение переменной `NAME2` на переменную `NAME` (только int)
```bufft
INT X 5
INT Y 2
DIV X Y
```
Первая указанная переменная будет изменена после проведения арифметических операций

---
##### Вывод
`PUB INT VALUE` - Вывод переменной типа int
```bufft
INT X 5
PUB INT X
```
`PUB STR VALUE` - Вывод переменной типа str
```bufft
STR X Hello!
PUB STR X
```
`PUB VAL VALUE` - Вывод простого текста
```bufft
INT X 5
PUB VAL Число: 
PUB INT X
```
`PUB NL` - Перенос строки
```bufft
INT X 5
PUB VAL Число:
PUB NL
PUB INT X
```
---
##### Ввод
`REA INT VALUE` - Ввод значения типа int в консоли
```bufft
PUB VAL Введите число: 
REA INT X
PUB INT X
```
`REA STR VALUE` - Ввод значения типа str в консоли
```bufft
PUB VAL Введите число: 
REA STR X
PUB STR X
```
---
##### Условия
`MIF NAME NAME2` - Если значение переменной `NAME` > `NAME2`, выполняет ниже написанный код
```bufft
INT X 14
INT Y 5
MIF X Y
PUB INT X
PUB VAL больше
PUB INT Y
PUB VAL на
SUB X Y
PUB INT X
END         ; Обязательно!!
```
`ELSE` - Если значение переменной `NAME` < `NAME2`, выполняет ниже написанный код
```bufft
INT X 3
INT Y 9
MIF X Y     ; Обязательно!!
PUB INT X
PUB VAL больше
PUB INT Y
PUB VAL на
SUB X Y
PUB INT X
ELSE        ; <-----
PUB INT X
PUB VAL меньше
PUB INT Y
END         ; Обязательно!!
```