import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator


def train_conv_net():
    """ Train conv net on images """
    #HERE Get data and split it in diferent directories for the train generator
    #HERE Split into train and test to verify that the code works

    #HERE verify addressess and params
    weights_address = 'backend/weights'
    images_address_tr = 'train/images_tr'
    images_address_tr = 'train/images_ts'
    num_classes = 5
    batch_size = 1000
    x_pixels = 150
    y_pixels = 150

    epochs = 150

    train_datagen = ImageDataGenerator(rescale=1./255)

    train_generator = train_datagen.flow_from_directory(
        images_address_tr,
        target_size=(x_pixels,y_pixels),
        batch_size=batch_size,
        class_mode='categorical'
    )

    test_datagen = ImageDataGenerator(rescale=1./255)

    test_generator = train_datagen.flow_from_directory(
        images_address_ts,
        target_size=(x_pixels,y_pixels),
        batch_size=batch_size,
        class_mode='categorical'
    )

    model = tf.keras.models.Sequential([
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
        tf.keras.layers.Flatten(input_shape=(x_pixels,y_pixels,3)),
        tf.keras.layers.Dense(x_pixels, activation='relu'),
        tf.keras.layers.Dense(num_classes, activation='softmax') 
    ])

    model.compile(optimizer='adam', loss='sparse_crossentropy', metrics=['acc'])

    history = model.fit(
        train_generator,
        epochs=epochs
        )

    model.evaluate(test_generator)

    model.load_weights(weights_address)

