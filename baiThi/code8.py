#Viết chương trình chuyển vị một ma trận, trong đó thao tác chuyển vị được thực hiện bằng 1 dòng lệnh duy nhất. 
import numpy as np


m = int(input("Nhập số hàng: "))
n = int(input("Nhập số cột: "))

arr = []
for i in range(m):
    row = [int(element) for element in input("Nhập hàng {}: ".format(i)).split()]
    arr.append(row)

arr = np.array(arr)

kq = np.transpose(arr)

print(kq)

