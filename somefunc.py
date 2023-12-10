import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("bike_buyers.csv")
data2 = data.dropna(axis=0) #удаляем "ненужные" строчки (где встречается хоть одно пустое значение)
data2.info()
data3 = data2.astype({'Marital Status': 'string', 'Gender': 'string', 'Income': 'int64', 'Children': 'int64', 'Education': 'string', 'Occupation': 'string', 'Home Owner': 'string', 'Cars': 'int64', 'Commute Distance': 'string', 'Region': 'string', 'Age': 'int64', 'Purchased Bike': 'string'})
data3.info()

fig, axs = plt.subplots(1, 3, figsize=(15, 5))

custom_colors = ['magenta', 'blueviolet', 'indigo', 'blueviolet', 'darkorchid']

# Построение круговой диаграммы для каждого подграфика
axs[0].pie(data3['Occupation'].value_counts().values, labels=data3['Occupation'].value_counts().index, autopct='%1.1f%%', startangle=90, colors = custom_colors)
axs[1].set_title('Cars')
axs[0].set_title('Occupation')

axs[1].pie(data3['Cars'].value_counts().values, labels=data3['Cars'].value_counts().index, autopct='%1.1f%%', startangle=90, colors = custom_colors)
axs[1].set_title('Cars')

axs[2].pie(data3['Commute Distance'].value_counts().values, labels=data3['Commute Distance'].value_counts().index, autopct='%1.1f%%', startangle=90, colors = custom_colors)
axs[2].set_title('Commute Distance')
plt.savefig('1.png')
plt.show()
plt.figure(figsize=(10, 5))


# Готовлю данные с разделением (м/ж) для популяционной пирамиды
male = data3[data3['Gender'] == "Male"].groupby("Age").count()
male["ID"].to_numpy()
ageM = male.index.to_numpy()

female = data3[data3['Gender'] == "Female"].groupby("Age").count()
female["ID"].to_numpy()
ageF = female.index.to_numpy()

# Генерируем искусственные данные для популяционной пирамиды
ageM = male.index.to_numpy()
ageF = female.index.to_numpy()
male_population = male["ID"].to_numpy()
female_population = female["ID"].to_numpy()

# Инвертируем данные о мужском населении, чтобы отобразить их на левой стороне пирамиды
male_population = -male_population

fig, ax = plt.subplots(figsize=(10, 8))

# Создаем график популяционной пирамиды
ax.barh(ageM, male_population, height=0.5, label='Male', color='mediumblue')
ax.barh(ageF, female_population, height=0.5, label='Female', color='magenta')

# ax.hist(ageM, male_population, height=0.5, label='Male', color='mediumblue',orientation='horizontal',bins=10)
# ax.hist(ageF, female_population, height=0.5, label='Female', color='magenta',orientation='horizontal',bins=10)


# Добавляем центральную линию для справки
ax.vlines(0, ymin= min(ageM[0], ageF[0]), ymax= max(ageM[-1], ageF[-1]), color='gray')

# Возвращаем ось x для мужчин, чтобы показать положительные значения
ax.set_xticks([ -25, 0, 25])
ax.set_xticklabels([-25, 0, 25])

ax.set_yticks(np.arange(25, 90, 5))
ax.set_yticklabels(np.arange(25, 90, 5))

# Устанавливаем метки
ax.set_xlabel('Number of people')
ax.set_ylabel('Age')
ax.set_title('Age distribution')

ax.legend(loc='upper right') # В правом вверхнем углу Males/Females

ax.grid(True, linestyle='--', which='both', color='gray', alpha=0.7) # Создаю сетку
plt.savefig('2.png')
plt.show() # Показываем график

data3['PeopleNumber'] = data3.apply(lambda x: 2 + x["Children"] if x["Marital Status"] == "Married" else 1+ x["Children"], axis=1)
data3["Income per person"] = data3.apply(lambda x: x["Income"] / x["PeopleNumber"], axis=1)
import random
def rep(x):
  if not(isinstance(x,str)):
    return x
  if "Miles" in x:
    x = x.replace("Miles", "")
  x=x.replace("+","")
  x=x.split("-")
  if len(x)==1:
    return int(x[0])
  else:
    return  random.random() + random.randint(int(x[0]), int(x[1])-1)
    # return (int(x[0])+int(x[1]))/2

data3["2Commute Distance"] = data3["Commute Distance"].apply(rep)
data3.plot.scatter(x = 'Income per person', y = "2Commute Distance", s = 10, c = data3['Purchased Bike'].apply(lambda x: 'magenta' if x == "Yes" else 'mediumblue'))
plt.savefig('3.png')