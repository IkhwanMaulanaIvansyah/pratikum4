import os

class Queue:
    def __init__(self):
        self.items = []

    def add_user(self, item):
        self.items.append(item)

    def next_user(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

class ATM:
    def __init__(self, jum_uang=0):
        self.uang = jum_uang

    def check_uang(self):
        return self.uang

    def depo(self, bnyk_uang):
        if bnyk_uang > 0:
            self.uang += bnyk_uang
            return True
        return False

    def penarikan(self, bnyk_uang):
        if 0 < bnyk_uang <= self.uang:
            self.uang -= bnyk_uang
            return True
        return False

def main():
    atm = ATM(jum_uang=1000)
    queue = Queue()

    try:
        jumlah_pengguna = int(input("Masukkan jumlah pengguna yang ingin menggunakan ATM: "))
        os.system('cls' if os.name == 'nt' else 'clear')
        if jumlah_pengguna <= 0:
            raise ValueError("Jumlah pengguna harus lebih dari 0")
    except ValueError as e:
        print(f"Input tidak valid: {e}")
        return

    for i in range(1, jumlah_pengguna + 1):
        pengguna_nama = f"Antrian ke-{i}"
        queue.add_user(pengguna_nama)
    
    while not queue.is_empty():
        pengguna = queue.next_user()
        print(f"\n{pengguna}. Silakan lakukan transaksi Anda.")
        
        while True:
            print("\n-Masukan Menu-")
            print("1. Cek Saldo")
            print("2. Setor Tunai")
            print("3. Tarik Tunai")
            print("4. Selesai (=>)")

            pilihan = input("Masukkan pilihan (1/2/3/4): ")
            print("")

            if pilihan == '1':
                
                print(f"Saldo Anda saat ini adalah: Rp {atm.check_uang()}")
            
            elif pilihan == '2':
                try:
                    bnyk_uang = float(input("Masukkan jumlah uang yang akan disetor: "))
                    if atm.depo(bnyk_uang):
                        
                        print(f"Rp {bnyk_uang} telah disetor ke rekening Anda.")
                    else:
                        print("Jumlah yang dimasukkan tidak valid.")
                except ValueError:
                    print("Masukkan jumlah yang valid.")
            
            elif pilihan == '3':
                try:
                    bnyk_uang = float(input("Masukkan jumlah uang yang akan ditarik: "))
                    if atm.penarikan(bnyk_uang):
                      
                        print(f"Rp {bnyk_uang} telah ditarik dari rekening Anda.")
                    else:
                        print("Saldo tidak mencukupi atau jumlah tidak valid.")
                except ValueError:
                    print("Masukkan jumlah yang valid.")
            
            elif pilihan == '4':
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"\n{pengguna} telah Log-out")
                print("------------------------------------------")
                print("")               
                break
            
            else:
                
                print("Pilihan tidak valid, silakan coba lagi.")
                
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=================================================================")                
    print("|| Semua pengguna telah selesai melakukan transaksi. ATM tutup ||")
    print("=================================================================")  
    print("")
    print("---------------------------------------")
    print("BY : Name : Ikhwan Maulana Ivansyah")
    print("     NIM  : SI20230016")
    print("     KLPK : II (DUA)")
    print("     TUGAS: QUEUE")
    print("---------------------------------------")
if __name__ == "__main__":
    main()
