import random

def printList(lst):
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            print(lst[i][j], end='    ')
        print()

n = 4
m = 4
a = []
for i in range(n):
    a.append([])
    for j in range(m):
        a[i].append(random.randint(2, 6))

print("İki ölçülü A(n,m) ədədi massivi:")
printList(a)
print()

# Elemanları toplamı pozitif olan satırların numaralarını bulma
print("Elementləri cəmi müsbət olan sətrin nömrələri:")
for i in range(n):
    row_sum = sum(a[i])
    if row_sum > 0:
        print(f"{i+1}-ci setr: toplam = {row_sum}")
