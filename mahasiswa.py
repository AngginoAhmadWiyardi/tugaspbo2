class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim
        self.krs = []
    
    def cetakkrs(self):
        print(f"KRS {self.nama} (NIM: {self.nim}):")
        for matkul in self.krs:
            print(f"- {matkul}")

# Membuat objek
mhs = Mahasiswa("Anggino Ahmad Wiiyardi", "230705166")
mhs.krs.extend(["Pemrograman Berorientasi Objek"])
mhs.cetakkrs()