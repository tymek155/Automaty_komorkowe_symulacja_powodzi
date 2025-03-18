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
* PIL
* pygame_gui
	
# Wykorzystanie
Kod był uruchamiany i napisany w środowisku PyCharm. Struktura kodu składa się 
z funkcji oraz klas `proguj_kolory`, która rozdziela założone kategorie terenu na podstawie kolorów RGB, `wyswietl_mape` 
wyświetlającą przetworzoną mapę z odpowiednio dopasowanymi kolorami, `run_prog` będącą funkcją główną wczytującą 
mapę z pliku `PNG`, konwertującą go do siatki kategorii oraz zwracającą macierz `mapa_progowa`, `Sasiedzi` będącej 
klasą zliczającą punkty sąsiadujące dla danego punktu (wykorzystywana do symulacji rozlewania się wody), `przejscia` 
aktualizującej stan mapy bazująć na liczbie sąsiadów zalanych (odpowiednie reguły znajdują się w kodzie), `opady` 
dodającej losowe punkty zalania, symulując w ten sposób lokalne opady, `tornado`, `obniz_teren`, `tama` służących 
do interaktywnej modyfikacji terenu przez użytkownika oraz `main`, gdzie zaprojektowne jest całe GUI dla użytkownika
w postaci przycisków oraz listy rozwijanej, znajduje się tam także cała logika symulacji i jej ciągłej aktualizacji 
oraz obsługa interakcji.

# Przykładowa wizualizacja


