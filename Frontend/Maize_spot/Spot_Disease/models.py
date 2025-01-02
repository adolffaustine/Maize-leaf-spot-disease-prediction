from django.db import models
import keras
from tensorflow import image
import numpy as np

class Maize(models.Model):
    maize_image = models.ImageField(upload_to="maizes")
    disease_name = models.CharField(max_length=255, blank=True)

    def save(self, *args, **kwargs):
        # Load the Keras model
        ml_model = keras.models.load_model('./ml_model/trained_model.keras')

        # Preprocess the image before feeding it into the model
        img = image.load_img(self.maize_image.path, target_size=(224, 224))  # Adjust target size as needed
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array /= 255.  # Normalize the image data

        # Make prediction
        prediction = ml_model.predict(img_array)

        # Assuming the model returns a one-hot encoded vector or probabilities,
        # you may need to decode it to get the actual disease name.
        # For example, if the model returns probabilities for different classes:
        classes = ['Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot',
 'Corn_(maize)___Common_rust_',
 'Corn_(maize)___Northern_Leaf_Blight',
 'Corn_(maize)___healthy']  # Define your class names
        predicted_class_index = np.argmax(prediction)
        self.disease_name = classes[predicted_class_index]

        # Save the instance
        super().save(*args, **kwargs)

    def __str__(self):
        return self.disease_name
