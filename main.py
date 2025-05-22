#Контрольная работа
#Шашков Никита х-71
#Уровень A
import pandas as pd
import matplotlib.pyplot as plt

#Задача 1
df_excel =pd.read_excel('Книга1.xlsx')
print(df_excel)

#Задача 2
df_excel =pd.read_excel('Книга1.xlsx')
print(df_excel.head(5))

#Задача 3
x = [1,2,3,4,5]
y = [2,4,1,3,5]

plt.bar(x,y)

plt.title('График из Excel')
plt.xlabel('Ось X')
plt.ylabel('Ось Y')
plt.grid(False)

plt.show()