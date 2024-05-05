import model.calc as calculate

kalkulasi = calculate.calc()

def saldo_masuk(saldo):
    kalkulasi.setTrxMasuk(saldo)

def saldo_keluar(saldo):
    kalkulasi.setTrxKeluar(saldo)

def total_masuk():
    return kalkulasi.getTotalTrxMasuk()

def total_keluar():
    return kalkulasi.getTotalTrxKeluar()

def total_balance():
    return kalkulasi.getTotalBalance()

def list_trx_masuk():
    return kalkulasi.getListTrxMasuk()

def list_trx_keluar():
    return kalkulasi.getListTrxKeluar()

