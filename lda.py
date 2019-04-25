import nltk
import gensim
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from gensim.utils import simple_preprocess
from gensim.parsing.preprocessing import STOPWORDS
from nltk.stem import WordNetLemmatizer, SnowballStemmer
from gensim import corpora
nltk.download('wordnet')

from nltk.stem.porter import *
from collections import Counter
stemmer = PorterStemmer()
stop_words=set(stopwords.words('english'))
tokenizer=RegexpTokenizer(r'\w+')

def data_load(path):

    with open(path) as f:
        doc=f.read().splitlines()
    print("data loaded successfully")
    return doc

def preprocess(doc):

    '''tokenizing the doc'''
    tokens=[tokenizer.tokenize(word) for word in doc]
    '''removing the stopwords'''
    final_tokens=[tok for sen in tokens for tok in sen if tok not in stop_words]
    '''lemmatizing the word'''
    lemmas=[lemmatize_stemming(tok) for tok in final_tokens]

    return final_tokens,lemmas

def lemmatize_stemming(text):
    return stemmer.stem(WordNetLemmatizer().lemmatize(text, pos='v'))

def word_count(tokens):

    word_count=Counter(tokens)
    return word_count

def number_sentences(doc):
    doc=' '.join(doc)
    sent_text = nltk.sent_tokenize(doc)
    return sent_text

def topic_modeling(corpus,n,id2word):
    lda_model = gensim.models.ldamodel.LdaModel(corpus=corpus,num_topics=n,id2word=id2word)

    return lda_model

def corpus_preprocessing(sent_text):
    new_token=[]
    lemma=[]
    for sentence in sent_text:

        tokens,lemmas=preprocess(sentence.split())
        new_token.append(tokens)
        lemma.append(lemmas)
    dictionary = corpora.Dictionary(new_token)
    corpus = [dictionary.doc2bow(text) for text in new_token]

    return corpus,dictionary


    #return

def corpus_statistics(doc):
    tokens,lemmas=preprocess(doc)
    #print(tokens)
    sentences=number_sentences(doc)
    #print(sentences)

    counts=word_count(tokens)
    number_of_tokens=len(tokens)
    number_of_sentences=len(sentences)
    counts
    return number_of_tokens,number_of_sentences,counts

def main():
    path=input("enter the path of the data")
    doc=data_load(path)
    #print(doc)
    sent_text=number_sentences(doc)
    #print(sent_text)
    preprocess_corpus,dictionary=corpus_preprocessing(sent_text)
    n=int(input("enter the number of topics"))
    model=topic_modeling(preprocess_corpus,n,dictionary)
    print(model.print_topics(n))
    stats=input("do you want to know corpus statistics enter either yes or no")
    if stats == 'yes':
        number_of_tokens,number_of_sentences,counts=corpus_statistics(doc)
        print("number of words in document is %d"%(number_of_tokens))
        print("number of sentences in document is %d"%(number_of_tokens))
        print(counts)

    #print(preprocess)

    #corpus = [dictionary.doc2bow(text) for text in texts]

if __name__ == "__main__":
    # execute only if run as a script
    main()
