import joblib
import numpy as np

# wczytanie modelu
model = joblib.load("model_v1.joblib")

sample = np.array([[5.1, 3.5, 1.4, 0.2]])

prediction = model.predict(sample)

print("Predykcja klasy:", prediction)