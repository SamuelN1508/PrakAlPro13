def palindrome(k):
    # Jika hanya memiliki 1 huruf maka otomatis palindrome
    if len(k) <= 1:
        return True
    # Mengecek huruf pertama dan terakhir
    elif k[0] == k[-1]:
        # Melakukan rekursif tetapi huruf pertama dan terakhir dihilangkan
        return palindrome(k[1:-1])
    else:
        # Jika tidak sama, maka bukan palindrome
        return False
print(palindrome("kasurrusak"))
print(palindrome("kasurrsak"))