import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load model
model = joblib.load('model/titanic_model.joblib')

st.title('🚢 Titanic Survival Prediction App')

st.sidebar.header('🧑‍💼 Passenger Information')

# Inputs
Pclass = st.sidebar.selectbox('Ticket Class (1 = 1st, 2 = 2nd, 3 = 3rd)', [1, 2, 3])
Sex = st.sidebar.selectbox('Sex', ['male', 'female'])
Age = st.sidebar.slider('Age', 0, 100, 30)
SibSp = st.sidebar.slider('Number of Siblings/Spouses Aboard', 0, 10, 0)
Parch = st.sidebar.slider('Number of Parents/Children Aboard', 0, 10, 0)
Fare = st.sidebar.slider('Passenger Fare', 0.0, 600.0, 32.0)
Embarked = st.sidebar.selectbox('Port of Embarkation', ['S', 'C', 'Q'])
Title = st.sidebar.selectbox('Title', ['Mr', 'Mrs', 'Miss', 'Master', 'Other'])

# Mapping encoding
Sex = 1 if Sex == 'male' else 0
Embarked = {'S': 2, 'C': 0, 'Q': 1}[Embarked]
Title = {'Mr': 2, 'Mrs': 3, 'Miss': 1, 'Master': 0, 'Other': 4}[Title]

# Predict button
if st.button('Predict Survival'):
    # Prepare data
    input_data = pd.DataFrame([[Pclass, Sex, Age, SibSp, Parch, Fare, Embarked, Title]],
                              columns=['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked', 'Title'])

    # Prediction
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][prediction]

    result = '🟢 Survived' if prediction == 1 else '🔴 Did not survive'

    st.subheader('Prediction Result:')
    st.markdown(f'### {result}')
    st.write(f'Prediction Confidence: **{probability * 100:.2f}%**')
