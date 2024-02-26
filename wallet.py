class Wallet:
    def __init__(self):
        self.balance = 0
        self.address = self.generate_address()

    def generate_address(self):
        # Implementasi pembuatan alamat kripto
        return "ABC123"  # Contoh alamat sederhana, seharusnya diganti dengan implementasi yang sesuai

    def get_balance(self):
        return self.balance

    def add_transaction(self, amount):
        self.balance += amount

    def spend(self, amount):
        if amount > self.balance:
            print("Saldo tidak mencukupi.")
        else:
            self.balance -= amount
            print(f"Transaksi sukses. Saldo saat ini: {self.balance}")

# Contoh penggunaan
if __name__ == "__main__":
    wallet = Wallet()
    print("Alamat dompet:", wallet.address)
    print("Saldo awal:", wallet.get_balance())
    
    wallet.add_transaction(50)
    print("Saldo setelah transaksi pertama:", wallet.get_balance())
    
    wallet.spend(20)
    print("Saldo setelah pengeluaran:", wallet.get_balance())
