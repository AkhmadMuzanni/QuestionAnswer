# -*- coding: utf-8 -*-
"""
Created on Mon May 14 13:40:58 2018

@author: USER
"""
import re
import Knowledge as kn
from nltk.tag import CRFTagger

ct = CRFTagger()

ct.set_model_file('all_indo_man_tag_corpus_model.crf.tagger')

questions = ["apa", "siapa", "mana", "bagaimana"]
penyakit = ["influenza", "cacar air", "diabetes", "hipertensi"]

def preprocessing(sentence):
    print(sentence)
    eta = ""
    subs = []
    tokens = re.findall(r'[a-z]+', sentence)
    for token in tokens:
        if token in questions:
            if token.lower() == "apa" or token.lower() == "bagaimana":
                eta = "things"
            elif token.lower() == "mana":
                eta = "tempat"
            elif token.lower() == "siapa":
                eta = "person"
            else:
                eta = ""

        sets = False
        if token in penyakit:
            sets = True

    tokens = map(unicode,tokens)
    postag = ct.tag(tokens)
    print(postag)

    if eta == "things":
        rel = [item[0] for item in postag if item[1] == "NN" or item[1] == "VB"]
        subs = [item[0] for item in postag if item[1] == "NN" or item[1] == "FW" or item[1] == "NNP" or item[1] == "JJ"]

    elif eta == "tempat":
        rel = [item[0] for item in postag if item[1] == "NN"]
        subs = [item[0] for item in postag if item[1] == "NN"]

    else:
        rel = [item[0] for item in postag if item[1] == "NN"]
        subs = [item[0] for item in postag if item[1] == "NN"]

    if "pemilik" in rel:
        for sub in subs:
            temp = kn.relApotek(sub, "?x", "?x", eta)
            if temp:
                print(', '.join(temp))

    if "pemilik" not in rel and "apotek" in rel:
        for sub in subs:
            temp = kn.relApotek(sub, "?x", "?x", eta)
            if temp:
                print(', '.join(temp))

    if "manfaat" in rel:
        for sub in subs:
            temp = kn.relGunaObat(sub, "?x")
            if temp:
                print(', '.join(temp))

    if "menular" in rel:
        for sub in subs:
            temp = kn.relMedia(sub, "?x")
            if temp:
                print(', '.join(temp))

    if "jenis" in rel:
        for sub in subs:
            temp = kn.relJenisPenyakit(sub, "?x")
            if temp:
                print(', '.join(temp))

    if "obat" in rel:
        if sets:
            for sub in subs:
                temp = kn.relObat(sub, "?x")
                if temp:
                    print(', '.join(temp))
        else:
            for sub in subs:
                temp = kn.relObat("?x", sub)
                if temp:
                    print(', '.join(temp))


    if "pencegahan" in rel or "mencegah" in rel:
        for sub in subs:
            temp = kn.relPencegahan(sub, "?x")
            if temp:
                print(', '.join(temp))
    
# dataTesting = "Bantengan diadakan saat hari kemerdekaan"
# for text in dataTesting.lower().split(" "):
#     print(posTagger.hitung(text))
# preprocessing("Apa obat dari Influenza ?")


# print(kn.relObat("influenza", "?x"))
# print(kn.relPencegahan("influenza", "?x"))

preprocessing("siapa pemilik apotek swadaya")
preprocessing("di mana apotek swadaya")





