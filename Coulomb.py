def Coulomb(num1, num2, r):
    k = 9*10**9
    b = r*10**-2
    answer = (k*num1* num2)/(b*b)
    return answer

def Multiply(num1, num2, rank):
    return num1*num2**rank
	
a = int(input("Masukkan angka ke-1: "))
b = int(input("Masukkan angka ke-2: "))
c = int(input("Masukkan pangkat: "))
Q1 = Multiply(a, b, c)

d = int(input("Masukkan angka ke-1: "))
e = int(input("Masukkan angka ke-2: "))
f = int(input("Masukkan pangkat: "))
Q2 = Multiply(d, e, f)

r = int(input("masukkan jarak: "))

h = Coulomb(Q1, Q2, r)
print(f"F: {h} N")
