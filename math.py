a = 10
b = 10

def penjumlahan(a,b):
    return a + b

def pengurangan(a,b):
    return a - b

def perkalian(a,b):
    return a * b

def pembagian(a,b):
    return a / b
    if b == 0:
        return "Tidak bisa dibagi dengan 0"
    
result = penjumlahan(a,b)
print(result)
