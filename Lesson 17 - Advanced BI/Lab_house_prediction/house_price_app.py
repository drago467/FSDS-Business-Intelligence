import streamlit as st
import pandas as pd
import numpy as np
import joblib

from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# Load model & data
@st.cache_data
def load_model():
    df = pd.read_csv('house_prices_hanoi_50000.csv')
    X = df[['square_meters', 'num_floors', 'num_bedrooms', 'num_bathrooms',
            'garage', 'main_road', 'near_school', 'near_market',
            'location', 'year_built']]
    y = df['price']

    preprocessor = ColumnTransformer([
        ('location', OneHotEncoder(handle_unknown='ignore'), ['location'])
    ], remainder='passthrough')

    model_pipeline = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('regressor', RandomForestRegressor(n_estimators=100, random_state=42))
    ])

    model_pipeline.fit(X, y)
    return model_pipeline, df

model, df = load_model()

# Streamlit UI
st.title("🏠 Dự Đoán Giá Nhà Hà Nội")

st.sidebar.header("Thông tin ngôi nhà")

square_meters = st.sidebar.slider('Diện tích (m2)', 20, 300, 100)
num_floors = st.sidebar.slider('Số tầng', 1, 5, 3)
num_bedrooms = st.sidebar.slider('Số phòng ngủ', 1, 5, 3)
num_bathrooms = st.sidebar.slider('Số phòng tắm', 1, 3, 2)
garage = st.sidebar.selectbox('Có chỗ để ô tô?', ['Không', 'Có'])
main_road = st.sidebar.selectbox('Nhà mặt đường?', ['Không', 'Có'])
near_school = st.sidebar.selectbox('Gần trường học?', ['Không', 'Có'])
near_market = st.sidebar.selectbox('Gần chợ?', ['Không', 'Có'])
location = st.sidebar.selectbox('Địa chỉ', sorted(df['location'].unique()))
year_built = st.sidebar.slider('Năm xây dựng', 1990, 2023, 2015)

# Convert input
input_data = pd.DataFrame({
    'square_meters': [square_meters],
    'num_floors': [num_floors],
    'num_bedrooms': [num_bedrooms],
    'num_bathrooms': [num_bathrooms],
    'garage': [1 if garage == 'Có' else 0],
    'main_road': [1 if main_road == 'Có' else 0],
    'near_school': [1 if near_school == 'Có' else 0],
    'near_market': [1 if near_market == 'Có' else 0],
    'location': [location],
    'year_built': [year_built]
})

# Predict
if st.button('Dự đoán giá nhà'):
    predicted_price = model.predict(input_data)[0]
    st.success(f"🏡 Giá dự đoán: {predicted_price:,.0f} VND")
