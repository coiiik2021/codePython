#Viết chương trình nhân 2 ma trận bằng cách sử dụng list comprehension.

m1 = int(input("Nhập số hàng của ma trận 1: "))
n1 = int(input("Nhập số cột của ma trận 1: "))
m2 = int(input("Nhập số hàng của ma trận 2: "))
n2 = int(input("Nhập số cột của ma trận 2: "))


if n1 != m2:
    print("Không thể nhân hai ma trận với số hàng của ma trận 1 khác số cột của ma trận 2")
else:
    print("Nhập ma trận 1:")
    arr1 = []
    for i in range(m1):
        row = [int(element) for element in input("Nhập hàng {}: ".format(i)).split()]
        arr1.append(row)

    print("Nhập ma trận 2:")
    arr2 = []
    for i in range(m2):
        row = [int(element) for element in input("Nhập hàng {}: ".format(i)).split()]
        arr2.append(row)

    kq = [[sum(arr1[i][k] * arr2[k][j] for k in range(n1)) for j in range(n2)] for i in range(m1)]

    print("Ma trận kết quả:")
    for row in kq:
        print(row)
