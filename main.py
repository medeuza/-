import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


data = pd.read_csv("bike_buyers.csv")
"1 Data Cleanup"
#удаляем "ненужные" строчки (где встречается хоть одно пустое значение)
data = data.dropna(axis=0)
# меняю все float64(), object() на int64(), string()
data = data.astype({'Marital Status': 'string', 'Gender': 'string', 'Income': 'int64', 'Children': 'int64', 'Education': 'string', 'Occupation': 'string', 'Home Owner': 'string', 'Cars': 'int64', 'Commute Distance': 'string', 'Region': 'string', 'Age': 'int64', 'Purchased Bike': 'string'})

st.title("Title")
st.header("here is dataset")
st.dataframe(data)

"2 Detailed overview"
# Готовлю данные с разделением (м/ж) для популяционной пирамиды
male = data[data['Gender'] == "Male"].groupby("Age").count()
male["ID"].to_numpy()
ageM = male.index.to_numpy()


female = data[data['Gender'] == "Female"].groupby("Age").count()
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



st.pyplot(fig)
