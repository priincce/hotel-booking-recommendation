import joblib
from config.paths_config import *
import numpy as np
import warnings
warnings.simplefilter("ignore")
model = joblib.load(MODEL_OUTPUT_PATH)
input = np.array([98, 1, 98, 1, 1, 0, 2, 1, 0, 0]).reshape(1, -1)
prediction = model.predict(input)
print(f"Prediction: {prediction[0]}")
