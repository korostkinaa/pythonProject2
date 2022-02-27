name = "Элина"
age = 19
print(name, age)
name5 = (name + " " + name + " " + name + " " + name + " " + name)
name6 = name5 * 5
print(name5, name6)
question_name = str(input("Как вас зовут?"))
try:
    question_age = int(input("Сколько вам лет?"))
except ValueError:
    print("Это строка, а нужно число. Попробуйте еще раз! ")
if question_age > 150 or question_age < 0:
    print("Укажите свой истинный возраст ")
    question_age = int(input("Сколько вам лет?"))
print("Привет, " + question_name + "!")
if question_age > 40:
    print("А вы выглядите моложе:) ")
else:
    print("Да у вас еще вся жизнь впереди")
print("Ваше имя наоборот: ", question_name[::-1])
n=(question_name[1:])
m=(n[:-1])
print(m[::-1], question_name[:1],  question_name[::-1], question_name[-3:], question_name[:5]) #первым я здесь вывела с 2 по предпоследний символ наоборот
summa = 0
umno = 1
for i in range(2):
    summa = summa + int(str(question_age)[i])
    umno =umno * int(str(question_age)[i])
print(len(question_name), summa, umno)
name = name.upper()
user_math = input(question_name + " сколько будет 2+2*2")
if user_math == "6":
    print("Правильно!")
else:
    print("У вас ошибка, Попробуйте снова!")
