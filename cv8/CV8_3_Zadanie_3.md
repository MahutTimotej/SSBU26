## Zadanie 3 (5b)

V tomto zadaní budete pracovať s nástrojom FamLinkX a datasetom **dna_screening_zadanie** dostupným v priečinku `inputs`. 

Dataset obsahuje údaje matky, dcéry a dvoch strýkov, ktorí sú bratmi muža, u ktorého predpokladáme, že je otcom dcéry. Je potrebné potvrdiť alebo vyvrátiť či bol muž otcom dievčaťa. Pomocou nástroja FamLinkX zostavte hypotézy s rodokmeňom členov, vykonajte analýzu, určte výsledné pravdepodobnosti hypotéz a uveďte výsledné rozhodnutie na potvrdenie/zamietnutie otcovstva.

<img src="data/family_tree.png" width="100%"/>

### Úloha 1 (1b)

**Formulujte hypotézy pre riešenie úlohy:**

H0: Testovaný otec(S0) je biologický otec dcéry(D).
(možný doplnok: Tiež možno dodať, že zároveň obidvaja testovaní muži(S1;S2) sú biologickí strýkovia dcéry(D).)

HA: Testovaný otec(S0) nie je biologický otec dcéry(D).


### Úloha 2 (4b)

Vykonajte analýzu pomocou nástroja FamLinkX. Ako referenčnú databázu použite Českú alebo Nemeckú databázu. Ako prílohu zadania odovzdajte vygenerovaný report z analýzy (Case report vo formáte .rtf). 

**Uveďte LR a pravdepodobnosť (W) pre jednotlivé hypotézy a Váš záver analýzy:**

Analýza som urobil v programe FamLinkX s CZE databázou. Základnú hypotézu som vybral Two Aunts/Uncles a ako alternatívnu hypotézu Two Full Siblings One Unrelated.

Výsledok analýzy:
LR (Exact) = 7.12e+004 = 71 200

Pravdepodobnosť hypotézy H0:
W = 0,99998596
W = 99,998596 %

Pravdepodobnosť alternatívnej hypotézy HA:
W = 1,4044079e-005
W = 0,001404 %

Na základe výsledkov je hypotéza H0 výrazne pravdepodobnejšia ako alternatívna hypotéza, a teda môžem vytvoriť záver, že prijímam základnú hypotézu a tvrdím, že testovaný človek JE biologický otec dcéry. Hodnota LR a pravdepodobnosti sú vysoke, čo znamená, že podporujú príbuzenský vzťah medzi dieťaťom a strýkami. Preto môžeme predpokladané otcovstvo považovať za veľmi pravdepodobné. (Možno je potrebné dodať, že len v prípade, ak sme si istí, že otcom nemôže byť jeden zo strýkov.)