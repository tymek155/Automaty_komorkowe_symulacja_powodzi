Go to [English version](#english-version)
# Ogólne informacje
Projekt realizuje implementację symulacji powodzi opartą na przetwarzaniu gotowej mapy ze zdjęcia oraz modelowaniu 
rozprzestrzeniania się wody za pomocą automatów komórkowych. Na całosć projektu składają się przetwarzanie obrazu 
mapy na różne kategorie terenu (woda, niziny, wyżyny, góry, wysokie góry, tereny zalane), implementacja logiki 
symulacji np. rozlewanie się wody, efekt opadów, zmiany środowiskowe (lokalne zalania "tornada", obniżanie terenu 
budowanie niezalewalnych tam) oraz interfejs graficzny umożliwiający wizualizację symulacji oraz interakcje z nią.

# Technologie
W kodzie użyto:
* Python 3.12
* NumPy 2.2.2
* Pygame 2.6.0
* PIL 11.0.0
* pygame_gui 0.6.12
	
# Wykorzystanie
Kod był uruchamiany i napisany w środowisku PyCharm. Struktura kodu składa się 
z funkcji oraz klas `proguj_kolory`, która rozdziela założone kategorie terenu na podstawie kolorów RGB, `wyswietl_mape` 
wyświetlającą przetworzoną mapę z odpowiednio dopasowanymi kolorami, `run_prog` będącą funkcją główną wczytującą 
mapę z pliku `PNG`, konwertującą go do siatki kategorii oraz zwracającą macierz `mapa_progowa`, `Sasiedzi` będącej 
klasą zliczającą punkty sąsiadujące dla danego punktu (wykorzystywana do symulacji rozlewania się wody), `przejscia` 
aktualizującej stan mapy bazująć na liczbie sąsiadów zalanych (odpowiednie reguły znajdują się w kodzie), `opady` 
dodającej losowe punkty zalania, symulując w ten sposób lokalne opady, `tornado`, `obniz_teren`, `tama` służących 
do interaktywnej modyfikacji terenu przez użytkownika oraz `main`, gdzie zaprojektowne jest całe GUI dla użytkownika

![image](https://github.com/user-attachments/assets/c51a9ac7-8731-4f13-b775-b31734522da2)

![image](https://github.com/user-attachments/assets/049eda56-4224-4518-9c55-af12752b7857)
![image](https://github.com/user-attachments/assets/d75acb3e-0ed0-4bbf-9b01-525c0e41ea7f)
![image](https://github.com/user-attachments/assets/472fb73c-4b95-40b2-8ebb-9e2e1293166c)
![image](https://github.com/user-attachments/assets/0dba8ab9-d375-4dad-af3d-46b95a5b7784)



w postaci przycisków oraz listy rozwijanej, znajduje się tam także cała logika symulacji i jej ciągłej aktualizacji 
oraz obsługa interakcji.

# Przykładowa wizualizacja


