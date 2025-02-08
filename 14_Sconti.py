prezzo1 = int(input("Inserisci il prezzo del primo paio di jeans: "))  
prezzo_scontato1 = prezzo1 - prezzo1 * 0.20  

prezzo2 = int(input("Inserisci il prezzo del secondo paio di jeans: "))  
prezzo_scontato2 = prezzo2 - prezzo2 * 0.20  

totale = prezzo_scontato1 + prezzo_scontato2  
print("Il totale scontato è:", totale, "euro")  

contanti = int(input("Inserisci i contanti: "))  
resto = contanti - totale  

print("Resto dovuto:", resto, "euro")  
