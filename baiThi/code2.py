"""
Tìm cột thứ K của một ma trận là bài toán phổ biến trong lĩnh vực Học Máy.
Hãy viết chương trình tạo  tìm cột thứ K của ma trận,  bằng cách sử dụng list comprehension.



Output mẫu: 

The original list is : [[4, 5, 6], [8, 1, 10], [7, 12, 5]]
K = 2
The Kth column of matrix is : [6, 10, 5]
"""

def lay_cot_thu_k(arr, k):
    return [row[k] for row in arr]

m = int(input("Nhập số hàng: "))
n = int(input("Nhập số cột: "))
arr = []
for i in range(m):
    row = []
    for j in range(n):
        element = int(input("Nhập phần tử arr[{}][{}]: ".format(i, j)))
        row.append(element)
    arr.append(row)

k = int(input("Nhập cột k: "))

print(lay_cot_thu_k(arr, k))

