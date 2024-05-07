import service.calcServ as app

def main():
    while True:
        print("\nMenu:")
        print("1. Tambah Uang Masuk")
        print("2. Tambah Uang Keluar")
        print("3. Tampilkan Uang Masuk")
        print("4. Tampilkan Uang Keluar")
        print("5. Tampilkan Total Uang Masuk")
        print("6. Tampilkan Total Uang Keluar")
        print("7. Tampilkan Saldo")
        print("8. Keluar")
        
        pilihan = input("Masukkan pilihan Anda: ")
        
        if pilihan == '1':
            jumlah = input("Masukkan jumlah uang masuk: ")
            app.saldo_masuk(jumlah)
        elif pilihan == '2':
            jumlah = input("Masukkan jumlah uang keluar: ")
            app.saldo_keluar(jumlah)
        elif pilihan == '3':
            print("Uang Masuk:", app.list_trx_masuk())
        elif pilihan == '4':
            print("Uang Keluar:", app.list_trx_keluar())
        elif pilihan == '5':
            print("Total Uang Masuk:", app.total_masuk())
        elif pilihan == '6':
            print("Total Uang Keluar:", app.total_keluar())
        elif pilihan == '7':
            print("Saldo:", app.total_balance())
        elif pilihan == '8':
            print("Terima kasih telah menggunakan aplikasi.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()