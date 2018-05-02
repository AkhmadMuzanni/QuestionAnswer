# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 06:07:35 2018

@author: USER
"""
import nltk

def hitung(kataCari):
    berkas = open("dataLatih.txt",'r')
    isiBerkas = berkas.read()
    berkas.close()
    
    isiBerkas = isiBerkas.lower()
    x = [nltk.tag.str2tuple(t) for t in isiBerkas.split()]
    #print(x)
    tagFind = set()
    for word in x:
        if kataCari in str(word[0]) :
            """print(word[1])"""
            if "," in str(word[1]):                
                for text in (str(word[1])).split(","):
                    tagFind.add(text)
            else:
                tagFind.add(word[1])
    #print(tagFind)
    hasil = ((0,0,0,0))
    for tagSearch in tagFind:
        temp = posterior(kataCari,tagSearch,x) 
        if temp[3] > hasil[3]:
            hasil = temp
    #print(hasil)
    if (hasil[0] == 0):
        return str(kataCari+"/None")
    else:
        return(hasil[0])

def posterior(kataCari, tagCari, textFile):
    
    wt = []
    for word in textFile:
        if tagCari in str(word[1])[:2] :
            wt.append(word[0] + "/" + word[1])
    
    """Count frequent of tag"""
    jmlTag = 0.0
    tags = [tag for (word,tag) in textFile if tagCari in str(tag)]
    fdTags = nltk.FreqDist(tags)
    for tag,frek in fdTags.most_common() :
        jmlTag += frek    
    
    """Count frequnt of all words"""
    jmlKata = 0.0
    words = [word for (word,tag) in textFile]
    fdWord = nltk.FreqDist(words)
    for word,frek in fdWord.most_common() :
        jmlKata += frek
    
    """Count prior probability"""
    prior = jmlTag / jmlKata
    
    
    """Count specified word on specified tag"""
    fd = nltk.FreqDist(textFile)
    frekKata = 0
    for word,frek in fd.most_common():
        if word[0] == kataCari:
            frekKata = frek    
    
    """Count likelihood probability"""
    likelihood = frekKata / jmlTag
    
    """Count posterior probability"""
    posterior = prior*likelihood
    
    """print("-->" + kataCari + "/" + tagCari)
    print("Prior      : " + str(prior))
    print("Likelihood : " + str(likelihood))
    print("Posterior  : " + str(posterior))
    print("")"""
    return (str(kataCari+"/"+tagCari),prior,likelihood,posterior)

def main():    
    dataTesting = "Bantengan diadakan saat hari kemerdekaan"
    for text in dataTesting.lower().split(" "):
        print(hitung(text))

if __name__ == "__main__":
    main()


