PROJEKT:
Kolorowanie grafu
Projekt przedstawia rozwiazanie problemu kolorowania grafu z wykorzystaniem roznych algorytmow optymalizacyjnych oraz porowanie ich efektywnosci.

CEL PROJEKTU:
Zadanie polega na przypisaniu kolorow wierzcholkow grafu tak, aby zadane dwa sasiadujace wierzcholki nie mialy tego samego koloru, uzywajac maksymalnie k kolorow. 
Minimalizujemy liczbe konfliktow (czyli sasiadujacych wierzcholkow o tym samym kolorze).

ALGORYTMY:
Brute force - pelny przeglad wszystkich mozliwych kolorowan.
Hill Climbing - wspoinaczka klasyczna z deterministycznym wyborem najlepszego sasiada.
Tabu Search - algorytm tabu z mozliwościa ustawienia rozmiaru listy tabu.

URUCHAMIANIE:
'''bash
python main.py --file data/sample_graph.txt --colors 3 --method hill --iterations 100
python main.py --file data/sample_graph.txt --colors 3 --method tabu --tabu_size 7
python main.py --file data/sample_graph.txt --colors 3 --method brute

Porownanie metod:
python compare_methods.py

Nastepnie mozliwa wizualizacja wynikow:
python plot_results.py

Eksperymenty:
Skrypt compare_methods.py przeprowadza porownanie metod na podstawie:
- Jakosci rozwiazania (sredni koszt)
- Czasu wykonania
- Zuzycia pamieci
- szybkosci zbieznosci
Dane zbierane sa automatycznie i zapisywane do pliku .csv. Skrypt plot_results.py tworzy wykresy porownawcze.

przykladowy plik wejsciowy (sample_graph.txt)
0 1
0 2
1 2
1 3
2 3
