"""
Viết chương trình tính tích các thừa số nguyên tố duy nhất của một số nguyên dương

Ví dụ:

Input: 44
Output: 22
vì các thừa số của 44 là 2, 2, 11
nên tích số cần tìm = 2*11 = 22
"""

def tich_thua_so_nguyen_to(n):
    i = 2
    result = 1
    while i <= n:
        if n % i == 0:
            result *= i
            while n % i == 0:
                n /= i
        i += 1
    return result
n = int(input())
print(tich_thua_so_nguyen_to(n))

