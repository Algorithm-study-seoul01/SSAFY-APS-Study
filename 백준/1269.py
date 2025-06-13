a_len, b_len = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))

a_diff = a - b
b_diff = b - a

print(len(a_diff) + len(b_diff))