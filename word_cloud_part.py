import os
from wordcloud import WordCloud
from config import klasör_yolu_word

all_text=""
for file_name in sorted(os.listdir(klasör_yolu_word)):
    file_path_word = os.path.join(klasör_yolu_word, file_name)
    with open(file_path_word,'r',encoding='utf-8') as f:
        all_text+=f.read()+" "

wc=WordCloud(
    background_color='white',
    height=600,
    width=400
)
wc.generate(all_text)
wc.to_file("word_cloud_second.png")




