def Coulomb(num1, num2, r):
    k = 9*10**9
    b = r*10**-2
    answer = (k*num1* num2)/(b*b)
    return answer

def Multiply(num1, num2, rank):
	return num1*num2**rank
	
y = int(input("Masukkan angka ke-: "))
p = int(input("Masukkan angka ke-2: "))
q = int(input("Masukkan pangkat: "))
hasil1 = Multiply(y, p, q)

je = int(input("Masukkan angka ke-1: "))
ha = int(input("Masukkan angka ke-2: "))
wj = int(input("Masukkan pangkat: "))
hasil2 = Multiply(je, ha, wj)

y = int(input("masukkan distance: "))

h = Coulomb(hasil1, hasil2, y)
print(f"F: {h}N")