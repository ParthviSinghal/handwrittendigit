from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
import joblib
import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv('dataset.csv')
X = df.drop('label', axis=1).values
y = df['label'].values

# Preprocess data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split data
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Train model
classifier = SVC(kernel='linear', gamma='auto')
classifier.fit(X_train, y_train)

# Save the model
joblib.dump(classifier, 'digit_recognition_model.pkl')

# Evaluate model
y_pred = classifier.predict(X_test)
print(f'Accuracy: {accuracy_score(y_test, y_pred)}')
