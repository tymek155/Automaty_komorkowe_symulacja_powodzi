from progowanie import run_prog
from progowanie import wyswietl_mape
import pygame
import numpy as np


class Sasiedzi:
    def __init__(self):
        self.elementy = [0] * 7

    def oblicz_sasiadow(self, mapa_progowana, y, x):
            for j in range(-1,2):
                for i in range(-1,2):
                    if j == 0 and i == 0:
                        continue
                    self.elementy[mapa_progowana[(y+j) % mapa_progowana.shape[0], (x+i) % mapa_progowana.shape[1]]]+=1

def przejscia(mapa_progowana, counter):
    #Obszar zalany = 5
    up_mapa = np.copy(mapa_progowana)
    for y in range(mapa_progowana.shape[0]):
        for x in range(mapa_progowana.shape[1]):
            sasiedzi = Sasiedzi()
            sasiedzi.oblicz_sasiadow(mapa_progowana, y, x)

            #Jeżeli sprawdzasz wode 0
            if mapa_progowana[y,x] == 0:
                if sasiedzi.elementy[5] >= 1:
                    up_mapa[y, x] = 5
            #Jeżeli sprawdzasz niziny
            elif mapa_progowana[y,x] == 1:
                if sasiedzi.elementy[5]>=2:
                    up_mapa[y,x] = 5
                elif counter % 5 == 0 and sasiedzi.elementy[5]>=1:
                    up_mapa[y, x] = 5
            #Jeżeli sprawdzasz wyżyny
            elif mapa_progowana[y,x] == 2:
                if sasiedzi.elementy[5]>=3:
                    up_mapa[y,x]=5
                elif counter % 8 == 0 and sasiedzi.elementy[5]>=2:
                    up_mapa[y, x] = 5
            #Jeżeli sprawdzasz góry
            elif mapa_progowana[y,x] == 3:
                if sasiedzi.elementy[5]>=4:
                    up_mapa[y,x]=5
                elif counter % 10 == 0 and sasiedzi.elementy[5]>=3:
                    up_mapa[y, x] = 5
            #Jeżeli sprawdzasz giga góry:
            elif mapa_progowana[y,x] == 4:
                if sasiedzi.elementy[5]>=5:
                    up_mapa[y,x]=5
                elif counter % 12 == 0 and sasiedzi.elementy[5]>=4:
                    up_mapa[y, x] = 5
                elif counter % 15 == 0 and sasiedzi.elementy[5]>=3:
                    up_mapa[y, x] = 5

    return up_mapa

def opady(mapa_progowana, ilosc):
    up_mapa = np.copy(mapa_progowana)
    ilosc_zer = np.argwhere(mapa_progowana ==0)

    if len(ilosc_zer) < ilosc:
        ilosc = len(ilosc_zer)

    wylosuj_opad = ilosc_zer[np.random.choice(len(ilosc_zer), ilosc, replace=False)]

    for y,x in wylosuj_opad:
        up_mapa[y,x] = 5

    return up_mapa

def tornado(mapa_progowana, y, x):
    up_mapa = np.copy(mapa_progowana)
    for j in range(-2, 3):
        for i in range(-2, 3):
            if (j,i) == (-2,-2) or (j,i) == (-2, 2) or (j,i) == (2, -2) or (j,i) == (2, 2):
                continue
            up_mapa[(y+j) % mapa_progowana.shape[0], (x+i) % mapa_progowana.shape[1]] = 5

    return up_mapa

def zwroc_stan(mapa_progowana, y, x):
    return mapa_progowana[y,x]

def obniz_teren(mapa_progowana, obnizenie, y, x):
    obnizenie -= 1
    if (obnizenie) < 0:
        return mapa_progowana

    up_mapa = np.copy(mapa_progowana)
    for j in range(-2, 3):
        for i in range(-2, 3):
            if (j,i) == (-2,-2) or (j,i) == (-2, 2) or (j,i) == (2, -2) or (j,i) == (2, 2):
                continue
            elif up_mapa[(y + j) % mapa_progowana.shape[0], (x + i) % mapa_progowana.shape[1]] == obnizenie + 1:
                up_mapa[(y + j) % mapa_progowana.shape[0], (x + i) % mapa_progowana.shape[1]] = obnizenie

    return up_mapa

def tama(mapa_progowana, y, x):
    up_mapa = np.copy(mapa_progowana)
    for j in range(-2, 3):
        for i in range(-2, 3):
            if (j,i) == (-2,-2) or (j,i) == (-2, 2) or (j,i) == (2, -2) or (j,i) == (2, 2):
                continue
            up_mapa[(y+j) % mapa_progowana.shape[0], (x+i) % mapa_progowana.shape[1]] = 6

    return up_mapa

