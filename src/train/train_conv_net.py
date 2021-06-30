import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator


def train_conv_net():
    """ Train conv net on images """

    #HERE verify addressess
    weights_address = 'backend/weights'
    images_address = 'train/images'

    #HERE verify image params
    train_datagen = ImageDataGenerator(
        rescale=1./255,
        horizontal_flip=True,
        rotation_range=20,
        width_shift_range=0.15,
        height_shift_range=0.15,
        fill_mode='wrap'
    )

    #HERE verify params
    train_generator = train_datagen.flow_from_directory(
        images_address,
        target_size=(150,150),
        batch_size=10,
        class_mode='binary'
    )

    #HERE check shape of network and number of layers
    model = tf.keras.models.Sequential([
        tf.keras.layers.Conv2D(16, (3,3), activation='relu', input_shape=(150,150,3)),
        tf.keras.layers.MaxPooling2D(2,2),
        tf.keras.layers.Conv2D(32, (3,3), activation='relu'),
        tf.keras.layers.MaxPooling2D(2,2),
        tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
        tf.keras.layers.MaxPooling2D(2,2),
        tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
        tf.keras.layers.MaxPooling2D(2,2),
        tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
        tf.keras.layers.MaxPooling2D(2,2),
        tf.keras.layers.Flatten(input_shape=(150,150,3)),
        tf.keras.layers.Dense(150, activation='relu'),
        tf.keras.layers.Dense(1, activation='sigmoid')  # two classes, so same as softmax
    ])

    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['acc'])

    model.fit(train_generator)

    model.load_weights(weights_address)

