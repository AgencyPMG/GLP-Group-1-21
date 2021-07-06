import sys
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator

def train_conv_net():
    """ Train conv net on images """
    #HERE verify addressess and params
    NUM_CLASSES = 5
    BATCH_SIZE = 1024

    weights_address = 'src/backend/weights'
    images_address_tr = 'src/train/data/training'
    images_address_ts = 'src/train/data/testing'
    x_pixels = 400
    y_pixels = 550

    epochs = 150

    train_datagen = ImageDataGenerator(rescale=1./255)
    
    sys.stdout.write('Generating train files\n')
    
    train_generator = train_datagen.flow_from_directory(
        images_address_tr,
        target_size=(x_pixels,y_pixels),
        batch_size=BATCH_SIZE,
        class_mode='categorical'
    )

    test_datagen = ImageDataGenerator(rescale=1./255)
    
    sys.stdout.write('Generating test files\n')

    test_generator = train_datagen.flow_from_directory(
        images_address_ts,
        target_size=(x_pixels,y_pixels),
        batch_size=BATCH_SIZE,
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
        tf.keras.layers.Dense(NUM_CLASSES, activation='softmax') 
    ])

    model.compile(optimizer='adam', loss='sparse_crossentropy', metrics=['acc'])

    sys.stdout.write('Training...\n')

    history = model.fit(
        train_generator,
        epochs=epochs
        )
    sys.stdout.write('Training done!!!\n')

    acc = model.evaluate(test_generator)

    # sys.stdout.write(model.metrics_names)
    sys.stdout.write(acc)

    model.save_weights(weights_address)

if __name__ =='__main__':
    train_conv_net()