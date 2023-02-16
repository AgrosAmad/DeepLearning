# Load Data
from tensorflow.keras.datasets import mnist
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# Network Architecture
from tensorflow import keras 
from tensorflow.keras import layers 
model = keras.Sequential([layers.Dense(512, activation="relu"), layers.Dense(10, activation="softmax")])

# Compilation step
model.compile(optimizer="rmsprop", 
              loss="sparse_categorical_crossentropy",
              metrics=["accuracy"])

# Processing image data
train_images = train_images.reshape((60000, 28*28))
train_images = train_images.astype("float32")/255
test_images = test_images.reshape((10000, 28*28))
test_images = test_images.astype("float32")/255

# Fitting the model
model.fit(train_images, train_labels, epochs=5, batch_size=128)

# Make prefictions
test_digits = test_images[0:10]
predictions = model.predict(test_digits)
print(predictions[0])
