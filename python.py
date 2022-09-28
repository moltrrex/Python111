#realizar un codigo que encuentre cuantas vocales hay en una frase
#en python

frase = str(input("digite una frase"))
vocales = "aeiouAEIOU"
n = []

for i in frase:
    if i in vocales:
        n.append(i)
        
print(len(n))