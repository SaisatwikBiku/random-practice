#   Caesar Cipher Implementation: CSI 424/524 – Computer Security: Assignment-1
#  (c) Programming: Write a program to implement encoder and decoder of Caesar cipher using the following formulas. Provide your full name as input string and generate the encrypted text. Next, apply the decryption formula to decrypt the cipher text. Use the key table in problem 1(a) and key shift 7. Feel free to use C, java or python to write the program. 10 points


def encrypt(text, shift):
    out = []
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            out.append(chr((ord(ch) - base + shift) % 26 + base))
        else:
            out.append(ch)
    return ''.join(out)


def decrypt(text, shift):
    out = []
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            out.append(chr((ord(ch) - base - shift) % 26 + base))
        else:
            out.append(ch)
    return ''.join(out)


if __name__ == "__main__":
    name = "Sai Satwik Bikumandla"
    shift = 7
    cipher = encrypt(name, shift)
    plain = decrypt(cipher, shift)
    print("Original:", name)
    print("Encrypted:", cipher)
    print("Decrypted:", plain)