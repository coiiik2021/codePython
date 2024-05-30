"""Viết chương trình kiểm tra biểu diễn nhị phân của một số nguyên dương có phải là Palindrome không?

Ví dụ:

Input: 9
Output: True
vì biểu diễn nhị phân của 9 là 1001 (là palindrome)

Input: 10
Output: False
vì biểu diễn nhị phân của 10 là 1010 (không là palindrome)"""

def kiem_tra_palindrome(n):
    binary = bin(n)[2:]  
    return binary == binary[::-1]  

n = int(input())

print(kiem_tra_palindrome(n))
