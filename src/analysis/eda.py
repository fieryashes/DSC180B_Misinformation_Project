import pandas as pd
import nltk
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
import nltk.corpus
nltk.download('stopwords')
from nltk.corpus import stopwords
import re

def text_cleaning(video_caption):
    # normalize case
    video_caption = video_caption.lower()
    # remove punctuation
    video_caption = re.sub(r"(@\[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)|^rt|http.+?", "", video_caption)
    # remove stopwords
    stop = stopwords.words('english')
    video_captions = " ".join(\[word for word in video_captions.split() if word not in (stop)])
    # lemmenization
    wn = nltk.WordNetLemmatizer()
    video_captions = " ".join(\[wn.lemmatize(word) for word in video_captions.split()])
    return video_caption

def tfidf(video_df):
    words = pd.Series(video_df.text.dropna().str.split().sum())
    tfidf = pd.DataFrame([], index=video_df.index)  # dataframe of documents
    tf_denom = (video_df.text.str.count(' ') + 1)
    for w in words.value_counts().iloc[0:500].index:
        # imperfect pattern match for speed
        re_pat = ' %s ' % w
        tf = video_df.text.str.count(re_pat) / tf_denom
        idf = np.log(len(df) / video_df.text.str.contains(re_pat).sum())
        tfidf[w] =  tf * idf

    
    
    