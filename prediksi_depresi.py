# -*- coding: utf-8 -*-
"""Prediksi Depresi.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1wDruoIgC01jw13caSyOuCrRuPUEsHFca
"""

import pandas as pd
import numpy as np
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense


# Streamlit
st.title('Depression Prediction')
st.write('Fill this form as your current condition')

file = st.file_uploader("Unggah file CSV", type=["csv"])

# Widget input untuk data baru
new_age = st.number_input('**Age**', value=0, min_value=0, max_value=4)
st.write('25-30 tahun: 0')
st.write('30-35 tahun: 1')
st.write('35-40 tahun: 2')
st.write('40-45 tahun: 3')
st.write('45-50 tahun: 4')
st.write('')

new_feeling_sad = st.number_input('**Feeling sad**', value=0, min_value=0, max_value=2)
st.write('Yes: 1 | No: 0 | Sometimes: 2')
st.write('')

new_irritable_towards_people = st.number_input('**Irritable towards people**', value=0, min_value=0, max_value=2)
st.write('Yes: 1 | No: 0 | Sometimes: 2')
st.write('')

new_trouble_sleeping_at_night = st.number_input('**Trouble sleeping at night**', value=0, min_value=0, max_value=2)
st.write('Yes: 1 | No: 0 | Two or more days a week: 2') 
st.write('')

new_problems_concentrating_or_making_decision = st.number_input('**Problems concentrating or making decision**', value=0, min_value=0, max_value=2)
st.write('Yes: 1 | No: 0 | Often: 2')
st.write('')

new_loss_of_appetite = st.number_input('**loss of appetite**', value=0, min_value=0, max_value=2)
st.write('Yes: 1 | No: 0 | Not at all: 2')
st.write('')

new_feeling_of_guilt = st.number_input('**Feeling of guilt**', value=0, min_value=0, max_value=2)
st.write('Yes: 1 | No: 0 | Maybe: 2')
st.write('')

new_problems_of_bonding_with_people = st.number_input('**Problems of bonding with people**', value=0, min_value=0, max_value=2)
st.write('Yes: 1 | No: 0 | Sometimes: 2')
st.write('')

new_suicide_attempt = st.number_input('**Suicide attempt**', value=0, min_value=0, max_value=2)
st.write('Yes: 1 | No: 0 | Not interested to say: 2')
st.write('')

prediksi = st.button('Prediksi')

if file is not None:
    df = pd.read_csv(file)


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
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# Standardize the features
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)


# Build the model
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


# Input data baru
    if prediksi:
        new_data = np.array([[new_age, new_feeling_sad, new_irritable_towards_people, new_trouble_sleeping_at_night, new_problems_concentrating_or_making_decision, new_loss_of_appetite, new_feeling_of_guilt, new_problems_of_bonding_with_people, new_suicide_attempt]])
        new_data_scaled = scaler.transform(new_data)


# Prediksi dengan menggunakan model yang telah dilatih
        predictions = model.predict(new_data_scaled)


#konversi ke yes atau no dengan  threshold (0.5)
        binary_predictions = (predictions > 0.5).astype(int)


# hasil prediksi
        st.write(f"Predicted Probability: {predictions[0][0]}")
        st.write(f"Binary Prediction: {binary_predictions[0][0]}")

        if (binary_predictions==0):
            st.write("Selamat, Anda tidak depresi :)")
        else:
            st.write("Anda terindikasi depresi :(")
