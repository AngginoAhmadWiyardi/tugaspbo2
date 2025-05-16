class Buku:
    def __init__(self, judul, pengarang):
        self.judul = judul
        self.pengarang = pengarang
    
    def tampilkan_info(self):
        print(f"Judul: {self.judul}\nPengarang: {self.pengarang}")

# Membuat objek
buku1 = Buku("Laskar Pelangi", "Andrea Hirata")
buku1.tampilkan_info()