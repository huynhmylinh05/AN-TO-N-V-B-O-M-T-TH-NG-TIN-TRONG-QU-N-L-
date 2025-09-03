
def caesar_encrypt(text, k):
    result = ""
    for char in text:
        if char.isalpha(): 
            shift = 65 if char.isupper() else 97
            result += chr((ord(char) - shift + k) % 26 + shift)
        else:
            result += char  
    return result

k = 16
plaintext = "Huynh Thi My Linh"

# Mã hóa
ciphertext = caesar_encrypt(plaintext, k)

# Kết quả
print("Plaintext :",plaintext)
print("Ciphertext:",ciphertext)
