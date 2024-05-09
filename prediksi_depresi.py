# -*- coding: utf-8 -*-
"""Prediksi Depresi.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1wDruoIgC01jw13caSyOuCrRuPUEsHFca
"""

import pandas as pd
import numpy as np
import streamlit as st

from google.colab import files
files.download('depressionData.csv')
df = pd.read_csv("depressionData.csv")


# Split the data into features (X) and target variable (y)
X = df.drop(columns=['Timestamp', 'Depressed'])

X['Age'] = X['Age'].map({'25-30': 0, '30-35': 1, '35-40': 2, '40-45': 3, '45-50': 4})
X['Feeling sad'] = X['Feeling sad'].map({'Yes': 1, 'No': 0, 'Sometimes': 2})
X['Irritable towards people'] = X['Irritable towards people'].map({'Yes': 1, 'No': 0, 'Sometimes': 2})
X['Trouble sleeping at night'] = X['Trouble sleeping at night'].map({'Yes': 1, 'No': 0, 'Two or more days a week': 2})
X['Problems concentrating or making decision'] = X['Problems concentrating or making decision'].map({'Yes': 1, 'No': 0, 'Often': 2})
X['loss of appetite'] = X['loss of appetite'].map({'Yes': 1, 'No': 0, 'Not at all': 2})
X['Feeling of guilt'] = X['Feeling of guilt'].map({'Yes': 1, 'No': 0, 'Maybe': 2})
X['Problems of bonding with people'] = X['Problems of bonding with people'].map({'Yes': 1, 'No': 0, 'Sometimes': 2})
X['Suicide attempt'] = X['Suicide attempt'].map({'Yes': 1, 'No': 0, 'Not interested to say': 2})

y = df['Depressed'].map({'Yes': 1, 'No': 0})


# Split the data into training and testing sets
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# Standardize the features
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


# Build the model
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

model = Sequential([
    Dense(128, activation='relu', input_shape=(X_train.shape[1],)),
    Dense(64, activation='relu'),
    Dense(32, activation='relu'),
    Dense(10, activation='softmax'),
    Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])


# Train the model
model.fit(X_train, y_train, epochs=50, batch_size=64, validation_data=(X_test, y_test), verbose=2)


# Evaluate the model
loss, accuracy = model.evaluate(X_test, y_test, verbose=0)


# Streamlit
st.title('Depression Prediction')
st.write('Fill this form as your current condition')


# Widget input untuk data baru
new_age = st.selectbox('Age',['25-30','30-35','35-40','40-45','45-50'])
new_feeling_sad = st.selectbox('Feeling sad',['Yes','No','Sometimes'])
new_irritable_towards_people = st.selectbox('Irritable towards people',['Yes','No','Sometimes'])
new_trouble_sleeping_at_night = st.selectbox('Trouble sleeping at night',['Yes','No','Two or more days a week'])
new_problems_concentrating_or_making_decision = st.selectbox('Problems concentrating or making decision',['Yes','No','Often'])
new_loss_of_appetite = st.selectbox('loss of appetite',['Yes','No','Not at all'])
new_feeling_of_guilt = st.selectbox('Feeling of guilt',['Yes','No','Maybe'])
new_problems_of_bonding_with_people = st.selectbox('Problems of bonding with people',['Yes','No','Sometimes'])
new_suicide_attempt = st.selectbox('Suicide attempt',['Yes','No','Not interested to say'])

st.button('Prediksi')


# Input data baru
if st.button('Prediksi'):
  new_data = np.array([[new_age, new_feeling_sad, new_irritable_towards_people, new_trouble_sleeping_at_night, new_problems_concentrating_or_making_decision, new_loss_of_appetite, new_feeling_of_guilt, new_problems_of_bonding_with_people, new_suicide_attempt]])
  new_data_scaled = scaler.transform(new_data)


# Prediksi dengan menggunakan model yang telah dilatih
  predictions = model.predict(new_data_scaled)


#konversi ke yes atau no dengan  threshold (0.5)
  binary_predictions = (predictions > 0.5).astype(int)


# hasil prediksi
  st.write(f"Predicted Probability: {predictions[0][0]}")
  st.write(f"Binary Prediction: {binary_predictions[0][0]}")