import os
import numpy as np

dir_path = os.path.dirname(os.path.realpath(__file__))
kdataApotek = np.genfromtxt(dir_path+'\Corpus\DataApotek.csv', delimiter=';', dtype=None,  encoding='ascii')
kdistribusiObat = np.genfromtxt(dir_path+'\Corpus\DistribusiObat.csv', delimiter=';', dtype=None,  encoding='ascii')
kgejala = np.genfromtxt(dir_path+'\Corpus\Gejala.csv', delimiter=';', dtype=None,  encoding='ascii')
kjenisPenyakit = np.genfromtxt(dir_path+'\Corpus\JenisPenyakit.csv', delimiter=';', dtype=None,  encoding='ascii')
kkegunaanObat = np.genfromtxt(dir_path+'\Corpus\KegunaanObat.csv', delimiter=';', dtype=None,  encoding='ascii')
kmedia = np.genfromtxt(dir_path+'\Corpus\Media.csv', delimiter=';', dtype=None,  encoding='ascii')
kobat = np.genfromtxt(dir_path+'\Corpus\Obat.csv', delimiter=';', dtype=None,  encoding='ascii')
kpencegahan = np.genfromtxt(dir_path+'\Corpus\Pencegahan.csv', delimiter=';', dtype=None,  encoding='ascii')
kpenyebab = np.genfromtxt(dir_path+'\Corpus\Penyebab.csv', delimiter=';', dtype=None,  encoding='ascii')

def relApotek(apotek, kota, nama, konteks):
    if apotek == "?x" and kota == "?x" and konteks == "apotek":
        ans = [item[0] for item in kdataApotek if item[2].lower() == nama.lower() ]
        return ans
    elif apotek == "?x" and kota == "?x" and konteks == "tempat":
        ans = [item[1] for item in kobat if item[0].lower() == nama.lower()]
        return ans
    elif apotek == "?x" and nama == "?x":
        ans = [item[0] for item in kdataApotek if item[2].lower() == kota.lower()]
        return ans
    elif kota == "?x" and nama == "?x" and konteks == "person":
        ans = [item[2] for item in kdataApotek if item[0].lower() == apotek.lower()]
        return ans
    elif kota == "?x" and nama == "?x" and konteks == "tempat":
        ans = [item[1] for item in kdataApotek if item[0].lower() == apotek.lower()]
        return ans
    elif apotek  == "?x" and nama == "?x":
        ans = [item[0] for item in kobat if item[0].lower() == kota.lower()]
        return ans
    else:
        ans = "?"
        return ans

def relDistribusiObat(obat, apotek):
    if obat == "?x":
        ans = [item[0] for item in kdistribusiObat if item[1].lower() == apotek.lower() ]
        return ans
    else:
        ans = [item[1] for item in kdistribusiObat if item[0].lower() == obat.lower()]
        return ans

def relGejala(penyakit, gejala):
    if penyakit == "?x":
        ans = [item[0] for item in kgejala if item[1].lower() == gejala.lower() ]
        return ans
    else:
        ans = [item[1] for item in kgejala if item[0].lower() == penyakit.lower()]
        return ans

def relJenisPenyakit(penyakit, jenis):
    if penyakit == "?x":
        ans = [item[0] for item in kjenisPenyakit if item[1].lower() == jenis.lower() ]
        return ans
    else:
        ans = [item[1] for item in kjenisPenyakit if item[0].lower() == penyakit.lower()]
        return ans

def relGunaObat(obat, guna):
    if obat == "?x":
        ans = [item[0] for item in kkegunaanObat if item[1].lower() == guna.lower() ]
        return ans
    else:
        ans = [item[1] for item in kkegunaanObat if item[0].lower() == obat.lower()]
        return ans

def relMedia(penyakit, media):
    if penyakit == "?x":
        ans = [item[0] for item in kmedia if item[1].lower() == media.lower() ]
        return ans
    else:
        ans = [item[1] for item in kmedia if item[0].lower() == penyakit.lower()]
        return ans

def relObat(penyakit, obat):
    if penyakit == "?x":
        ans = [item[0] for item in kobat if item[1].lower() == obat.lower() ]
        return ans
    else:
        ans = [item[1] for item in kobat if item[0].lower() == penyakit.lower()]
        return ans

def relPencegahan(penyakit, pencegahan):
    if penyakit == "?x":
        ans = [item[0] for item in kpencegahan if item[1].lower() == pencegahan.lower() ]
        return ans
    else:
        ans = [item[1] for item in kpencegahan if item[0].lower() == penyakit.lower()]
        return ans

def relPenyebab(penyakit, sebab):
    if penyakit == "?x":
        ans = [item[0] for item in kpenyebab if item[1].lower() == sebab.lower() ]
        return ans
    else:
        ans = [item[1] for item in kpenyebab if item[0].lower() == penyakit.lower()]
        return ans