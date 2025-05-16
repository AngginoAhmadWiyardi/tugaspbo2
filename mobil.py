class Mobil:
    def __init__(self, merek, tahun):
        self.merek = merek
        self.tahun = tahun
    
    def jalankan(self):
        print(f"Mobil {self.merek} tahun {self.tahun} sedang melaju!")

# Membuat objek
mobil1 = Mobil("Toyota", 2020)
mobil1.jalankan()