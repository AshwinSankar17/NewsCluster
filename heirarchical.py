from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.manifold import MDS
import matplotlib.pyplot as plt
import pandas as pd
from scipy.cluster.hierarchy import ward, dendrogram
import string
from sklearn.metrics import accuracy_score


def clean(text):
    '''
        Clean text before running clusterer
    '''
    text = text.strip()
    text = text.lower()
    for punct in string.punctuation:
        text = text.replace(punct, ' ')
    lst = text.split()
    text = " ".join(lst)
    for t in text:
        if t not in string.printable:
            text = text.replace(t, '')
    return text

# Function to return a list of stemmed words
def tokenize_and_stem(text_file):
    # declaring stemmer and stopwords language
    stemmer = SnowballStemmer("english")
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(text_file)
    filtered = [w for w in words if w not in stop_words]
    stems = [stemmer.stem(t) for t in filtered]
    return stems


def hierarchical_cluster():

    df = pd.read_csv('./data/NewsCluster.csv')
    data = df["Title"].tolist()

    for dt in data:
        data[data.index(dt)] = clean(dt)

    data = pd.DataFrame(data, columns=["text"])
    data['text'].dropna(inplace=True)

    # text data in dataframe and removing stops words
    stop_words = set(stopwords.words('english'))
    data['text'] = data['text'].apply(lambda x: ' '.join([word for word in x.split() if word not in stop_words]))

    # Using TFIDF vectorizer to convert convert words to Vector Space
    tfidf_vectorizer = TfidfVectorizer(max_features=200000,
                                       use_idf=True,
                                       stop_words='english',
                                       tokenizer=tokenize_and_stem)
    #                                   ngram_range=(1, 3))

    # Fit the vectorizer to text data
    tfidf_matrix = tfidf_vectorizer.fit_transform(data['text'])

    # Calculating the distance measure derived from cosine similarity
    distance = 1 - cosine_similarity(tfidf_matrix)

    # Ward’s method produces a hierarchy of clusterings
    linkage_matrix = ward(distance)
    fig, ax = plt.subplots(figsize=(15, 20)) # set size
    ax = dendrogram(linkage_matrix, orientation="top", labels=data.values)
    plt.tight_layout()
    plt.title('News Headlines using Ward Hierarchical Method')
    plt.savefig('./results/hierarchical.png')

if __name__ == "__main__":
    hierarchical_cluster()