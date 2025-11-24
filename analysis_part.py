import os
import re
from config import klasör_yolu_word, klasör_yolu,klasör_yolu_output
from zemberek_part import morphology,spell_checker
from stop_words_part import turkish_stopwords,stopwords,stop_words,tr_stopwords


ritim_words = []

#her şarkı dosyasının alfabetik sıraya göre okunması
for file_name in sorted(os.listdir(klasör_yolu)):
    file_path = os.path.join(klasör_yolu, file_name)

    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        sarki_icerik = f.readlines()
        new_icerik = []
        final_new_icerik = []
#her sarkı cümlesinin ayrılması
        for satir in sarki_icerik:
            satir = satir.strip()
            if not satir:
                continue
#sarkı sözlerinin kelimelere ayrılması(boşluklarla)
            words = satir.split()
            new_words = []
#kelimelerin küçük harflere çevrilmesi ve noktalama işaretlerinin temizlenmesi ve ritim sözcüklerinin toplanması
            for word in words:
                word = word.lower()
                word = re.sub(r"[^\wığüşöçİĞÜŞÖÇ]", "", word)
                if len(word) < 3:
                    ritim_words.append(word)
                    continue
                    #yazım yanlışı olan kelimelerin  için öneri yapılması(bi' ve bir)
                analysis = morphology.analyze(word)
                if analysis.analysisCount() == 0:#kelime bulunamadıysa
                    suggestion = spell_checker.suggestForWord(word)
                    if suggestion:
                        word = suggestion[0]

                    else:
                        continue
                new_words.append(str(word))
            new_sentence = " ".join(new_words)
            #kelimelerin cümlelerdeki anlamlarına göre analiz edilmesi
            if new_sentence.strip():
                sentence_analysis = morphology.analyzeAndDisambiguate(new_sentence)
                best_analyses = sentence_analysis.bestAnalysis()
            else:
                continue
#kelimeleri ve analiz sonuçlarının eşleştirilerek köklerine ve pozisyonlarına ayrılması
            for word, analysis in zip(new_words, best_analyses):
                java_lemmas = analysis.getLemmas()
                lemmas = []
                for lemma in java_lemmas:
                    lemmas.append(str(lemma))
                    pos = str(analysis.getPos())
                print(f"Kelime: {lemma} ,Pos:{pos}")
#stop-word temizliğinin yapılması
                for lemma in lemmas:
                    if lemma not in turkish_stopwords and lemma not in stopwords and lemma not in stop_words and lemma not in tr_stopwords and pos != "Punctuation":
                        new_icerik.append(lemma + "->" + pos + "\n ")
                    if lemma not in turkish_stopwords and lemma not in stopwords and lemma not in stop_words and lemma not in tr_stopwords and pos != "Punctuation":
                        final_new_icerik.append(lemma + "\n")

    file_path_output = os.path.join(klasör_yolu_output, file_name)
    with open(file_path_output, "w", encoding="utf-8") as f:
        f.writelines(new_icerik)
    file_path_word = os.path.join(klasör_yolu_word, file_name)
    with open(file_path_word, "w", encoding="utf-8") as f:
        f.writelines(final_new_icerik)