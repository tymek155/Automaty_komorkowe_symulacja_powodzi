from PIL import Image
import numpy as np


def proguj_kolory(photo_rgb):
    r, g, b = photo_rgb

    if b > 185 and r < 175 and g < 220: #niebieski
        return 0
    elif g > 100 and b < 190 and r < 155: #zielony
        return 1
    elif r > 150 and g < 145 and b < 130:  #czerwony
        return 3
    elif r > 150 and g > 100 and b < 225: #żółty
        return 2
    else: #szarość
        return 4

def wyswietl_mape(mapa_progowana):
    #Określenie kolorów dla każdej wartości:
    #0 Niebieski, 1 Zielony, 2 Żółty, 3 Czerwony, 4 Szary, 5 Błękitny
    kolory = {
        0: (0, 0, 255),  #Niebieski (woda)
        1: (0, 255, 0),  #Zielony (niziny)
        2: (255, 255, 0),  #Żółty (wyżyny)
        3: (255, 0, 0),  #Czerwony (góry)
        4: (128, 128, 128),  #Szary (wysokie góry)
        5: (51, 255, 255) #Błęktiny (tereny zalane)
    }

    wys = mapa_progowana.shape[0]
    szer = mapa_progowana.shape[1]
    obraz = Image.new("RGB", (szer, wys))

    #Wypełnienie obrazu odpowiednimi kolorami
    for y in range(wys):
        for x in range(szer):
            wartosc = mapa_progowana[y, x]
            obraz.putpixel((x, y), kolory[wartosc])

    # Wyświetlenie obrazu
    obraz.show()

def run_prog():
    mapa = 'mapa2.png'
    img = Image.open(mapa)
    img = img.convert("RGB")

    mapa_progowana = np.zeros((img.height, img.width), dtype = int)

    for y in range(img.height):
        for x in range(img.width):
            kolor = img.getpixel((x,y))
            mapa_progowana[y,x] = proguj_kolory(kolor)

    #wyswietl_mape(mapa_progowana)
    return mapa_progowana

run_prog()