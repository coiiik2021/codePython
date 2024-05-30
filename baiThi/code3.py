#Viết chương trình tạo ra ma trận  n * n  chứa  n*n  số nguyên dương đầu tiên,  bằng cách sử dụng list comprehension.

def tao_ma_tran(n):
    return [[i + j*n for i in range(1, n+1)] for j in range(n)]

n = int(input())

ma_tran = tao_ma_tran(n)
for row in ma_tran:
    print(row)

