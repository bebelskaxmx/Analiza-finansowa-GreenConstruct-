import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


projekty = pd.read_csv('projekty.csv')
rzis = pd.read_csv('rzis.csv')
bilans = pd.read_csv('bilans.csv')
cashflow = pd.read_csv('cashflow.csv')


print("=== Projekty ===")
print(projekty, "\n")

print("=== Rachunek Zysków i Strat ===")
print(rzis, "\n")

print("=== Bilans ===")
print(bilans, "\n")

print("=== Cash Flow ===")
print(cashflow, "\n")


projekty['Zysk'] = projekty['Przychód'] - (
    projekty['Koszt materiałów'] +
    projekty['Koszt robocizny'] +
    projekty['Koszt podwykonawców'] +
    projekty['Pozostałe koszty']
)
projekty['Marża [%]'] = projekty['Zysk'] / projekty['Przychód'] * 100

print("=== Zysk i marża dla każdego projektu ===")
print(projekty[['Projekt', 'Zysk', 'Marża [%]']])


sns.set(style="whitegrid")
plt.figure(figsize=(8, 5))
sns.barplot(x='Projekt', y='Zysk', data=projekty, palette='crest')
plt.title('Zysk netto na projekt')
plt.ylabel('Zysk [PLN]')
plt.xlabel('Projekt')
plt.tight_layout()
plt.show()

#podstawowe wskaźniki finansowe z RZiS i bilansu


rzis_dict = dict(zip(rzis['Pozycja'], rzis['PLN']))
bilans_dict = dict(zip(bilans['Pozycja'], bilans['PLN']))

# Wskaźniki finansowe

# Rentowność netto - Ile procent z przychodów zostaje jako zysk
rentownosc_netto = rzis_dict['Zysk netto'] / rzis_dict['Przychody ze sprzedaży'] * 100

# ROA - zwrot z aktywów - Jak efektywnie firma wykorzystuje cały majątek

aktywa_razem = bilans_dict['Aktywa trwałe'] + bilans_dict['Aktywa obrotowe']
roa = rzis_dict['Zysk netto'] / aktywa_razem * 100

# ROE - zwrot z kapitału własnego - Jak opłaca się właścicielowi inwestować kapitał

roe = rzis_dict['Zysk netto'] / bilans_dict['Kapitał własny'] * 100

# Wskaźnik płynności bieżącej - Czy firma ma z czego spłacić bieżące zobowiązania

plynnosc_biezaca = bilans_dict['Aktywa obrotowe'] / bilans_dict['Zobowiązania krótkoterminowe']

# Wskaźnik zadłużenia ogólnego - Jak duża część majątku pochodzi z kredytów


zadluzenie = (bilans_dict['Zobowiązania krótkoterminowe'] + bilans_dict['Zobowiązania długoterminowe']) / aktywa_razem * 100


print("\n=== Wskaźniki finansowe ===")
print(f"Rentowność netto: {rentownosc_netto:.2f}%")
print(f"ROA (zwrot z aktywów): {roa:.2f}%")
print(f"ROE (zwrot z kapitału własnego): {roe:.2f}%")
print(f"Płynność bieżąca: {plynnosc_biezaca:.2f}")
print(f"Zadłużenie ogólne: {zadluzenie:.2f}%")

#wizualizacja 
# wykres wskażników
wskazniki = {
    'Rentowność netto [%]': rentownosc_netto,
    'ROA [%]': roa,
    'ROE [%]': roe,
    'Płynność bieżąca': plynnosc_biezaca,
    'Zadłużenie ogólne [%]': zadluzenie
}


plt.figure(figsize=(10, 5))
sns.barplot(x=list(wskazniki.keys()), y=list(wskazniki.values()), palette='muted')
plt.title("Wskaźniki finansowe – GreenConstruct")
plt.ylabel("Wartość")
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()

#generuje sb tabelke
from tabulate import tabulate

dane = [
    ["Rentowność netto", "5,13%"],
    ["ROA", "21,10%"],
    ["ROE", "39,44%"],
    ["Płynność bieżąca", "1,50"],
    ["Zadłużenie ogólne", "46,51%"]
]

print(tabulate(dane, headers=["Wskaźnik", "Wartość"], tablefmt="fancy_grid"))



#tabelka wyniki projektow

import matplotlib.pyplot as plt

dane = [
    ["Dom jednorodzinny", "200 000", "23,5%"],
    ["Remont kamienicy", "52 000", "12,4%"],
    ["Termomodernizacja szkoły", "95 000", "19,0%"]
]

naglowki = ["Projekt", "Zysk (PLN)", "Marża (%)"]

fig, ax = plt.subplots(figsize=(7, 2.5))  # rozmiar obrazka
ax.axis('off')  # wyłącz osie

table = ax.table(
    cellText=dane,
    colLabels=naglowki,
    cellLoc='center',
    colLoc='center',
    loc='center'
)

table.auto_set_font_size(False)
table.set_fontsize(12)
table.scale(1.2, 1.5)

plt.savefig("moja_tabela.png", bbox_inches='tight', dpi=300)
plt.show()


#tabelka do wskażników finansowych

import matplotlib.pyplot as plt

dane = [
    ["Rentowność netto", "5,13%"],
    ["ROA", "21,10%"],
    ["ROE", "39,44%"],
    ["Płynność bieżąca", "1,50"],
    ["Zadłużenie ogólne", "46,51%"]
]

naglowki = ["Wskaźnik", "Wartość"]

fig, ax = plt.subplots(figsize=(6, 2.5))  # rozmiar: możesz zmienić np. (7, 3)
ax.axis('off')

tabela = ax.table(
    cellText=dane,
    colLabels=naglowki,
    cellLoc='center',
    colLoc='center',
    loc='center'
)

tabela.auto_set_font_size(False)
tabela.set_fontsize(12)
tabela.scale(1.2, 1.5)

plt.savefig("tabela_wskazniki_finansowe.png", bbox_inches='tight', dpi=300)
plt.show()
