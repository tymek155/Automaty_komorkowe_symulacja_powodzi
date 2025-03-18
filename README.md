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
do interaktywnej modyfikacji terenu przez użytkownika oraz `main`, gdzie zaprojektowne jest całe GUI dla 
użytkownika w postaci przycisków oraz listy rozwijanej, znajduje się tam także cała logika symulacji i jej ciągłej 
aktualizacji oraz obsługa interakcji.

# Przykładowe wizualizacje
## Wizualizacja startowa, bez edycji (widoczny wycinek z mapy świata - Europa, fragment Afryki oraz Azji)
<div align="center">

![image](https://github.com/user-attachments/assets/c51a9ac7-8731-4f13-b775-b31734522da2)
</div>

## Przykładowa wizualizacja powodzi z użyciem wyłącznie opcji `Lekkie opady`
<div align="center">
	
![image](https://github.com/user-attachments/assets/049eda56-4224-4518-9c55-af12752b7857)
</div>

## Przykładowa prezentacja użycia opcji podtopienia/tornada (błękitny pas na górze mapy), obniżenia (szare pasmo górskie z lewej strony jest w połowie czerwone) oraz tamy (brązowy okrąg w prawym, górnym rogu)
<div align="center">
	
![image](https://github.com/user-attachments/assets/d75acb3e-0ed0-4bbf-9b01-525c0e41ea7f)
</div>

## Przykładowa wizualziacja z użyciem opcji z poprzedniej wizualizacji, wraz z symulacją średnich opadów
<div align="center">
	
![image](https://github.com/user-attachments/assets/472fb73c-4b95-40b2-8ebb-9e2e1293166c)
</div>

## Stan końcowy wizualizacji wyżej - wizualizacja zakończyła się zatopieniem całego obszaru z wyjątkiem obszaru zatoczonego tamą
<div align="center">
	
![image](https://github.com/user-attachments/assets/0dba8ab9-d375-4dad-af3d-46b95a5b7784)
</div>

# English version

# General Information 
The project implements a flood simulation based on processing a ready-made map from an image and modeling the 
spread of water using cellular automata. The entire project consists of processing the map image into different 
terrain categories (water, lowlands, highlands, mountains, high mountains, flooded areas), implementing the 
simulation logic, such as water spreading, the effect of rainfall, environmental changes (local flooding 
"tornadoes," terrain lowering, building flood-proof dams), and a graphical interface enabling the visualization of 
the simulation and interaction with it.

# Technologies  
The code uses:  
* Python 3.12
* NumPy 2.2.2
* Pygame 2.6.0
* PIL 11.0.0
* pygame_gui 0.6.12

# Usage 
The code was written and executed in the PyCharm environment. The code structure consists of functions and 
classes, including `proguj_kolory`, which separates the predefined terrain categories based on RGB colors, 
`wyswietl_mape`, which displays the processed map with appropriately adjusted colors, and `run_prog`, the main 
function that loads the map from a `PNG` file, converts it into a category grid, and returns the `mapa_progowa` 
matrix. Additionally, there is the `Sasiedzi` class, which counts neighboring points for a given point (used for 
simulating water spread), `przejscia`, which updates the map state based on the number of flooded neighbors (the 
corresponding rules are defined in the code), and `opady`, which adds random flooding points, simulating local 
rainfall. Furthermore, functions such as `tornado`, `obniz_teren`, and `tama` are used for interactive terrain 
modifications by the user. The `main` function contains the entire user interface (GUI) designed with buttons and 
a dropdown list, as well as the complete logic for the simulation, its continuous updates, and interaction handling.

# Sample visualizations
## Starting visualization, without editing (visible fragment of the world map - Europe, part of Africa and Asia)
<div align="center">

![image](https://github.com/user-attachments/assets/c51a9ac7-8731-4f13-b775-b31734522da2)
</div>

## Example flood visualization using only the `Light Rain` option
<div align="center">
	
![image](https://github.com/user-attachments/assets/049eda56-4224-4518-9c55-af12752b7857)
</div>

## Example demonstration of using the flood/tornado option (blue band at the top of the map), depression (grey mountain range on the left is half red) and dam (brown circle in the upper right corner)
<div align="center">
	
![image](https://github.com/user-attachments/assets/d75acb3e-0ed0-4bbf-9b01-525c0e41ea7f)
</div>

## Example visualization using the options from the previous visualization, including simulation of average precipitation
<div align="center">
	
![image](https://github.com/user-attachments/assets/472fb73c-4b95-40b2-8ebb-9e2e1293166c)
</div>

## Final state of the visualization above - the visualization ended with the entire area flooded except for the area surrounded by the dam
<div align="center">
	
![image](https://github.com/user-attachments/assets/0dba8ab9-d375-4dad-af3d-46b95a5b7784)
</div>
