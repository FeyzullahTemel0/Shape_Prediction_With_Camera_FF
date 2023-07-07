import cv2
import numpy as np
import urllib.request
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input, decode_predictions


model = ResNet50(weights='imagenet')


cap = cv2.VideoCapture(0)


labels = np.array(urllib.request.urlopen('https://raw.githubusercontent.com/anishathalye/imagenet-simple-labels/master/imagenet-simple-labels.json').read().decode().splitlines())

while True:
    ret, frame = cap.read()
    img = cv2.resize(frame, (224, 224))
    img = np.expand_dims(img, axis=0)
    img = preprocess_input(img)
    predictions = model.predict(img)
    predicted_label = labels[np.argmax(predictions)]
  
    cv2.putText(frame, "Shape: {}".format(predicted_label), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
    cv2.imshow('Camera', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
