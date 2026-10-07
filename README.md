# Analiza preturilor apartamentelor

Proiect Python care genereaza un set de date cu apartamente, il analizeaza statistic si il reprezinta grafic.

## Setul de date

20 de apartamente generate automat (`apartments.json`), fiecare cu atributele:

| Atribut | Descriere |
|---|---|
| `location` | zona (Centru, Floreasca, Dristor, Berceni, Drumul Taberei, Titan, Militari) |
| `rooms` | numar de camere (1-4) |
| `surface_m2` | suprafata in m2 |
| `floor` | etajul (0-10) |
| `bathrooms` | numar de bai (1-2) |
| `distance_to_transport_m` | distanta pana la transportul public, in metri |
| `price` | pretul |

Datele nu sunt complet aleatorii: pretul depinde de suprafata, de zona (Centru si Floreasca sunt mai scumpe, Militari mai ieftin) si scade usor cu distanta fata de transport, plus o mica variatie aleatorie. Astfel graficele arata relatii vizibile. `random.seed(42)` face ca datele sa fie mereu aceleasi.

## Structura proiectului

```
PythonProject/
├── main.py              # punctul de intrare: ruleaza toate cerintele
├── generate_data.py     # genereaza apartments.json (se ruleaza o singura data)
├── data_loader.py       # citeste JSON-ul intr-un DataFrame pandas
├── analysis.py          # calculele (min/max, prag, medie, abatere standard)
├── plots.py             # toate graficele
├── apartments.json      # datele generate
└── README.md
```

Codul este impartit pe fisiere dupa responsabilitate: date, calcule, grafice si fisierul principal care le leaga.

## Cum se ruleaza

1. Instalare biblioteci: `pip install pandas matplotlib numpy`
2. (Optional) Regenerare date: `python generate_data.py`
3. Rulare: `python main.py`

Programul afiseaza rezultatele in terminal, cere un prag de pret de la tastatura, apoi deschide cele 3 ferestre cu grafice.

## Cum este rezolvata fiecare cerinta

### 1. Fisierul de date si pretul minim / maxim
`generate_data.py` creeaza fisierul JSON, iar `data_loader.py` il citeste cu `pd.read_json`. In `analysis.py`, `find_min_max` foloseste `idxmin()` si `idxmax()` pe coloana `price` pentru a gasi randurile corespunzatoare. Se afiseaza toate caracteristicile celor doua apartamente, nu doar pretul.

### 2. Grafic suprafata vs pret
`plot_scatter` deseneaza un scatter plot cu suprafata pe axa X si pretul pe axa Y. Fiecare punct este un apartament.

### 3. Preturi peste un prag
Pragul se citeste cu `input()` in terminal. `count_above` numara cate preturi sunt strict mai mari decat acesta: `(df["price"] > threshold).sum()`.

### 4. Medie, abatere standard, boxplot si violin plot
`price_stats` calculeaza media si abaterea standard a preturilor. `plot_box_violin` afiseaza doua grafice una langa alta:
- **Boxplot**: sumar statistic (mediana, cuartile, valori extreme).
- **Violin plot**: forma distributiei, adica unde sunt concentrate preturile. Include marcaje pentru medie si mediana.

### 5. Grafic radar
Se compara 3 apartamente: cel cu pret minim, cel cu pret maxim si cel al carui pret este cel mai apropiat de medie (`find_closest_to_mean`). Atributele folosite sunt suprafata, camerele, bailor, etajul, distanta pana la transport si pretul.

Atributele au scari foarte diferite (pretul e in zeci de mii, camerele intre 1 si 4), deci fiecare este **normalizata min-max** intre 0 si 1:

```
valoare_normalizata = (valoare - minim) / (maxim - minim)
```

Minimul si maximul se iau din tot setul de date, nu doar din cele 3 apartamente. Distanta pana la transport ramane normalizata la fel ca celelalte atribute: valoare mare inseamna departe de transport.

## Rezultate obtinute (cu `seed=42`)

- Cel mai ieftin apartament: **30.600** (Dristor, 1 camera, 25 m2, etaj 5).
- Cel mai scump apartament: **202.400** (Centru, 4 camere, 104 m2, etaj 6).
- Pret mediu: **89.850**.
- Abatere standard: **49.637**.

## Tehnologii

- **pandas**: citirea datelor si calcule pe coloane
- **matplotlib**: scatter, boxplot, violin plot si radar
- **numpy**: calculul unghiurilor pentru radar
