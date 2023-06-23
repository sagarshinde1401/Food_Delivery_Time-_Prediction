#Application for Prediction of Time for the Food Delivery
import numpy as np
from keras.models import load_model

model = load_model('Time_Predict.h5')
print("Food Delivery Time Prediction")
a = int(input("Age of Delivery Partner: "))
b = float(input("Ratings of Previous Deliveries: "))
c = int(input("Total Distance: "))

features = np.array([[a, b, c]])
print("Predicted Delivery Time in Minutes = ", model.predict(features))