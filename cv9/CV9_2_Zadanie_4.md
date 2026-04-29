## Zadanie 4 (5b)

V tomto zadaní budete pracovať s nástrojom MetaboAnalyst a datasetom: **NMR spectral bins**
    
`Binned 1H NMR spectra of 50 urine samples using 0.04 ppm constant width (Psihogios NG, et al.) Group 1- control; group 2 - severe kidney disease.`
    
Tento dataset je dostupný v sekcii 'Try our test data' v nástroji pre Jednofaktorovú štatistickú analýzu. 

Dataset pochádza z NMR-metabolomickej štúdie: Hodnotenie závažnosti tubulointersticiálnych lézií u pacientov s glomerulonefritídou. Začiatok tubulointersticiálnych lézií je charakterizovaný zníženým vylučovaním citrátu, hipurátu, glycínu a kreatinínu, zatiaľ čo po ďalšom zhoršení nasleduje glykozúria, selektívna aminoacidúria, úplné vyčerpanie citrátu a hipurátu a postupné zvyšovanie vylučovania laktátu, acetátu a trimetylamín-N-oxidu. Metabonomická analýza moču založená na NMR by mohla prispieť k včasnému hodnoteniu závažnosti poškodenia obličiek a prípadne k monitorovaniu ich funkcie. [1]


Načítajte množinu údajov v nástroji MetaboAnalyst. Pri filtrovaní údajov (Data filter) môžete použiť predvolené nastavenia.

### Úloha 1 (1b)

Normalizujte distribúciu datasetu (pre premenné aj vzorku).
(Vyberte akúkoľvek kombináciu operácií, ktorá je podľa Vás najlepšia).

**Ktoré operácie ste pri normalizácii použili?**
Sample normalization: Normalization by median
Data Transformation: Square root transformation
Data Scaling: Auto scaling
### Úloha 2 (4b)

Použite ľubovoľné štatistické metódy na analýzu datasetu (napr. t-test, correlations, PCA, PLS-DA, Dendrogram, Heatmap, K-means, RandomForest, ..) 

**Uveďte aspoň 4 skutočnosti (z 4 rôznych metód), ktoré ste zistili analýzou datasetu:**

(Napr. Pri použití pearsonovho korelačného koeficientu je najvyššia pozitívna korelácia medzi premennými x a y, a koeficient korelácie je 0.992.)

1: Pri použití t-testu bolo pri hranici p-value 0,05 a FDR korekcii nájdených 100 štatisticky významných premenných a 90 premenných nebolo štat. významných. Z toho vyplýva, že medzi skupinou control a patient je viacero rozdielov v NMR spektrálnych binoch.

2: Pri metóde Random Forest vyšiel OOB error 0,06, čo znamená približne 6 % chybovosť klasifikácie. Podľa confussion matrix bolo všetkých 25 vzoriek zo skupiny control zaradených správne. Zo skupiny patient bolo správne zaradených 22 z 25 vzoriek a 3 boli nesprávne.

3: Pri korelačnej analýze pomocou Pearsonovho korelačného koeficientu bola zistená silná pozitívna korelácia medzi premennými Bin.7.62 a Bin.7.58. Korelačný koeficient bol 0,952, čo znamená, že tieto dve spektrálne oblasti sa vo vzorkách menili veľmi podobne.

4: Pri hierarchickej heatmape bolo vidieť rozdielne vzory hodnôt medzi skupinami control a patient. Napríklad pri premennej Bin.8.30 mala vzorka P100b hodnotu 4,04, čo patrilo medzi výrazne vyššie hodnoty. Na heatmape bolo vidieť, že niektoré biny majú vyššie hodnoty najmä u pacientov a iné skôr v kontrolnej skupine. To naznačuje, že metabolomický profil pacientov sa veľmi líši od kontrolnej skupiny...

Vygenerujte report z vykonanej analýzy a celý výsledný zip file odovzdajte ako prílohu k riešeniu zadania.

----

#### Referencie

[1] Psihogios, N. G., Kalaitzidis, R. G., Dimou, S., Seferiadis, K. I., Siamopoulos, K. C., & Bairaktari, E. T. (2007). Evaluation of tubulointerstitial lesions’ severity in patients with glomerulonephritides: an NMR-based metabonomic study. Journal of Proteome Research, 6(9), 3760–3770. https://doi.org/10.1021/PR070172W
