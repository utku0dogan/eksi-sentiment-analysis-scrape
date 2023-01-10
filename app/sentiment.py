from keras.models import load_model
import pickle
import tensorflow as tf
from pandas import read_csv
from sklearn.feature_extraction.text import TfidfVectorizer

def sentiment(texts):
    with open('app/models/turkish_tokenizer_hack.pickle', 'rb') as handle:
        turkish_tokenizer = pickle.load(handle)
    model = load_model('app/models/hack_model.h5')
    entries_tokens = turkish_tokenizer.texts_to_sequences(texts)
    max_tokens = 62
    tahminler = []
    tokens_pad = tf.keras.utils.pad_sequences(entries_tokens, maxlen=max_tokens)
    for i in model.predict(tokens_pad):
        if i < 0.5:
            tahminler.append("positive")
        else:
            tahminler.append("negative")
    return tahminler


def emotion(texts):
    df = read_csv('app/datasets/6_Farklı_Duygu.csv')
    with open('app/datasets/stopwords-tr.txt', 'r') as f:
        myList = [line.strip() for line in f]
    tfidf = TfidfVectorizer(sublinear_tf=True, min_df=5, norm='l2', encoding='latin-1', ngram_range=(1, 2), stop_words=myList)

    loaded_model = pickle.load(open("app/models/emotion_model.pickle", 'rb'))
    corpus = texts
    tfidf.fit_transform(df.Entry).toarray()
    features = tfidf.transform(corpus).toarray()
    results = loaded_model.predict(features)
    return results    