#Viết chương trình cho bài toán tháp Hà nội
def thap_hanoi(n, nguon, dich, trung_gian):
    if n == 1:
        print("Di chuyển đĩa 1 từ", nguon, "->", dich)
    else:
        thap_hanoi(n-1, nguon, trung_gian, dich)
        print("Di chuyển đĩa", n, "từ", nguon, "->", dich)
        thap_hanoi(n-1, trung_gian, dich, nguon)

so_dia = int(input())
thap_hanoi(so_dia, 'A', 'C', 'B')

