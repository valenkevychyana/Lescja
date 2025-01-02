rozmiar = int(input("Podaj rozmiar boku kwadratu: "))
for _ in range(rozmiar):
    print('*' * rozmiar)

#Zadanie 2
szerokosc = int(input("Podaj szerokość prostokąta: "))
wysokosc = int(input("Podaj wysokość prostokąta: "))

for _ in range(wysokosc):
    print('*' * szerokosc)

#Zadanie 3
rozmiar = int(input("Podaj rozmiar boku kwadratu: "))
for i in range(rozmiar):
    if i == 0 or i == rozmiar - 1:
        print('*' * rozmiar) 
    else:
        print('*' + ' ' * (rozmiar - 2) + '*')


#Zadanie 4
dlugosc = int(input("Podaj długość prostokąta: "))
szerokosc = int(input("Podaj szerokość prostokąta: "))
for i in range(szerokosc):
    if i == 0 or i == szerokosc - 1:
        print('*' * dlugosc)
    else:
        print('*' + ' ' * (dlugosc - 2) + '*')
        