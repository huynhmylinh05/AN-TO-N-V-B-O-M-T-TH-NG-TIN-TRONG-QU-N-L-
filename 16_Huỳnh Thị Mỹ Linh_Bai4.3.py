import math
# 1. Tham số RSA
p = 17
q = 23
e = 5
# 2. Tính toán Modulus (n)
n = p * q
# Khóa công khai: (e, n) = (5, 391)
P_text = "HuynhThiMyLinh"

print(f"Tham số RSA: p={p}, q={q}, e={e}")
print(f"Modulus n: {n}")
print(f"Khóa công khai (e, n): ({e}, {n})")
print(f"Thông điệp gốc P: {P_text}")

# 4. Chuyển đổi thông điệp thành số (ASCII)
P_nums = [ord(char) for char in P_text]
print(f"Thông điệp số hóa (P): {P_nums}")

# 5. Thực hiện Mã hóa (Encryption)
# Công thức: C = P^e mod n
C_cipher = [pow(num, e, n) for num in P_nums]

print("\n--- KẾT QUẢ MÃ HÓA ---")
print(f"Bản mã C: {C_cipher}")

