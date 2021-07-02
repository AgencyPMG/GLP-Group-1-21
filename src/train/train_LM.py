import random
import pandas as pd
import numpy as np
import tensorflow as tf

from nltk.tokenize import TweetTokenizer 
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

from sklearn.preprocessing import LabelEncoder


EMBEDDING_DIM = 50
SPLIT_SIZE = 0.1
BATCH_SIZE = 512
DATA_PATH = 'src/train/data/ralph_lauren_retail_feed.csv'
EMBEDDINGS_PATH = 'src/train/data/glove.6b.50d.txt'

def train():
    """ Train language model for description """
    random.seed(1)

    # Language preprocessing definitions
    lemma = WordNetLemmatizer()
    nltk_tok = TweetTokenizer()
    
    flatten = lambda l: np.array([x for sub in l for x in sub])
    filter_words = lambda seq: [lemma.lemmatize(word) for word in seq if word not in stopwords.words('english')]

    # load data
    data = pd.read_csv(DATA_PATH)
    data = data[['description', 'product_type']].dropna()
    raw_seqs = data.description.tolist()
    labels = data.product_type.tolist()

    idx = [i for i in range(len(raw_seqs))]
    train_idx = random.sample(idx, round(SPLIT_SIZE * len(raw_seqs)))
    test_idx = list(set(idx) - set(train_idx))

    # make list of tuples
    patterns = np.array([
        [' '.join(nltk_tok.tokenize(seq)), label]
        for seq, label in zip(raw_seqs, labels)
    ])

    patterns = np.apply_along_axis(filter_words, 0, patterns)

    train_patterns = patterns[train_idx, :]
    test_patterns = patterns[test_idx, :]

    X_tokenizer = Tokenizer(oov_token="<OOV>")
    X_tokenizer.fit_on_texts(train_patterns[:, 0])

    X_train = X_tokenizer.texts_to_sequences(train_patterns[:, 0])
    X_train = pad_sequences(X_train, padding='post')

    y_enc = LabelEncoder()
    y_train = y_enc.fit_transform(train_patterns[:, 1])
    y_train = np.expand_dims(y_train, 1)


    X_test = X_tokenizer.texts_to_sequences(test_patterns[:, 0])
    X_test = pad_sequences(X_test, padding='post')

    y_test = y_enc.fit_transform(test_patterns[:, 1])
    y_test = np.expand_dims(y_test, 1)

    classes = len(y_enc.classes_)

    vocab_size = len(X_tokenizer.word_index) + 1

    train_data = tf.data.Dataset.from_tensor_slices((X_train, y_train))
    train_data = train_data.batch(BATCH_SIZE)

    test_data = tf.data.Dataset.from_tensor_slices((X_test, y_test))
    test_data = test_data.batch(y_train.shape[0])

    ## Initialize GloVe weights
    embeddings_index = {}
    with open(EMBEDDINGS_PATH) as f:
        for line in f:
            values = line.split()
            word = values[0]
            coefs = np.asarray(values[1:], dtype='float32')
            embeddings_index[word] = coefs

    embeddings_matrix = np.zeros((vocab_size, EMBEDDING_DIM))
    for word, i in X_tokenizer.word_index.items():
        embedding_vector = embeddings_index.get(word)
        if embedding_vector is not None:
            embeddings_matrix[i] = embedding_vector

    ## Training 
    model = tf.keras.Sequential([
        tf.keras.layers.Embedding(vocab_size, EMBEDDING_DIM, weights=[embeddings_matrix], mask_zero=True),
        tf.keras.layers.Dropout(0.4),  
        tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(1024, return_sequences=True)),
        tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(1024)),
        tf.keras.layers.Dropout(0.4), 
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(64, activation="relu"),
        tf.keras.layers.Dropout(0.5),
        tf.keras.layers.Dense(classes, activation='softmax')
    ])

    model.compile(loss="categorical_crossentropy", optimizer="adam", metrics="accuracy")

    history = model.fit(train_data, epochs=50)

    ## Save model
    model.save_weights('language_model_weights')

    with open('tokenizer.pickle', 'wb') as handle:
        pickle.dump(X_tokenizer, handle, protocol=pickle.HIGHEST_PROTOCOL)

    with open('label_encoder', 'wb') as handle:
        pickle.dump(y_enc, handle, protocol=pickle.HIGHEST_PROTOCOL)


if __name__ == '__main__':
    train()
