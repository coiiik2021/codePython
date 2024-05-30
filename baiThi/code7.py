"""Cho hai số N và K, nhiệm vụ của chúng ta là trừ số K từ N cho đến khi số (N) lớn hơn 0,
khi N trở thành số âm hoặc 0 thì chúng ta bắt đầu cộng K cho đến khi số đó trở thành số (N) ban đầu.
Lưu ý: Không cho phép sử dụng bất kỳ vòng lặp nào.

Ví dụ:

Input : N = 15 K = 5
Output : 15 10 5 0 5 10 15
Input : N = 20 K = 6
Output : 20 14 8 2 -4 2 8 14 20"""
def tru_cong(N, K):
    if N <= 0:
        return [N]
    else:
        return [N] + tru_cong(N - K, K) + [N]

N = int(input("N = "))
K = int(input("K = "))

kq = tru_cong(N, K)
print("Output:", ' '.join(map(str, kq)))
