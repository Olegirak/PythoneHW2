# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать. Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.
s = int(input("Введите сумму двух чисел X и Y  "))
p = int(input("Введите произведение двух чисел X и Y  "))
i=0
for i in range (s//2+1):
    x = i
    y = s-i
    if x*y == p:
        print (f" Искомые числа {x} и {y}")
   
    