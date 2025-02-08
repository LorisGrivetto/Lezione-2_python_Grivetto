kg = int(input("Inserisci i kg di pesche: "))  
prezzo_kg = int(input("Inserisci il prezzo al kg delle pesche: "))  

totale = kg * prezzo_kg  
print("Totale da pagare:", totale, "euro")  

contanti = int(input("Inserisci i contanti dati dal cliente: "))  
resto = contanti - totale  

print("Resto dovuto:", resto, "euro")  
