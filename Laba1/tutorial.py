# -*- coding: utf-8 -*-
"""
Навчальний tutroial 

Приклади засновані на ресурсі Python v2.7.3 documentation:
    - http://docs.python.org/2/
    - http://oim.asu.kpi.ua/python/docs (дзеркало, доступне з кафедральних комп'ютерів)
"""

# підключення модулей в мові Python виконується за допомогою конструкції import
import random
import math
# для модулів можна вводити аліаси (alias) - прізвиська
import numpy as np
# можна імпортувати окремі функції, а не цілий модуль
from copy import deepcopy

"""
Базові операції в мові Python
-----------------------------

Числові операції
"""
print u"\nЧислові операції:"
print "2+2 =", 2+2        

# конструкція print виводить у стандартний вивід (output) - у консоль       
# print використовує кому "," для декількох аргументів
print "(50-5*6)/4 = ", (50-5*6)/4 

# ділення цілих чисел повертає цілу частину від ділення
print "7/3 = ", 7/3              

# піднесення в степінь
print "2**4 =", 2**4

# при операціях з дійсними та цілими числами, результат приводиться до цілих чисел
print "3 * 3.75 / 1.5 = ", 3 * 3.75 / 1.5   

# В мові Python не використовуються жорстка типізація,
#   тобто не потрібно вказувати тип змінних при їх оголошенні.
# Щоб оголосити змінну просто потрібно приписати їй якесь значення
# Знак рівності (=) використовується для приписування значень змінним
width = 20
height = 5*9
print "width * height = ", width * height

# змінним можна приписувати одне значення одночасно
x = y = z = 0               
print "x =", x, "y =", y, "z =", z

"""
Важливі константи
-----------------

в Python є деякі важливі константи, які дозволяють оперувати границями обчислень
"""
print u"\nВажливі константи:"

# невизначене значення
a = None
print "a = None; a =", a

# нескінченність 
a = float('inf')
print "a = float(inf); a =", a

# булеві константи та логічні операції
print "True and False =", True and False
print "True or False =", True or False
print "not True =", not True


"""
Математичні функції
-------------------

Базові математичні функції знаходяться в модулі math
"""
print u"\nМатематичні функції:"

# константи math.pi та math.e
print "math.pi =", math.pi
print "math.e =", math.e

# math.ceil(x) - повертає найменше ціле число, яке більше х
print "math.ceil(5.3) =", math.ceil(5.3)

# math.floor(x) - повертає найбльше ціле число, яке менше х
print "math.floor(5.3) =", math.floor(5.3)

# math.factorial(x) - повертає факторіал х
print "math.factorial(10) =", math.factorial(10)

# math.isinf(x) - перевіряє, чи х є нескінченністю (inf)
print "math.isinf(float('inf')) =", math.isinf(float('inf'))

# math.exp(x) - повертає e**x (експоненту в степені х)
print "math.exp(2) =", math.exp(2)

# math.log(x[, base]) - повертає логарифм від х за основою base
# за замовчуванням base - основа натурального логарифму
print "math.log(math.e) =", math.log(math.e)

# math.pow(x, y) - підносить х в степінь y
print "math.pow(2, 10) =", math.pow(2, 10)
print "math.pow(2, float(1)/10) =", math.pow(2, float(1)/10)

# math.sqrt(x) - повертає квадратний корінь з х
print "math.sqrt(2) =", math.sqrt(2)

"""
Символьні рядки
---------------

В мові Python для символьних рядків використовуються як одинарні лапки (') 
aбо апостроф, так і подвійні ("). У символьних рядках можна використовувати
особливі символи:
    \n - новий рядок
    \t - символ табуляції
Python не має окремий тип для символьного рядку та для окремого символу.
Тут 'a' та "a" означає одне й те саме - символьний рядок з одного символу "а"
"""
print u"\nСимвольні рядки:"

# приклад простого символьного рядку
print "Hello world!\n"

# символьні рядки можна розбивати по рядках (lines)
# в такому випадку використовується символ "\" у кінці кожного рядка
hello = "This is a rather long string containing\n\
several lines of text just as you would do in C.\n\
    Note that whitespace at the beginning of the line is\
 significant."
print hello

# або можна використовувати потрійні лапки (""") або ('''), щоб ввести довгий рядок
print """This is another long string.
No newline symbols are needed.
"""

# об'єднання рядків виконується за допомогою знаку +
string = 'Good ' + 'day!'
print string

# до окремих елементів рядків (тобто символів) можна діставатись як до елементів масиву
# string[index], де index - індекс, який починається з 0
print "string[0] =", string[0]

# щоб дістатись до підрядка використовується конструкція:
# string[begin:end], де begin - індекс початку підрядка, end - наступний за кінцевим індекс
# таким чином підрядок буде містити (end - begin) символів
print "string[1:4] =", string[1:4]

# щоб вивести підрядок до кінця символьного рядку просто не вказуйте індекс end
print "string[5:] =", string[5:]

"""
На противагу іншим мовам (наприклад, С), символьні рядки в Python не можуть змінюватись
Так, конструкція
    string[0] = 'X'
призведе до помилки:
    TypeError: 'str' object does not support item assignment
"""

# але легко створювати нові символьні рядки з інших рядків
string_2 = string[:5] + 'morning!'
print string_2
string_2 = "Nice " + string[5:8] + " :)"
print string_2

# якщо при індексації підрядків вказується занадто великий або малий індекс, 
# то це не призведе до помилки
print "string[5:100] =", string[5:100]

# індекси можуть бути негативним, тоді вони вказують на позицію з кінця рядку
print "string[-1] =", string[-1]
# останні два символи
print "string[-2:] =", string[-2:]
# все, окрім двох останніх символів
print "string[:-2] =", string[:-2]

# перевести число в рядок
a = 100
print "a = " + str(a)
# запис "a = " + a призведе до помилки

# перевести символьний рядок в число
print "int('10') + float('2.3') =", int('10') + float('2.3')
# переведення int('2.3') призведе до помилки
#   ValueError: invalid literal for int() with base 10: '2.3'

"""
Операції над символьними рядками
--------------------------------

Символьні рядки - це об'єкти класу string тому мають методи цього класу
Щоб переглянути методи класу str, використовуйте конструкцію:
    dir(str)
Щоб переглянути опис конкретного методу, використовуйте конструкцію:
    print str.count.__doc__
Взагалі, кожна сутність в Python є об'єктом (навіть клас або модуль).
А у кожного об'єкту є набір стандартних властивостей. Так властивість __doc__
    використовується для зберігання опису об'єкту
"""
print u"\nОперації над символьними рядками:"

string = "abrAcadAbrA"
print "string =", string

# Метод str.count(sub[, start[, end]]) повертає кількість входжень підрядків sub у рядок str
#   метод враховує регістр символів
print "string.count('a') =", string.count('a')

# Метод str.find(sub[, start[, end]]) повертає перший індекс підрядка sub у рядку str
#   Повертає -1 у випадку коли підрядок не знайдений
print "string.find('rA') =", string.find('rA')

# Метод str.rfind(sub[, start[, end]]) працює як str.find, але шукає з кінця
print "string.rfind('rA') =", string.rfind('rA')

# Метод str.replace(old, new[, count]) замінює всі входження підрядків old на рядки new у рядку str
print "string.replace('rA','Ra') =", string.replace('rA','_Ra_')

# Метод str.split([sep[, maxsplit]]) повертає масив підрякдів (слів) у рядку,
#   які розділені рядком sep (за замовчуванням це пробіл)
print "'Hello world!'.split() =", 'Hello world!'.split()
print "string.split('br') =", string.split('br')

# Метод str.splitlines([keepends]) повертає масив окремих рядків (lines)
wb_quote = """To see the world in a grain of sand,
and to see heaven in a wild flower,
hold infinity in the palm of your hands,
and eternity in an hour.
"""
print "wb_quote.splitlines() =", wb_quote.splitlines()

# для симолів Unicode використовуйте літеру 'u' перед лапками рядків
print u'Вітаємо в курсі Теорія Алгоритмів!'

"""
Списки (або масиви)
-------------------

У мові Python є декілька вбудованих типів даних, що використовуються як
колекції. Серед них списки (lists), словники (dictionaries), кортежі (tuples).
Списки відповідають (динамічним) масивам у мові C. 
"""
print u"\nСписки:"
# визначення списку
list_1 = [1, 2, 3]
print "list_1 =", list_1

# списки можуть містити елементи різних типів...
list_2 = ['spam', 'eggs', 100, 1234]
print "list_2 =", list_2

# ...навіть окремі списки
list_3 = [100, 5.3, 'string', ['apple', 'orange']]
print "list_3 =", list_3

# індексація елементів списку відбувається так само, як і в символьних рядках
# тобто: list[index] або list[begin:end]
print "list_3[1] =", list_3[1]
print "list_3[:2] =", list_3[:2]
print "list_3[1:3] =", list_3[1:3]

# можна об'єднувати списки за допомогою операції "+"
print "list_1 + list_2 = ", list_1 + list_2

# можна робити копії списків або деяких їх частин
print "list_1[1:]*3 + list_2 =", list_1[1:]*3 + list_2

# елементи списків, на відміну від елементів символьних рядків, можна змінювати
list_3[1] = -5.3
print "list_3 =", list_3

# порожний список означаєтся як []
list_0 = []
print "list_0 =", list_0

# якщо прирівняти один список до іншого, то насправді відбудеться зв'язування 
# через посилання, тобто змінні будуть посилатись на один й той самий об'єкт
# у пам'яті
list_4 = list_3
print "list_4 =", list_4
list_3[1] = list_3[1] * 10
print "list_4 =", list_4

# щоб створити нову копію списку використовуйте наступну конструкцію
list_5 = list_3[:]
print "list_5 =", list_5
list_3[1] = list_3[1] * 10
print "list_3 =", list_3
print "list_5 =", list_5

# фрагментам списків можна приписувати значення, таким чином або замінюючи деякі
# елементи списків, або видаляючі фрагменти, якщо приписується порожній список []
list_5[1:3] = ['one element']
print 'list_5 =', list_5
list_5[2:] = []
print 'list_5 =', list_5
list_5[:] = []
print 'list_5 =', list_5

# вбудована функція len() повертає розмір списку або іншої колекції 
# (а також символьних рядків)
print "list_3 =", list_3, "; len(list_3) =", len(list_3)
print "list_3[3] =", list_3[3], "; len(list_3[3]) =", len(list_3[3])
print "list_3[3][0] =", list_3[3][0], "; len(list_3[3][0]) =", len(list_3[3][0])

"""
Операції над списками
---------------------

Всі списки в Python є екземплярами класу list, який має багато корисних методів
для роботи зі списками.
Перелік методів можна подивитись командую: dir(list)
"""
print u"\nОперації над списками:"

# list.append(x) - додає елемент х до списку
list_3.append('appended')
print "list_3 =", list_3

# list.insert(i, x) - вставляє елемент х до списку на позицію i
list_3.insert(1, 'inserted')
print "list_3 =", list_3

# list.remove(x) - видаляє перший елемент зі значенням х зі списку
# якщо такого елементу немає, то це призведе до помилки
list_3.remove('inserted')
print "list_3 =", list_3

# list.pop([i]) - видаляє елемент під індексом і зі списку та повертає його
# якщо i не вказано, то видаляє останній елемент
print "Last element:", list_3.pop(), "; list_3 =", list_3

# list.index(x) - повертає індекс елементу x в списку
print "Index of 'string' in list_3:", list_3.index('string')

# list.count(x) - підраховує кількість входжень елементу х у список
print "Number of 'string' element in list_3:", list_3.count('string')

# list.sort() - сортує елементи списку
list_3.sort()
print "list_3.sort() =", list_3

# list.reverse() - перевертає список 
list_3.reverse()
print "list_3.reverse() =", list_3

# використання списків як стеку
stack = [3, 4, 5]
print "Stack =", stack
stack.append(6)
stack.append(7)
print "Stack =", stack
stack.pop()
stack.pop()
stack.pop()
print "Stack =", stack

"""
У Python списки можна створювати на основі інших списків за допомогою
скорочених конструкцій, які мають вигляд:
    [операція(x) for x in список]
    
Більш загальна форма:
    [операція(x_1, x_2, ...) for x_1 in список_1 for x_2 in список_2 if умова]
    тут є декілька списків, кожен з яких має власну змінну x
    також присутня необов'язкова умова в конструкції if
"""

# повертає квадрати чисел від 0 до 9
squares = [x**2 for x in range(10)]
print "Squares:", squares

# повертає суми елементів двох списків, якщо ці елементи різні
sums = [x+y for x in [1,2,3] for y in [3,1,4] if x != y]
print "Sums:", sums

# повертає матрицю (двовимірний масив), кожен елемент якої є сумою індексів власного рядка та стовпця
matrix = [[x+y for x in range(5)] for y in range(5)]
print "Matrix:", matrix


"""
Умовні оператори
----------------

Головним умовним оператором в Python є конструкція 'if-elif-else'
Вона має таку форму:
    if умова_1:
        набір дій 1
    elif умова_2:
        набір дій 2
    elif умова_3:
        набір дій 3
    else:
        набір дій 4
Частин 'elif' може бути декілька або жодної. Частина 'else' є необов'язковою.
Зверніть увагу на двокрапки після умов. 
Дужки в умовній частині не потрібні. 
Умовна частина може містити в собі складні логічні перевірки, які використовують
логічні оператори and, or, xor, not    
"""
print u"\nУмовні оператори:"

x = random.randint(-10,10)
print "x =", x
if x < 0:
    print "x is negative"
elif x == 0:
    print 'x is Zero'
elif x%2==0 and x>0:
    print 'x is even'
else:
    print 'x is positive'
    
"""
Умовний оператор. 
В деяких мовах програмування (наприклад, в С/C++) є тернарний умовний оператор
вигяду "умова ? дія_1 : дія_2", який можна використовувати всередині рядків коду
В Python такого оператору немає, але замість нього можна використовувати наступну
конструкцію:
    умова and дія_1 or дія_2
Якщо умова має логічне значення True, то виконаєтся та повернеться результат дії_1,
інакше виконаєтсья та повернеться дія_2.
"""
print "x is", x<0 and "negative" or "non-negative"

# але якщо умова є True, а дія_1 дорівнює False, то тоді повернеться дія_2...
print "2 - 2 =", 2-2==0 and 0 or 1

# ...щоб уникнути такої помилки можна використовувати наступний "трюк"
a = []
print "2 - 2 =", (2-2==0 and [0] or [1])[0]
# тобто спочатку на основі потрібного елементу (0 або 1) стоврюється одноелементний
# список, а потім повертається його перший елемент (під індексом 0)

"""
Цикли
-----

У Python є типові циклічні конструкції: for, while

Конструкція while виглядає досить типово:
    while умова:
        набір дій
Дії будуть виконуватись до тих пір, поки умова є істинною (дорівнює True)
"""
print u"\nЦикли:"

# використання циклу while для обрахунку чисел Фібоначчі, які менше 10
# запис a, b = 0, 1 дозволяє в одному рядку приписати змінній a значення 0, 
#   а змінній b = 1
print "Fibonacci numbers lower 100:",
a, b = 0, 1
while b < 100:
    # кома після конструкції print не додає перехід на новий рядок
    print b,
    a, b = b, a+b
print ""
    
"""
Конструкція for є набагато гнучкішоб ніж в таких мовах, як С. Вона має такий вигляд:
    for задання ітератору:
        перелік дій
Ітератором може бути перелік елементів в колекції (списку, словнику, символьному рядку тощо)
або числові значення в певному діапазоні (але які по суті є також елементами колекції - списку)

В циклах while та for можуть використовуватись конструкції:
    break - для передчасного завершення роботи циклу
    continue - для передчасного переходу на нову ітеацію циклу
"""

# використання циклу for для ітерацій по всім елементам списку
print "Elements of list_1:",
for x in list_1:
    print x,
print ""

# використання циклу for для ітерацій по символьному рядку
print "Characters in string:",
for char in string:
    print char,
print ""

# для того щоб дізнатись індекс елементу в колекції використовуйте функцію enumerate()
print "First 5 characters in string:",
for index, char in enumerate(string):
    if index>=5:
        break
    print char,
print ""

"""
Для того щоб ввести звичайний числовий ітератор використовуйте функцію range()
Функція range([start,] stop[, step]) повертає колекцію цілих чисел у
напіввідкритому інтервалі [start, stop) з кроком step. За замовчуванням значення
start=0, step=1.
Все що робить функція range(), це повертає колекцію цілих чисел. А вже потім оператор
for робить ітерації по цій колекції 
"""
print "for i in range(10):",
for i in range(10):
    print i,
print ""

print "for i in range(5,10):",
for i in range(5,10):
    print i,
print ""

print "for i in range(2,10,2):",
for i in range(2,10,2):
    print i,
print ""

# ще один спосіб індексації за допомогою циклу for...
print "Characters in string in reverse order:",
for i in range(len(string)-1,-1,-1):
    print string[i],
print ""

# ...або ще простіше
print "Characters in string in reverse order:",
for i in reversed(range(len(string))):
    print string[i],
print ""

# цикли довзоляють використання конструкції else, в якій описується дія, що
# буде виконуватись у випадку коли робота циклу завершилась, але не за допомогою
# конструкції break

# визначає прості числа в проміжку від 2 до 9
print "\nPrime numbers between 2 and 9:"
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print n, 'equals', x, '*', n/x
            break
    else:
        print n, 'is a prime number'

# для заглушки циклів чи інших конструкцій (функцій, класів) можна використовувати
# конструкцію pass
print "This for loop do nothing. for i in range(10): pass"
for i in range(10):
    pass

"""
Функції
-------

У Python функції визначаються за допомогою ключового слова def:
    def ім'я_функції(аргумент_1, аргумен_2, аргумен_3=значення_3):
        перелік дій в середині функції
        return значення_результату
        
- Перелік аргументів може бути порожнім, але в такому випадку дужки після ім'я функції
повинні стояти все-одно. 
- Тип значення, що повертається, не визначається (в Python немає строгої типізації)
- Функції не обов'язково повинні повертати якесь значення - конструкції return може
не бути.
- Якщо після оголошення функції одразу йде коментар у потрійних лапках, то він
буде використовуватись для документації функції і буде доступний через властивість
__doc__ об'єкту функції (так, функції у Python є також об'єктами!)
"""
print u"\nФункції:"

# функція обрахунку чисел Фібоначчі
def fib(n):
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        # додає в кінець списку нове число
        result.append(a)
        a, b = b, a+b
    return result
    
# Опис функції fib
print "fib function description:", fib.__doc__

# Числа Фібоначчі до 100
print "fib(100) =", fib(100)

"""
Аргументи функцій можуть мати значення за замовчуванням. Більше того, до аргументів
можна звертатись при виклику функцій в довільному порядку, при цьому зазначаючи
ім'я аргументів (keywords). Якщо використовуються, іменовані аргументи можуть йти
тільки після позиційних аргументів.
"""

def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print "-- This parrot wouldn't", action,
    print "if you put", voltage, "volts through it."
    print "-- Lovely plumage, the", type
    print "-- It's", state, "!"
    
print "\nThe Dead Parrot Sketch by Monty Python"
#parrot(1000)                                          # 1 позиційний аргумент
#parrot(voltage=1000)                                  # 1 іменований аргумент
#parrot(voltage=1000000, action='VOOOOOM')             # 2 іменованих аргументи
#parrot(action='VOOOOOM', voltage=1000000)             # 2 іменованих аргументи
#parrot('a million', 'bereft of life', 'jump')         # 3 позиційних аргументи
parrot('a thousand', state='pushing up the daisies')  # 1 позиційний, 1 іменований

# наступні виклики функцій є невірними - призведуть до помилки
#parrot()                     # пропущений обов'язковий аргумент
#parrot(voltage=5.0, 'dead')  # неіменований аргумент після іменованого
#parrot(110, voltage=220)     # дубліковане значення для одного аргументу
#parrot(actor='John Cleese')  # невідомий іменований аргумент

"""
Мова Python включає в себе можливості функціонального програмування, яке засновується
на ламбда-численні (lambda). За допомогою ключового слова lambda можна стоврювати
анонімні (такі, які не мають ім'я) функції

Недоліком таких функцій є те, що вони можуть складатись лише з однієї конструкції,
хоч вона й може бути достатньо складною.

Ламбда-функції мають наступний вигляд:
    lambda аргумент_1, аргумент_2 : дія
Вони повертають результат своєї єдиної дії
"""
f = lambda a,b: a+b
print "f(2,3) =", f(2,3)

# можна навіть не присвоювати ламбда-функцію якійсь змінній, а відразу виконувати її виклик
print "(lambda a,b: a*b)(2,3) =", (lambda a,b: a*b)(2,3)

"""
Комплексний приклад ламбда-функцій:
    lambda n: filter(lambda x: x%2 and x%3, range(n))

    Ця функція повертає список цілих чисел в інтервалі [0;n), які
    не діляться без остачі на 2 або 3
"""
f = lambda n: filter(lambda x: x%2 and x%3, range(n))
print "Numbers in range(20) that are not divided by 2 or 3:", f(20)