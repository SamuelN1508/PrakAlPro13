def is_prima(n):
    # Membuat d untuk divider
    d = n-1
    # Fungsi rekursif
    def cek(n, d):
        # Fungsi cek akan membagi n dengan d, lalu rekursif fungsi lagi dengan d-1
        if d == 1:
            # Jika nilai d setelah dikurang 1 menjadi 1, maka n adalah prima
            return True
        if n % d == 0:
            # Jika n bisa dibagi d manapun maka n bukanlah prima
            return False
        else:
            # Rekursif
            return cek(n, d-1)
    return cek(n, d)
            
print(is_prima(17))
print(is_prima(16))
    