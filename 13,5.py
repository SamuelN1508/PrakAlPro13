def combination(n, k):
    # Base case, jika k == 0 atau k=n, maka return 1 karena ada satu cara untuk memilih 0 dari n, dan untuk memilih semua n dari n
    if k == 0 or k == n:
        return 1
    # Rekursif, Jika base case tidak terpenuhi, maka akan rekursif dua kali mengikuti rumus kombinasi
    else:
        return combination(n-1, k-1) + combination(n-1, k)
    
print(combination(8, 2))