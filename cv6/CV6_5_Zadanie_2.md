## Zadanie 2 (5b)

V tomto zadaní budete pracovať s aplikáciou v adresári `machine_learning` a datasetom: **Breast Cancer Wisconsin (Diagnostic)**

Dataset je dostupný aj online samostatne, alebo v knižnici scikit-learn: 
https://archive.ics.uci.edu/dataset/17/breast+cancer+wisconsin+diagnostic
https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_breast_cancer.html

Dataset Breast Cancer Wisconsin (Diagnostic) obsahuje údaje získané z digitalizovaných obrazov tenkých ihlových aspirátov (FNA) hmoty prsníka, ktoré opisujú charakteristiky jadier buniek v nich. Zahŕňa 569 prípadov s 30 vlastnosťami, s cieľom na klasifikáciu benigných alebo maligných prípadov rakoviny prsníka na základe rôznych vlastností jadier buniek. Viac informácií nájdete na UCI Machine Learning Repository. [1]

### Úloha 1 (1b)

Pridajte do kódu ďalší model strojového učenia (ľubovoľný), a taktiež definujte parametre a ich hodnoty pre Grid Search.

**Uveďte aký ML model a hodnoty jeho parametrov ste použili:**

1.
Do projektu som pridal ďalší model strojového učenia konkrétne K-Nearest Neighbors (KNN, ktorý som našiel na internete). 
Tento model funguje na princípe hľadania najbližších susedov a rozhodovania podľa nich (daných susedov).

pre Grid Search som nastavil tieto parametre:
- n_neighbors: 3, 5, 7, 9 ( t. j. počet susedov)
- uniform a distance ( váhovanie susedov )
- euclidean a manhattan ( spôsoby výpočtov vzdialeností )

### Úloha 2 (2b)

Implementujte ďalšiu (ľubovoľnú) metriku pre evaluáciu modelov. Nezabudnite na to, aby sa implementovaná metrika ukladala do logov v súbore `model_accuracies.csv` a tiež ju pridajte do grafov (do grafov pre funkciu hustoty rozdelenia a tiež pre ňu vytvorte nový graf ktorý bude zobrazovať jej priebeh počas replikácií - tak ako pre presnosť (accuracy)).  

**Uveďte akú metriku ste doplnili:**

Nová doplnená metrika PRECISION ukazuje, aký podiel pozitívnych predikcií modelu bol správny. (pridané aj do triedy modeltrainer + výsledkov df + grafy)

### Úloha 3 (1b)

Do implementácie pridajte ukladanie všetkých grafov, ktoré sa vytvárajú pri behu skriptu `main.py`` v adresári `machine_learning`.

### Úloha 4 (1b)

**V skripte `main.py`** nastavte počet replikácií na vyššie číslo (rozumne, podľa vlastného uváženia). Vykonajte beh aplikácie s Vašou implementáciou. Po skončení behu zanalyzujte vygenerované grafy a pár vetami popíšte ich interpretáciu. (Napr. v čom je ktorý ML model lepší, a pod.)

Po nastavení až 30 replikácií boli výsledky oveľa stabilnejšie, a teda bolo možné lepšie porovnať modely.
Z density grafu accuracy je vidieť, že oba modely dosahujú veľmi podobné výsledky okolo hodnoty 0.97. 
Logistic Regression má mierne širšie rozdelenie smerom k vyšším hodnotám, takže v niektorých prípadoch dosahuje o trošku lepšie výsledky. 
KNN má naopak mierne užšie rozdelenie, takže jeho výsledky sú "konzistentnejšie".
A pri F1-score je situácia podobná ako pri accuracy. Oba modely majú veľmi podobné hodnoty, ale Logistic Regression dosahuje mierne vyššie maximá.

Z grafu ROC AUC (roc_auc_density.png) je vidieť, že Logistic Regression dosahuje veľmi vysoké a stabilné hodnoty blízko 1.0, takže veľmi dobre rozlišuje medzi triedami. 
KNN má rozdelenie širšie a posunuté nižšie, čiže má o niečo horšiu schopnosť rozlišovania.

Pri metrike precision je zaujímavé, že KNN má mierne vyššie hodnoty ako Logistic Regression. 
To znamená, že KNN robí menej falošne pozitívnych predikcií (FP), čo môže byť niekedy výhoda.
Z grafov priebehu (replications) je vidieť, že oba modely majú podobný priemer accuracy aj precision (okolo 0.97), ale KNN má väčšie výkyvy medzi jednotlivými replikáciami, 
zatiaľ čo Logistic Regression je stabilnejšia.

Z confusion matrix vyplýva, že oba modely klasifikujú väčšinu prípadov správne, 
keďže najvyššie hodnoty sú na diagonále. Logistic Regression má menej false negatives (2.97) ako KNN (4.20), čo znamená, 
že lepšie zachytáva pozitívne prípady (už konkrétne maligné nádory). KNN má menej FPs.

Celkovo môžem povedať, že Logistic Regression je stabilnejší model s lepším ROC AUC a menším počtom false negatives, zatiaľ čo KNN má trochu lepšiu precision, ale je menej stabilný.

**Odovzdávanie riešenia:** Ako súčasť riešenia zahrňte okrem odpovedí na otázky aj skripty s Vašou implementáciou, vygenerované logy a grafy (všetko môžete dať na Github).

----

#### Referencie

[1] Street, W. N., Wolberg, W. H., & Mangasarian, O. L. (1993). Nuclear feature extraction for breast tumor diagnosis. Electronic Imaging, 1905, 861–870. https://doi.org/10.1117/12.148698
