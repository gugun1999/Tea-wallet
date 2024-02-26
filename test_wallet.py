import unittest
from wallet import Wallet

class TestWallet(unittest.TestCase):
    def test_initial_balance(self):
        wallet = Wallet()
        self.assertEqual(wallet.get_balance(), 0)

    def test_add_transaction(self):
        wallet = Wallet()
        wallet.add_transaction(50)
        self.assertEqual(wallet.get_balance(), 50)

    def test_spend(self):
        wallet = Wallet()
        wallet.add_transaction(50)
        wallet.spend(20)
        self.assertEqual(wallet.get_balance(), 30)

    def test_insufficient_balance(self):
        wallet = Wallet()
        wallet.add_transaction(20)
        wallet.spend(30)
        self.assertEqual(wallet.get_balance(), 20)

if __name__ == "__main__":
    unittest.main()
