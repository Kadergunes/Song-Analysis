import nltk
from nltk.corpus import stopwords as nltk_stopwords
import json




nltk.download('stopwords')
turkish_stopwords = nltk_stopwords.words('turkish')

#stop-word kelime listesinin okunması
with open('stopwords-tr.json', 'r', encoding='utf-8') as f:
    stopwords = json.load(f)
with open('turkish_stopwords.txt','r',encoding='utf-8') as f:
    stop_words=f.read().splitlines()
with open('turkish_stopword.txt','r',encoding='utf-8') as f:
    tr_stopwords=f.read().splitlines()







