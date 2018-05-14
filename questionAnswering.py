# -*- coding: utf-8 -*-
"""
Created on Mon May 14 13:40:58 2018

@author: USER
"""
import posTagger

def preprocessing(sentence):
    tokens = sentence.split()
    print(sentence.split())
    return tokens
    
dataTesting = "Bantengan diadakan saat hari kemerdekaan"
for text in dataTesting.lower().split(" "):
    print(posTagger.hitung(text))
preprocessing("Apa obat dari Influenza ?")
    
