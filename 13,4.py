def hitung(b):
    # Jika tidak ada b maka return 0
    if not b:
        return 0
    # Jika masih ada maka b akan dibagi 10 untuk mencari satuan ditambah hasil fungsi rekursif(b//10) untuk mencari puluhan/ratusan
    else:
        return b % 10 + hitung(b//10)
    
print(hitung(234))
    