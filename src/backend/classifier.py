import tensorflow as tf


class Classifier(tf.keras.models.Model):
    def __init__(self):
        super().__init__()
        self.language_model = tf.keras.Sequential([
            tf.keras.layers.Embedding(vocab_size, EMBEDDING_DIM, weights=[embeddings_matrix], mask_zero=True),
            tf.keras.layers.Dropout(0.7),
            tf.keras.layers.LSTM(512, return_sequences=True),
            tf.keras.layers.Dropout(0.8), 
            tf.keras.layers.LSTM(64),
            tf.keras.layers.Dropout(0.8), 
            tf.keras.layers.Flatten(),
            tf.keras.layers.Dense(128, activation="relu"),
            tf.keras.layers.Dropout(0.6),
            tf.keras.layers.Dense(128, activation="relu"),
            tf.keras.layers.Dropout(0.6),
            tf.keras.layers.Dense(classes, activation='softmax')
        ])

        self.vision_model = tf.keras.Sequential([
            tf.keras.layers.Conv2D(16, (3,3), activation='relu', input_shape=(x_pixels,y_pixels,3)),
            tf.keras.layers.MaxPooling2D(2,2),
            tf.keras.layers.Conv2D(32, (3,3), activation='relu'),
            tf.keras.layers.MaxPooling2D(2,2),
            tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
            tf.keras.layers.MaxPooling2D(2,2),
            tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
            tf.keras.layers.MaxPooling2D(2,2),
            tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
            tf.keras.layers.MaxPooling2D(2,2),
            tf.keras.layers.Flatten(input_shape=(x_pixels, y_pixels, 3)),
            tf.keras.layers.Dense(x_pixels, activation='relu'),
            tf.keras.layers.Dense(NUM_CLASSES, activation='softmax') 
        ])

    def predict():
        pass

    def load_data():
        pass
