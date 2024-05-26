def ganjil(n, awal = None):
    # Awal bilangan ganjil = 1
    awal = 1
    
    # Fungsi rekursif untuk menambah ganjil
    def hitung(n, awal):
        # Jika bilangan awal setelah ditambah melebihi batas n, return 0
        if awal > n:
            return 0
        # Jika belom melebihkan batas, awal akan ditambah dengan fungsi rekursif hitung awal ditambah 2
        if n >= awal:
            return awal + hitung(n, awal+2)
    return hitung(n, awal)
    
print(ganjil(10))
        