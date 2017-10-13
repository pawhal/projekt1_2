# projekt1_2
Stworzenie programu, który będzie tworzyć listę zapytań SQL i zapisywać je do pliku.

Użytkownik podaje numer zadania i w kolejnej linii zapytanie SQL (takie jak odpowiedź na zadanie z Baz Danych). Zakładamy, ze użytkownik zawsze wpisze poprawny numer jednak zapytanie SQL powinno być w prostu sposób parsowane (poprzez wyszukanie słów kluczowych SELECT, FROM, WHERE, ORDER BY i określenie czy podane były w danej kolejności, czy w złym porządku). W przypadku złego porządku odpowiedź nie jest zapisywana a użytkownik otrzymuje komunikat o błędzie.

Każde uruchomienie tworzy nowy plik odpowiedzi (program nie odczytuje żadnych danych).

W przypadku podania dwa razy tego samego numeru zadania odpowiedź jest nadpisywana.

    - co 30 sekund licząc od pełnych minut wpisane odpowiedzi zostają automatycznie zapisane do pliku odp.txt. Odpowiedzi w pliku mają być posortowane względem numerów zadań. (Uwaga! Użytkownik może w programie wpisywać odpowiedzi w dowolnej kolejności).

    - co pełną minutę od Pn-PT w godzinach 8.15-18.45 będzie pokazywać na ekranie komunikat "X minut do końca zajęć/przeryw". Zamodeluj godziny zajęć i przerw jak na WMI UAM.

Napisz testy do danych klas - co najmniej dla metody sprawdzającej poprawność zapytania SQL, oraz metody sprawdzającej czy dany czas jest przerwą czy zajęciami.