# lab01-NTPD

**Lista różnic i wyzwań, które pojawiają się przy wdrażaniu modelu ML w środowisku produkcyjnym:**

**1. Stabilność vs. eksperymenty**

W środowisku deweloperskim model jest testowany i często zmieniany. W produkcji musi działać stabilnie, przewidywalnie i bez przerw.
**Jak sobie radzić:** CI/CD, testy automatyczne, wersjonowanie modeli (np. MLflow), wdrożenia typu blue-green lub canary.

**2. Dane treningowe vs. dane rzeczywiste (data drift)**

W dev pracujemy na statycznym zbiorze danych. W produkcji dane mogą zmieniać rozkład (data drift), co obniża skuteczność modelu.
**Jak sobie radzić:** monitorowanie rozkładu danych i metryk (np. accuracy, F1), alerty, okresowy retraining modelu.

**3. Jednorazowe trenowanie vs. ciągły retraining**

W dev model trenuje się „raz”. W produkcji wymaga regularnego aktualizowania.
**Jak sobie radzić:** pipeline MLOps (np. Airflow), automatyczne ponowne trenowanie przy wykryciu spadku jakości.

**4. Lokalne środowisko vs. infrastruktura produkcyjna**

W dev wszystko działa na jednym komputerze. W produkcji model działa w chmurze lub klastrze (Docker, Kubernetes).
**Jak sobie radzić:** konteneryzacja (Docker), Infrastructure as Code, kontrola wersji środowiska.

**5. Zależności i wersje bibliotek**

W dev łatwo zmienić wersję biblioteki. W produkcji konflikt zależności może zatrzymać system.
**Jak sobie radzić:** requirements.txt / poetry.lock, Docker, dokładne wersjonowanie pakietów.

**6. Opóźnienia i skalowalność**

W dev nie liczy się czas odpowiedzi. W produkcji ważne są latency i obsługa wielu użytkowników.
**Jak sobie radzić:** optymalizacja modelu (quantization, batching), autoskalowanie, cache.

**7. Brak monitoringu vs. monitoring ciągły**

W dev patrzymy na metryki offline. W produkcji trzeba stale obserwować działanie systemu.
**Jak sobie radzić:** logowanie predykcji, dashboardy (Prometheus, Grafana), alerty przy spadku jakości.

**Podsumowanie:**

Wdrożenie ML w produkcji wymaga podejścia inżynieryjnego (MLOps), nie tylko analizy danych. Największe wyzwania to stabilność, zmienność danych, skalowalność oraz automatyzacja całego cyklu życia modelu.
