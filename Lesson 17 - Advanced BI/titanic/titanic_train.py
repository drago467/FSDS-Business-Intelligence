import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
import joblib

# Load data
train_df = pd.read_csv('data/train.csv')

# Feature Engineering
train_df['Title'] = train_df['Name'].str.extract(' ([A-Za-z]+)\.', expand=False)
train_df['Title'] = train_df['Title'].replace(['Mlle', 'Ms'], 'Miss').replace(['Mme'], 'Mrs')
train_df['Title'] = train_df['Title'].apply(lambda x: x if x in ['Mr', 'Mrs', 'Miss', 'Master'] else 'Other')

train_df['Sex'] = LabelEncoder().fit_transform(train_df['Sex'])
train_df['Embarked'] = train_df['Embarked'].fillna('S')
train_df['Embarked'] = LabelEncoder().fit_transform(train_df['Embarked'])
train_df['Title'] = LabelEncoder().fit_transform(train_df['Title'])

train_df['Age'] = train_df['Age'].fillna(train_df['Age'].median())
train_df['Fare'] = train_df['Fare'].fillna(train_df['Fare'].median())

# Features & Target
features = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked', 'Title']
X = train_df[features]
y = train_df['Survived']

# Train Model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

# Save model
joblib.dump(model, 'model/titanic_model.joblib')

# Simple test accuracy
y_pred = model.predict(X)
print(f'Train Accuracy: {accuracy_score(y, y_pred):.4f}')
