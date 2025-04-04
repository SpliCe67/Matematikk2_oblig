"""
Author: Tor Markus Tønnesen & Erik Mellem Arnesen
Date: 04.04.25
Purpose: Kalkulere Bitterhetbidrag i IBU (Internation bitternes units) fra humle ved bruk av Tinseth approksimasjonen 
"""
import numpy as np

def beregn_ibu(aa_prosent, humle_gram, koketid_min, batch_vol, og):
    aa_prosent = aa / 100
    utnyttelse = 1.65 * 0.000125**(og - 1) * ((1 - np.exp(-0.04 * koketid_min)) / 4.15)
    ibu = (aa_prosent * humle_gram * 1000 / batch_vol) * utnyttelse
    return round(ibu, 2)

aa = float(input("Alfasyreprosent (skriv f.eks. 5 for 5%): "))
humle_gram = float(input("Humlemengde i gram: "))
koketid_min = float(input("Koketid i minutter: "))
batch_vol = float(input("Volum vørter i liter: "))
og = float(input("Original Gravity (f.eks. 1.050): "))

ibu = beregn_ibu(aa, humle_gram, koketid_min, batch_vol, og)
print(f"IBU-bidrag fra humlen er: {ibu}")
