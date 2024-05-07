import tabulate as tb

class calc:
    def __init__(self):
        self.dataTrxMasuk = []
        self.dataTrxKeluar = []

    def setTrxMasuk(self, saldo):
        if not saldo.isdigit():
            raise ValueError("Saldo harus angka")
        self.dataTrxMasuk.append([int(saldo)]) 

    def setTrxKeluar(self, saldo):
        if not saldo.isdigit():
            raise ValueError("Saldo harus angka")
        self.dataTrxKeluar.append([int(saldo)])

    def getTotalTrxMasuk(self):
        return sum(data[0] for data in self.dataTrxMasuk) if self.dataTrxMasuk else 0

    def getTotalTrxKeluar(self):
        return sum(data[0] for data in self.dataTrxKeluar) if self.dataTrxKeluar else 0
    
    def getTotalBalance(self):
        return self.getTotalTrxMasuk() - self.getTotalTrxKeluar()
    
    def getListTrxMasuk(self):
        if not self.dataTrxMasuk:
            return "Data masih kosong"
        return tb.tabulate(self.dataTrxMasuk, headers=["Transaksi Masuk"], tablefmt="pretty")
    
    def getListTrxKeluar(self):
        if not self.dataTrxKeluar:
            return "Data masih kosong"
        return tb.tabulate(self.dataTrxKeluar, headers=["Transaksi Keluar"], tablefmt="pretty")
