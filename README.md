# Predykcja cen samochodów
Ten projekt ma na celu przewidywanie cen samochodów za pomocą różnych modeli regresji. Dane do projektu zostały pobrane z Kaggle, a następnie poddane procesom czyszczenia, wizualizacji oraz tworzenia modeli regresji w celu dokładnego przewidywania cen.

# Opis Projektu
1. Pobieranie Danych:
  Dane zostały pobrane z Kaggle i zawierają różne cechy samochodów, takie jak marka, model, rok rejestracji, pojemność silnika itd.
  
2. Czyszczenie Danych:
  Dane zostały oczyszczone poprzez uzupełnianie brakujących wartości, usuwanie duplikatów oraz poprawianie nieścisłości.
  Przeprowadzono inżynierię cech, aby utworzyć nowe, istotne cechy oraz przekształcić istniejące w celu poprawy wydajności modeli.

3. Wizualizacja Danych:
  Został utworozny dashboard za pomocą biblioteki streamlit, w celu wizualizacji najważniejszych cech - aby uruchomić dashboard należy w terminalu wpisać komendę streamllit run cars_visualization.py.

4. Tworzenie Modeli:
  Utworzono wiele modeli regresji w celu przewidywania cen samochodów, w tym:
  Regresja Liniowa
  Regresja Drzewa Decyzyjnego
  Regresja Lasu Losowego

  Wydajność modeli była oceniana za pomocą takich metryk jak średni błąd bezwzględny (MAE), średni błąd kwadratowy (MSE) oraz współczynnik determinacji (R-kwadrat).
  
5. Wyniki:
  Modele zostały porównane na podstawie ich metryk wydajności.
  Najlepiej działający model został wybrany do przewidywania cen samochodów na nowych danych.
