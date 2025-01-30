a = float(input("Vvedite chislo 1: "))
b = float(input("VVedite chislo 2: "))
c = float(input("Vvedite chislo 3: "))

maxchislo = a
minchislo = a

if b > maxchislo:
    maxchislo = b
if c > maxchislo:
    max_value = c

if b < minchislo:
    minchislo = b
if c < minchislo:
    minchislo = c

print(f"Max: {maxchislo}")
print(f"Min: {minchislo}")