import numpy as np
import pickle

import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
from nltk.tokenize.casual import TweetTokenizer
from nltk.stem import WordNetLemmatizer

class Classifier(tf.keras.models.Model):
    """
    Classifier that abstracts TF model to make predictions
    """
    def __init__(self, model_dir, embedding_dim=50):
        super().__init__()
        with open(model_dir + '/tokenizer.pickle', 'rb') as handle:
            self.tokenizer = pickle.load(handle)

        with open(model_dir + '/label_encoder.pickle', 'rb') as handle:
            self.label_encoder = pickle.load(handle)

        self.tweeter = TweetTokenizer()
        self.lemma = WordNetLemmatizer()
        self.vocab_size = len(self.tokenizer.word_index)
        self.embedding_dim = embedding_dim

        self.language_model = tf.keras.Sequential([
            tf.keras.layers.Embedding(self.vocab_size, self.embedding_dim, mask_zero=True),
            tf.keras.layers.Dropout(0.7),
            tf.keras.layers.LSTM(512),
            tf.keras.layers.Dropout(0.7), 
            tf.keras.layers.Flatten(),
            tf.keras.layers.Dense(64, activation="relu"),
            tf.keras.layers.Dropout(0.6),
            tf.keras.layers.Dense(len(self.label_encoder.classes_), activation='softmax')
        ])

        self.language_model.load_weigts(model_dir + '/language_model_weights')
        
    def _process_seq(self, raw_seq):
        out_seq = [self.lemma.lemmatize(word) for word in seq if word not in stopwords.words('english')]
        out_seq = self.tokenizer.texts_to_sequences(out_seq)
        out_seq = pad_sequences(out_seq, padding='post')
        return out_seq[0]
        
    def predict(self, raw_seq):
        """
        Return dict of schema
        {
            class (str): confidence (float)
        }
        """
        clearn_seq = self._process_seq(raw_seq)
        preds = self.model.predict(clean_seq)

        return{
            self.label_encoder.inverse_transform(i):pred
            for i, pred in enumerate(preds)
        }
