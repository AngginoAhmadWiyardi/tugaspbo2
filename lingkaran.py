class Lingkaran:
    def __init__(self, jari_jari):
        self.jari_jari = jari_jari
    
    def buatlingkaran(self):
        luas = 3.14 * (self.jari_jari ** 2)
        print(f"Luas lingkaran dengan jari-jari {self.jari_jari}: {luas}")

# Membuat objek
blt = Lingkaran(7)
blt.buatlingkaran()