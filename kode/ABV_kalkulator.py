"""
Author: Erik Mellem Arnesen & Tor Markus Tønnesen
Date: 04.04.25
Purpose: Beregne alkohol prosent (ABV - Alcohol by volume)
"""

def beregn_abv(og, fg):
    abv = (og - fg) * 131.25
    return round(abv, 2)

og = float(input("Skriv inn Original Gravity (OG): "))
fg = float(input("Skriv inn Final Gravity (FG): "))

abv = beregn_abv(og, fg)
print(f"Alkoholprosent (ABV) er: {abv}%")