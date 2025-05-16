class AkunBank:
    def __init__(self, pemilik, saldo):
        self.pemilik = pemilik
        self.saldo = saldo
    
    def cek_saldo(self):
        print(f"Saldo {self.pemilik}: Rp{self.saldo:,}")

# Membuat objek
akun = AkunBank("Budi", 5_000_000)
akun.cek_saldo()