s = input('Введите элементы через пробел')
s=s.split()
s1 = [int(i) for i in s]
def f(L):
    if not L: return None
    b = L[0]
    m = 0
    for i in L:
        c = L.count(i)
        if c > m:
            m = c
            b = i
        elif c == m and i < b:
            b = i
    return b
print(f(s1))