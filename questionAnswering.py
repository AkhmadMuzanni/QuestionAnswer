# -*- coding: utf-8 -*-
"""
Created on Mon May 14 13:40:58 2018

@author: USER
"""
import re
import posTagger
import numpy as np
import Knowledge as kn
from nltk.tag import CRFTagger

ct = CRFTagger()

ct.set_model_file('all_indo_man_tag_corpus_model.crf.tagger')

questions = ["apa", "siapa", "mana"]
penyakit = ["influenza", "cacar air", "diabetes", "hipertensi"]

def preprocessing(sentence):
    print(sentence)
    eta = ""
    subs = []
    tokens = re.findall(r'[a-z]+', sentence)
    for token in tokens:
        if token in questions:
            if token.lower() == "apa":
                eta = "things"
            elif token.lower() == "mana":
                eta = "tempat"
            elif token.lower() == "siapa":
                eta = "person"
            else:
                eta = ""
        if token in penyakit:
            subs = [token]

    # print(eta)



    postag = ct.tag(tokens)
    if eta == "things":
        rel = [item[0] for item in postag if item[1] == "NN"]
        if not subs:
            subs = [item[0] for item in postag if item[1] == "NN" or item[1] == "FW" or item[1] == "NNP"]

    if eta == "tempat":
        rel = [item[0] for item in postag if item[1] == "NN"]
        subs = [item[0] for item in postag if item[1] == "NN"]

    if eta == "person":
        rel = [item[0] for item in postag if item[1] == "NN"]
        subs = [item[0] for item in postag if item[1] == "NN"]

    if "pemilik" in rel:
        for sub in subs:
            print(kn.relApotek(sub, "?x", "?x", eta))

    if "pemilik" not in rel and "apotek" in rel:
        for sub in subs:
            temp = kn.relApotek(sub, "?x", "?x", eta)
            print()

    if "manfaat" in rel:
        for sub in subs:
            print(kn.relGunaObat(sub, "?x"))

    if "obat" in rel:
        for sub in subs:
            print(kn.relObat(sub, "?x"))


    print(postag)
    return tokens
    
# dataTesting = "Bantengan diadakan saat hari kemerdekaan"
# for text in dataTesting.lower().split(" "):
#     print(posTagger.hitung(text))
# preprocessing("Apa obat dari Influenza ?")


# print(kn.relObat("influenza", "?x"))
# print(kn.relPencegahan("influenza", "?x"))

preprocessing("siapa pemilik apotek swadaya?")





