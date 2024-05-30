"""Viết chương trình tìm thừa số nguyên tố lớn nhất của một số nguyên dương

Ví dụ:

Input: 6
Output: 3
Giải thích:
Các thừa số nguyên tố của 6 là 2, 3
nên thừa số nguyên tố lớn nhất là 3 
"""

def tim_thua_so_nguyen_to_lon_nhat(n):
    max = 1
    for i in range(2, int(n**0.5) + 1):
        while n % i == 0:
            max = i
            n //= i
    if n > 1:
        max = n
    return max

n = int(input("n = "))

print(tim_thua_so_nguyen_to_lon_nhat(n))
