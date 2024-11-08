import json
import pwinput
import os
from prettytable import PrettyTable

# Path to JSON files
json_pengguna = r"C:\Users\User\Documents\PA DASPRO\pengguna.json"
json_renovasi = r"C:\Users\User\Documents\PA DASPRO\datarenov.json"

# Load data pengguna
with open(json_pengguna, "r") as jsonpengguna:
    data = json.load(jsonpengguna)
# Load data reservasi
with open(json_renovasi, "r") as jsonrenovasi:
    data_renovasi = json.load(jsonrenovasi)
# Fungsi clear
def clear():
    os.system("cls")

# Fungsi error
def error(a=""):
    print("=================================================")
    print(f"|Input {(a)} yang Anda masukkan salah. Silakan ulangi|")
    print("=================================================")

# Menu utama
def menu_utama():
    try:
        while True:
            clear()
            print("")
            print("===================================")
            print("|            Menu Utama           |")
            print("===================================")
            print("1. Admin")
            print("2. Registrasi Akun")
            print("3. Login")
            print("4. Keluar")
            input_menu = input("Pilih menu : ")
            if input_menu == "1": 
                login_admin()
            elif input_menu == "2":
                registrasi_akun()
            elif input_menu == "3":
                login_user()
            elif input_menu == "4":
                print("===================================")
                print("|    Anda keluar dari program     |")
                print("===================================")
                quit()
            else:
                error()
                input("Tekan enter untuk melanjutkan.....")
    except ValueError:
        clear()
        error()
    except Exception as a:
        print("===================")
        print(f"|Terjadi Kesalahan{a}|")
        print("===================")
        input("Tekan enter untuk melanjutkan.....")
    except KeyboardInterrupt:
        try:
            print("")
            print("====================================================")
            print("|  Tolong jangan tekan ctrl + c secara bersamaan!  |")
            print("====================================================")
            input("Tekan enter untuk melanjutkan.....")
        except Exception as a:
            print("===================")
            print(f"|Terjadi Kesalahan{a}|")
            print("===================")
        except KeyboardInterrupt:
            pass
    menu_utama()

# Fungsi login admin
def login_admin():
    admins = {"yuda": "000", "arifin": "111", "nova": "222"}
    try:
        for i in range(3):
            clear()
            print("===================================")
            print("|           Login Admin           |")
            print("===================================")
            username = input("Masukkan username admin: ").lower()
            password = pwinput.pwinput("Masukkan password admin: ", mask="*")
            if username in admins and admins[username] == password:
                print(f"Selamat datang, Admin {username}.")
                menu_admin()
                return
            else:
                print("===========================================")
                print("| Username atau password salah. Coba lagi |")
                print("===========================================")
                input("Tekan enter untuk melanjutkan.....")

        clear()
        print("=====================================")
        print("| Kesempatan login anda telah habis |")
        print("=====================================")
        quit()

    except ValueError:
        clear()
        error()
    except Exception as a:
        print("===================")
        print(f"|Terjadi Kesalahan{a}|")
        print("===================")
        input("Tekan enter untuk melanjutkan.....")
    except KeyboardInterrupt:
        try:
            print("")
            print("====================================================")
            print("|  Tolong jangan tekan ctrl + c secara bersamaan!  |")
            print("====================================================")
            input("Tekan enter untuk melanjutkan.....")
        except Exception as a:
            print("===================")
            print(f"|Terjadi Kesalahan{a}|")
            print("===================")
        except KeyboardInterrupt:
            pass

# Fungsi registrasi akun
def registrasi_akun():
    try:
        clear()
        print("===================================")
        print("|         Registrasi User         |")
        print("===================================")
        input_username = input("Masukan Username : ").lower()
        if input_username in data["Username"]:
            print("Username sudah digunakan. Silakan gunakan username yang lain.")
            input("Tekan enter untuk melanjutkan.....")
            return
        input_password = pwinput.pwinput("Masukan password : ")
        
        # Tetapkan saldo awal secara otomatis
        saldo_awal = 0

        data["Username"].append(input_username)
        data["Password"].append(input_password)
        data["Saldo"].append(saldo_awal)

        with open(json_pengguna, "w") as jsonpengguna:
            json.dump(data, jsonpengguna, indent=4)

        print("+---------------------------+")
        print("| Akun berhasil ditambahkan |")
        print("+---------------------------+")
        input("Tekan enter untuk melanjutkan.....")
    
    except ValueError:
        clear()
        error()
    except Exception as a:
        print("===================")
        print(f"|Terjadi Kesalahan{a}|")
        print("===================")
        input("Tekan enter untuk melanjutkan.....")
    except KeyboardInterrupt:
        try:
            print("")
            print("====================================================")
            print("|  Tolong jangan tekan ctrl + c secara bersamaan!  |")
            print("====================================================")
            input("Tekan enter untuk melanjutkan.....")
        except Exception as a:
            print("===================")
            print(f"|Terjadi Kesalahan{a}|")
            print("===================")
        except KeyboardInterrupt:
            pass

# Fungsi login user
def login_user():
    try:
        clear()
        print("===================================")
        print("|           Login User            |")
        print("===================================")
        for _ in range(3):
            input_username = input("Masukan Username : ").lower()
            input_password = pwinput.pwinput("Masukkan password : ", mask="*")
            if input_username in data["Username"]:
                index = data["Username"].index(input_username)
                if data["Password"][index] == input_password:
                    print(f"Login berhasil! Selamat datang, {input_username}.")
                    menu_user(index)
                    return
            print("===========================================")
            print("| Username atau password salah. Coba lagi |")
            print("===========================================")
            input("Tekan enter untuk melanjutkan.....")

        clear()
        print("=====================================")
        print("| Kesempatan login anda telah habis |")
        print("=====================================")
        quit()


    except ValueError:
        clear()
        error()
    except Exception as a:
        print("===================")
        print(f"|Terjadi Kesalahan{a}|")
        print("===================")
    except KeyboardInterrupt:
        try:
            print("")
            print("====================================================")
            print("|  Tolong jangan tekan ctrl + c secara bersamaan!  |")
            print("====================================================")
            input("Tekan enter untuk melanjutkan.....")
        except Exception as a:
            print("===================")
            print(f"|Terjadi Kesalahan{a}|")
            print("===================")
        except KeyboardInterrupt:
            pass

# Menu admin
def menu_admin():
    while True:
        clear()
        print("===================================")
        print("|            Menu Admin           |")
        print("===================================")
        print("1. Buat Reservasi")
        print("2. Lihat Data Reservasi")
        print("3. Ubah Data Reservasi")
        print("4. Hapus Data Reservasi")
        print("5. Kembali ke Menu Utama")
        try:
            pilihan = input("Masukkan Pilihan: ")
            if pilihan == '1':
                buat_reservasi_admin()
            elif pilihan == '2':
                lihat_renovasi()
                input("Tekan enter untuk melanjutkan.....")
            elif pilihan == '3':
                ubah_reservasi_admin()
            elif pilihan == '4':
                hapus_reservasi_admin()
            elif pilihan == '5':
                break
            else:
                error("Pilihan")
                input("Tekan enter untuk melanjutkan.....")

        except ValueError:
            clear()
            error()
        except Exception as a:
            print("===================")
            print(f"|Terjadi Kesalahan{a}|")
            print("===================")
            input("Tekan enter untuk melanjutkan.....")
        except KeyboardInterrupt:
            try:
                print("")
                print("====================================================")
                print("|  Tolong jangan tekan ctrl + c secara bersamaan!  |")
                print("====================================================")
                input("Tekan enter untuk melanjutkan.....")
            except Exception as a:
                print("===================")
                print(f"|Terjadi Kesalahan{a}|")
                print("===================")
            except KeyboardInterrupt:
                pass

# Fungsi buat reservasi admin
def buat_reservasi_admin():
    try:
        clear()
        print("===========================")
        print("|      Buat Reservasi     |")
        print("===========================")
        input_no = len(data_renovasi["no"]) + 1
        input_user = input("Masukan User : ")
        input_reservasi = input("Masukan Reservasi : ")
        input_harga = int(input("Masukan Harga : "))
        input_status = input("Masukan Status Pembayaran : ")

        data_renovasi["no"].append(input_no)
        data_renovasi["user"].append(input_user)
        data_renovasi["reservasi_user"].append(input_reservasi)
        data_renovasi["harga_reservasi"].append(input_harga)
        data_renovasi["status pembayaran"].append(input_status)
        
        print("+--------------------------------+")
        print("| Reservasi berhasil ditambahkan |")
        print("+--------------------------------+")
        input("Tekan enter untuk melanjutkan.....")
        with open(json_renovasi, "w") as jsonrenovasi:
            json.dump(data_renovasi, jsonrenovasi, indent=4)

    except ValueError:
        clear()
        error()
    except Exception as a:
        print("===================")
        print(f"|Terjadi Kesalahan{a}|")
        print("===================")
        input("Tekan enter untuk melanjutkan.....")
    except KeyboardInterrupt:
        try:
            print("")
            print("====================================================")
            print("|  Tolong jangan tekan ctrl + c secara bersamaan!  |")
            print("====================================================")
            input("Tekan enter untuk melanjutkan.....")
        except Exception as a:
            print("===================")
            print(f"|Terjadi Kesalahan{a}|")
            print("===================")
            input("Tekan enter untuk melanjutkan.....")
        except KeyboardInterrupt:
            pass

def lihat_renovasi():
    clear()
    table = PrettyTable()
    table.field_names = ["No", "User", "Reservasi", "Harga", "Status Pembayaran"]

    with open(json_renovasi, "r") as jsonrenovasi:
        data_renovasi = json.load(jsonrenovasi)

    for i in range(len(data_renovasi["no"])):
        table.add_row([
            data_renovasi["no"][i],
            data_renovasi["user"][i],
            data_renovasi["reservasi_user"][i],
            data_renovasi["harga_reservasi"][i],
            data_renovasi["status pembayaran"][i]])
    print(table)

# Fungsi ubah reservasi admin
def ubah_reservasi_admin():
    try:
        clear()
        lihat_renovasi()
        nomor = int(input("Masukkan nomor reservasi yang ingin diubah: "))
        if nomor in data_renovasi["no"]:
            index = data_renovasi["no"].index(nomor)

            print("Data lama: ")
            print(f"User: {data_renovasi['user'][index]}")
            print(f"Reservasi: {data_renovasi['reservasi_user'][index]}")
            print(f"Harga: {data_renovasi['harga_reservasi'][index]}")
            print(f"Status Pembayaran: {data_renovasi['status pembayaran'][index]}")
            
            new_user = input("Masukkan user baru (kosongkan jika tidak ada perubahan): ")
            new_reservasi = input("Masukkan reservasi baru (kosongkan jika tidak ada perubahan): ")
            new_harga = int(input("Masukkan harga baru (kosongkan jika tidak ada perubahan): "))
            new_status = input("Masukkan status pembayaran baru (kosongkan jika tidak ada perubahan): ")
            
            if new_user:
                data_renovasi["user"][index] = new_user
            if new_reservasi:
                data_renovasi["reservasi_user"][index] = new_reservasi
            if new_harga:
                data_renovasi["harga_reservasi"][index] = new_harga
            if new_status:
                data_renovasi["status pembayaran"][index] = new_status
            
            with open(json_renovasi, "w") as jsonrenovasi:
                json.dump(data_renovasi, jsonrenovasi, indent=4)
            
            print("+------------------------------+")
            print("|  Reservasi berhasil diubah   |")
            print("+------------------------------+")
        else:
            print("Nomor reservasi tidak ditemukan.")
            input("Tekan enter untuk melanjutkan.....")

    except ValueError:
        error()
        clear()
    except Exception as a:
        print("===================")
        print(f"|Terjadi Kesalahan{a}|")
        print("===================")
        input("Tekan enter untuk melanjutkan.....")
    except KeyboardInterrupt:
        print("")
        print("====================================================")
        print("|  Tolong jangan tekan ctrl + c secara bersamaan!  |")
        print("====================================================")
        input("Tekan enter untuk melanjutkan.....")
    except Exception as a:
        print("===================")
        print(f"|Terjadi Kesalahan{a}|")
        print("===================")
    except KeyboardInterrupt:
        pass

def hapus_reservasi_admin():
    try:
        lihat_renovasi()
        nomor = int(input("Masukan nomor reservasi yang ingin dihapus: "))
        if nomor in data_renovasi["no"]:
            index = data_renovasi["no"].index(nomor)
            print("Data lama: ")
            print(f"User: {data_renovasi['user'][index]}")
            print(f"Reservasi: {data_renovasi['reservasi_user'][index]}")
            print(f"Harga: {data_renovasi['harga_reservasi'][index]}")
            print(f"Status Pembayaran: {data_renovasi['status pembayaran'][index]}")

            data_renovasi["no"].pop(index)
            data_renovasi["user"].pop(index)
            data_renovasi["reservasi_user"].pop(index)
            data_renovasi["harga_reservasi"].pop(index)
            data_renovasi["status pembayaran"].pop(index)

            with open(json_renovasi, "w") as jsonrenovasi:
                json.dump(data_renovasi, jsonrenovasi, indent=4)
            
            print("+------------------------------+")
            print("|  Reservasi berhasil dihapus  |")
            print("+------------------------------+")
            input("Tekan enter untuk melanjutkan.....")
        else:
            print("Nomor reservasi tidak ditemukan.")
            input("Tekan enter untuk melanjutkan.....")

    except ValueError:
        clear()
        error()
    except Exception as a:
        print("===================")
        print(f"|Terjadi Kesalahan{a}|")
        print("===================")
        input("Tekan enter untuk melanjutkan.....")
    except KeyboardInterrupt:
        try:
            print("")
            print("====================================================")
            print("|  Tolong jangan tekan ctrl + c secara bersamaan!  |")
            print("====================================================")
            input("Tekan enter untuk melanjutkan.....")
        except Exception as a:
            print("===================")
            print(f"|Terjadi Kesalahan{a}|")
            print("===================")
            input("Tekan enter untuk melanjutkan.....")
        except KeyboardInterrupt:
            pass

def menu_user(index):
    try:
        while True:
            clear()
            print("===================================")
            print("|            Menu User            |")
            print("===================================")
            print("1. Saldo")
            print("2. Lihat Jasa Renovasi")
            print("3. Buat Reservasi Renovasi")
            print("4. Lihat Bukti Reservasi")
            print("5. Cari Jasa Renovasi")
            print("6. Kembali")
            input_menu = input("Pilih menu : ")
            if input_menu == "1":
                menu_saldo_user(index)
            elif input_menu == "2":
                lihat_jasa_renovasi()
                input("Tekan enter untuk melanjutkan.....")
            elif input_menu == "3":
                buat_reservasi_user(index)
            elif input_menu == "4":
                lihat_bukti_reservasi()
            elif input_menu == "5":
                searching_jasa_renovasi()
            elif input_menu == "6":
                menu_utama()
            else:
                print("Menu tidak tersedia. Silakan coba lagi")
                input("Tekan enter untuk melanjutkan.....")

    except ValueError:
        clear()
        error()
    except Exception as a:
        print("===================")
        print(f"|Terjadi Kesalahan{a}|")
        print("===================")
        input("Tekan enter untuk melanjutkan.....")
    except KeyboardInterrupt:
        print("")
        print("====================================================")
        print("|  Tolong jangan tekan ctrl + c secara bersamaan!  |")
        print("====================================================")
        input("Tekan enter untuk melanjutkan.....")
    except Exception as a:
        print("===================")
        print(f"|Terjadi Kesalahan{a}|")
        print("===================")
        input("Tekan enter untuk melanjutkan.....")
    except KeyboardInterrupt:
        pass
# Menu saldo user
def menu_saldo_user(index):
    try:
        while True:
            clear()
            print("===================================")
            print("|            Menu Saldo           |")
            print("===================================")
            print("1. Tampilkan Saldo")
            print("2. Tambah Saldo")
            print("3. Kembali")
            input_menu = input("Pilih menu : ")
            if input_menu == "1":
                lihat_saldo(index)
            elif input_menu == "2":
                tambah_saldo(index)
            elif input_menu == "3":
                menu_user(index)
            else:
                error("Menu")
                input("Tekan enter untuk melanjutkan.....")

    except ValueError:
        clear()
        error()
    except Exception as a:
        print("===================")
        print(f"|Terjadi Kesalahan{a}|")
        print("===================")
        input("Tekan enter untuk melanjutkan.....")
    except KeyboardInterrupt:
        try:
            print("")
            print("====================================================")
            print("|  Tolong jangan tekan ctrl + c secara bersamaan!  |")
            print("====================================================")
            input("Tekan enter untuk melanjutkan.....")
        except Exception as a:
            print("===================")
            print(f"|Terjadi Kesalahan{a}|")
            print("===================")
        except KeyboardInterrupt:
            pass

# Fungsi tampilkan saldo
def lihat_saldo(index):
    clear()
    with open(json_pengguna, "r") as jsonpengguna:
        data = json.load(jsonpengguna)

    saldo = data["Saldo"][index]
    username = data["Username"][index]
    
    table = PrettyTable()
    table.field_names = ["Username", "Saldo E-Money"]
    table.add_row([username, f"Rp {saldo:.2f}"])
    print(table)
    input("Tekan enter untuk melanjutkan.....")

# Fungsi tambah saldo
def tambah_saldo(index):
    try:
        clear()
        print("===================================")
        print("|            Isi Saldo            |")
        print("===================================")
        jumlah = int(input("Masukkan jumlah saldo yang ingin ditambahkan: Rp "))
        if 1 <= jumlah <= 10000000:
            data["Saldo"][index] += jumlah
            with open(json_pengguna, "w") as jsonpengguna:
                json.dump(data, jsonpengguna, indent=4)
            print(f"Saldo berhasil ditambahkan: Rp {jumlah:.2f}")
            input("Tekan enter untuk melanjutkan.....")
        else:
            print("Jumlah yang ditambahkan harus lebih besar dari 0 dan tidak lebih dari 10 juta.")
            input("Tekan enter untuk melanjutkan.....")

    except ValueError:
        clear()
        error()
    except Exception as a:
        print("===================")
        print(f"|Terjadi Kesalahan{a}|")
        print("===================")
        input("Tekan enter untuk melanjutkan.....")
    except KeyboardInterrupt:
        try:
            print("")
            print("====================================================")
            print("|  Tolong jangan tekan ctrl + c secara bersamaan!  |")
            print("====================================================")
            input("Tekan enter untuk melanjutkan.....")
        except Exception as a:
            print("===================")
            print(f"|Terjadi Kesalahan{a}|")
            print("===================")
        except KeyboardInterrupt:
            pass

def lihat_jasa_renovasi():
    clear()
    with open(json_pengguna, "r") as jsonpengguna:
        pengguna_data = json.load(jsonpengguna)
    table = PrettyTable()
    table.title = "Daftar Jasa Renovasi dan Harga"
    table.field_names = ["No", "Jasa Renovasi", "Harga"]
    for i, (jasa, harga) in enumerate(zip(data_renovasi["reservasi"], data_renovasi["harga"]), start=1):
        table.add_row([i, jasa, f"Rp{harga:,}"])
    print(table)

def buat_reservasi_user(index):
    try:
        clear()
        print("===================================")
        print("|           Buat Reservasi        |")
        print("===================================")
        lihat_jasa_renovasi() 
        nomor = int(input("Masukkan nomor jasa yang ingin direservasi: "))

        with open(json_renovasi, "r") as jsonrenovasi:
            data_renovasi = json.load(jsonrenovasi)
        
        if 1 <= nomor <= len(data_renovasi["reservasi"]):
            jasa = data_renovasi["reservasi"][nomor - 1]
            harga = data_renovasi["harga"][nomor - 1]
            
            with open(json_pengguna, "r") as jsonpengguna:
                pengguna_data = json.load(jsonpengguna)
            
            saldo_user = pengguna_data["Saldo"][index]
            print("====================jasa yang dipilih dengan harga=====================")
            print(f"Anda memilih {jasa} dengan harga Rp{harga}. Saldo Anda saat ini: Rp{saldo_user:.2f}")
            if saldo_user >= harga:
                konfirmasi = input("Apakah Anda ingin membayar menggunakan saldo Anda? (y/n)                     : ")
                if konfirmasi.lower() == 'y':
                    saldo_user -= harga
                    pengguna_data["Saldo"][index] = saldo_user 
                    
                    data_renovasi["no"].append(len(data_renovasi["no"]) + 1)
                    data_renovasi["user"].append(pengguna_data["Username"][index])
                    data_renovasi["reservasi_user"].append(jasa)
                    data_renovasi["harga_reservasi"].append(harga)
                    data_renovasi["status pembayaran"].append("lunas")
                    
                    with open(json_pengguna, "w") as jsonpengguna:
                        json.dump(pengguna_data, jsonpengguna, indent=4)
                    
                    with open(json_renovasi, "w") as jsonrenovasi:
                        json.dump(data_renovasi, jsonrenovasi, indent=4)
                    
                    print(f"Reservasi untuk {jasa} berhasil dibuat dengan harga Rp{harga}. Saldo Anda sekarang: Rp{saldo_user:.2f}")
                    print("=======================================================================")
                    input("Tekan enter untuk melanjutkan.....")
                else:
                    print("Pembayaran dibatalkan.")
                    input("Tekan enter untuk melanjutkan.....")
            else:
                print("Saldo Anda tidak mencukupi. Silakan tambahkan saldo terlebih dahulu.")
                input("Tekan enter untuk melanjutkan.....")
        else:
            print("Nomor yang Anda masukkan tidak valid.")
            input("Tekan enter untuk melanjutkan.....")
    except ValueError:
        clear()
        error()
    except Exception as a:
        print("===================")
        print(f"|Terjadi Kesalahan{a}|")
        print("===================")
    except KeyboardInterrupt:
        try:
            print("")
            print("====================================================")
            print("|  Tolong jangan tekan ctrl + c secara bersamaan!  |")
            print("====================================================")
            input("Tekan enter untuk melanjutkan.....")
        except Exception as a:
            print("===================")
            print(f"|Terjadi Kesalahan{a}|")
            print("===================")
        except KeyboardInterrupt:
            pass

def lihat_bukti_reservasi():
    clear()
    with open(json_renovasi, "r") as jsonrenovasi:
        data_renovasi = json.load(jsonrenovasi)

    if len(data_renovasi["no"]) == 0:
        print("Tidak ada bukti reservasi yang tersedia.")
        return

    last_index = len(data_renovasi["no"]) - 1
    print("========== BUKTI RESERVASI ==========")
    print(f"Nomor Reservasi    : {data_renovasi['no'][last_index]}")
    print(f"User               : {data_renovasi['user'][last_index]}")
    print(f"Reservasi          : {data_renovasi['reservasi_user'][last_index]}")
    print(f"Harga              : Rp {data_renovasi['harga_reservasi'][last_index]}")
    print(f"Status Pembayaran  : {data_renovasi['status pembayaran'][last_index]}")
    print("=====================================")
    input("Tekan enter untuk melanjutkan.....")

def searching_jasa_renovasi():
    clear()
    print("===================================")
    print("|           Cari Jasa             |")
    print("===================================")
    with open(json_renovasi, "r") as jsonrenovasi:
        data_renovasi = json.load(jsonrenovasi)
    print("")
    cari = input("Masukkan jasa yang ingin dicari: ")
    found = False
    print("===========Jasa yang dicari===========")
    for i in range(len(data_renovasi["reservasi"])):
        if cari.lower() in data_renovasi["reservasi"][i].lower():
            print(f"Jasa: {data_renovasi['reservasi'][i]}")
            print(f"Harga: {data_renovasi['harga'][i]}")
            found = True
            input("Tekan enter untuk melanjutkan.....")
    if not found:
        print("======================================")
        print("|        Jasa tidak ditemukan        |")
        print("======================================")
        input("Tekan enter untuk melanjutkan.....")

menu_utama()
