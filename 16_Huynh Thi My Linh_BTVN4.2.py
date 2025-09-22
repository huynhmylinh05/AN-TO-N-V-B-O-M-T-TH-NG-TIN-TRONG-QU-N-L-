def shift_cipher_encrypt(plaintext, k=16):
    ciphertext = ""
    for ch in plaintext:
        if ch.isalpha(): 
            base = ord('A') if ch.isupper() else ord('a')
            # A=0...Z=25, a=0...z=25
            m = ord(ch) - base
            c = (m + k) % 26
            ciphertext += chr(base + c)
        else:
            ciphertext += ch  
    return ciphertext
# Thử
P = "HuynhThiMyLinh"
C = shift_cipher_encrypt(P, 16)
print("Plaintext :", P)
print("Ciphertext:", C)
