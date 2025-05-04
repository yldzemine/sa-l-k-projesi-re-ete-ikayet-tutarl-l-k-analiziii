
import pandas as pd
import re
from nltk.tokenize import word_tokenize
from snowballstemmer import TurkishStemmer
from zeyrek import MorphAnalyzer
import nltk

nltk.download('punkt')

# Türkçe kökleyici ve çözümleyici
stemmer = TurkishStemmer()
analyzer = MorphAnalyzer()

# Türkçe stop word listesi (örnek - genişletebilirsin)
stop_words = set([
    "ve", "ile", "de", "da", "bir", "bu", "çok", "ama", "fakat", "gibi",
    "mi", "mu", "mı", "mü", "için", "ne", "ya", "ki", "veya", "veya"
])

# Örnek veri (veya CSV'den okuyabilirsin)
complaints = [
    "Bekleme süresi",
    "Saygıyla Muamele Edilmiyor",
    "Laboratuvar Bekle",
    "Maliyet",
    "Çalışma Saatleri",
    "Kimi arayacağımı bilmiyorum",
    "Bilgi Eksikliği",
    "Park Sorunları"
]

def preprocess(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)  # noktalama işaretlerini kaldır
    tokens = word_tokenize(text, language='turkish')
    tokens = [t for t in tokens if t not in stop_words]

    # Stemming
    stemmed = [stemmer.stemWord(t) for t in tokens]

    # Lemmatization (ilk çözüm önerisini alır)
    lemmas = []
    for t in tokens:
        results = analyzer.analyze(t)
        if results:
            lemmas.append(results[0].lemma)
        else:
            lemmas.append(t)
    
    return {
        "orijinal": text,
        "tokenler": tokens,
        "stem": stemmed,
        "lemma": lemmas
    }

# Uygula
for c in complaints:
    result = preprocess(c)
    print("Orijinal:", result["orijinal"])
    print("Tokenler:", result["tokenler"])
    print("Stem:", result["stem"])
    print("Lemma:", result["lemma"])
    print("---")