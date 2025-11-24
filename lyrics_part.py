import lyricsgenius
import os
import json
from config import lyrics_folder,analysis_folder,wordcloud_folder,save_path_json
from config import GENIUS_TOKEN
import pandas as pd

#şarkı sözlerinin çekilmesi
genius=lyricsgenius.Genius(GENIUS_TOKEN)
genius.skip_non_songs=True
genius.excluded_terms=["(Remix)","(Live)"]
genius.remove_section_headers=True
genius.timeout=30
artist_name="Mabel Matiz"
max_song_count=100
artist=genius.search_artist(artist_name,max_song_count,sort='title')

#şarkı sözlerinin dosyalarını oluşturulması
os.makedirs(lyrics_folder,exist_ok=True)

os.makedirs(save_path_json,exist_ok=True)

os.makedirs(analysis_folder,exist_ok=True)

os.makedirs(wordcloud_folder,exist_ok=True)
#çektiği şarkıyı tekrar çekmemesi için hash map'in kullanılması
songs_map={}


#sarkıların sarkı-isimleri ve artist ismine göre çekilmesi ve dosya içine yazılması
for songs in artist.songs:
    song_title = songs.title.replace("/", "-")
    if song_title not in songs_map:
        lyrics = songs.lyrics
        songs_map[song_title] = artist_name
        filename = f"{song_title}-{artist_name}.txt"
        filename_json = f"{song_title}-{artist_name}.json"
        full_path = os.path.join(lyrics_folder, filename)
        full_path_json = os.path.join(save_path_json, filename_json)
        satirlar = lyrics.splitlines()

        with open(full_path, "w", encoding="utf-8") as f:
            for satir in satirlar[1:]:
                f.write(satir + "\n")

        #song_titles.append(song_title)
        #song_lyrics.append(lyrics)

#JSON formatında tutulması
    data = {
        "artist": artist_name,
        "title": songs.title,
        "lyrics": songs.lyrics
    }

    with open(full_path_json,"w",encoding="utf-8")as f:
        json.dump(data,f,ensure_ascii=False,indent=4)


#excel_path=os.path.join(lyrics_folder,f"{artist_name}_sarkilar.xlsx")
#df = pd.DataFrame({
#    "sarki_isimleri": song_titles,
#    "sarki_sözleri": song_lyrics
#})


#df.to_excel(excel_path, index=False)
