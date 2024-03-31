import pandas as pd
import nltk
from nltk import word_tokenize
from nltk.stem.isri import ISRIStemmer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tag import pos_tag
from nltk.tokenize import RegexpTokenizer
#nltk.download('punkt')
#nltk.download('maxent_ne_chunker')
#nltk.download('words')
# Named entity recognition (not available in NLTK for Arabic)

df = pd.DataFrame(pd.read_csv('articles.csv'))
#print(df.head())
#for i in df['article']:

st = ISRIStemmer()

def preprocess_article(article):
    # hna drna toknization 
    tokenizer = RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(article)
    # hna drna part of speech tagging
    pos = pos_tag(tokens)
    '''# lemmatization
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(token, pos=get_wordnet_pos(pos_tag)) for token, pos_tag in pos]'''
    # hna drna stopword removal
    ar_sw = set(stopwords.words('arabic'))
    filtered_tokens = [token for token in stemming(pos) if token not in ar_sw]
    # bind tokens back 
    enhanced_article = ' '.join(filtered_tokens)
    return enhanced_article

def stemming(tags):
    stemed_tokens = []
    for token,tag in tags:
        if tag == 'NNP':
            stemed_tokens.append(token)
        else:
            stem = st.stem(token)
            stemed_tokens.append(stem)
    return stemed_tokens

def get_wordnet_pos(treebank_tag):
    if treebank_tag.startswith('J'):
        return nltk.corpus.wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return nltk.corpus.wordnet.VERB
    elif treebank_tag.startswith('N'):
        return nltk.corpus.wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return nltk.corpus.wordnet.ADV
    else:
        return nltk.corpus.wordnet.NOUN

# hna applikin l preprocessing l kol article f dataframe ta3na
df['enhanced_articles'] = df['article'].apply(preprocess_article)

print(df['enhanced_articles'])
