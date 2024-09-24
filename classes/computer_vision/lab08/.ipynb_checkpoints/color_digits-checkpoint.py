import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

# Load MNIST dataset
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

# Preprocess data
x_train = x_train.astype('float32') / 255.0
x_test = x_test.astype('float32') / 255.0
x_train = x_train.reshape(-1, 28, 28, 1)
x_test = x_test.reshape(-1, 28, 28, 1)

# Define the autoencoder model
input_img = keras.Input(shape=(28, 28, 1))

# Encoder
x = layers.Conv2D(32, (3, 3), activation='relu', padding='same')(input_img)
x = layers.MaxPooling2D((2, 2), padding='same')(x)
x = layers.Conv2D(64, (3, 3), activation='relu', padding='same')(x)
x = layers.MaxPooling2D((2, 2), padding='same')(x)
encoded = layers.Flatten()(x)

# Decoder
x = layers.Dense(7 * 7 * 64, activation='relu')(encoded)
x = layers.Reshape((7, 7, 64))(x)
x = layers.Conv2DTranspose(64, (3, 3), strides=(2, 2), activation='relu', padding='same')(x)
x = layers.Conv2DTranspose(32, (3, 3), strides=(2, 2), activation='relu', padding='same')(x)
decoded = layers.Conv2D(3, (3, 3), activation='sigmoid', padding='same')(x)

autoencoder = keras.Model(input_img, decoded)

# Compile the model
autoencoder.compile(optimizer='adam', loss='mse')

# Train the autoencoder
autoencoder.fit(x_train, x_train, epochs=10, batch_size=32, validation_data=(x_test, x_test))

# Colorization logic (example)
def colorize_digit(image, label):
    if label % 2 == 0:  # Even
        color = [0, 1, 0]  # Green
    else:  # Odd
        color = [1, 0, 0]  # Red
    colored_image = image * color
    return colored_image

# Test and visualize
reconstructed_images = autoencoder.predict(x_test)
for i in range(10):
    original_image = x_test[i].reshape(28, 28)
    reconstructed_image = reconstructed_images[i]
    colored_image = colorize_digit(reconstructed_image, y_test[i])
    # Display original, reconstructed, and colored images
