## SISTEM PEMESANAN JASA RENOVASI RUMAH
# Deskripsi Program
Program ini kami buat sebagai gambaran sistem jasa pemesanan renovasi dalam bentuk program python. Didalam program ini terdapat menu yang dapat diakses oleh admin dan juga pengguna. Menu yang dapat diakses oleh admin yaitu ada buat reservasi renovasi, lihat reservasi renovasi, ubah reservasi renovasi, menghapus reservasi renovasi, sementara menu yang dapat di akses pengguna yaitu ada tampilkan saldo, tambah saldo, lihat jasa renovasi, buat reservasi renovasi, lihat bukti reservasi. Sehingga program ini dibuat untuk mengetahui bagaimana cara pemesanan reservasi renovasi.

# Library
Terdapat 4 library yang kami pakai yaitu:
1. json untuk menyimpan dan memproses data secara dinamis.
2. pwinput untuk membuat password admin dan user sensor.
3. os 
4. Prettytable untuk membuat tabel secara otomatis dan enak untuk dilihat.
   
# Fitur
### User
1. Lihat Saldo
2. Top Up Saldo
3. Lihat Jasa Renovasi
4. Buat Reservasi Renovasi
5. Lihat Bukti Reservasi
6. Cari Jasa Renovasi

### Admin
1. Buat Reservasi Renovasi
2. Lihat Data Reservasi
3. Ubah Data Reservasi
4. Hapus Data Reservasi

## Penggunaan Program
## Menu Utama
 ![Screenshot 2024-11-07 192613](https://github.com/user-attachments/assets/5f15e326-a1a8-48a5-8e42-7e198215188c)
#### Tampilan menu utama terdapat 4 pilihan yaitu Admin, Registrasi Akun, Login, dan Keluar.

# Menu Login
### Login Admin
![Screenshot 2024-11-07 192921](https://github.com/user-attachments/assets/ea57011d-a6c4-4b22-83a9-d9ac3bd5f402)
#### Jika anda memilih pilihan 1 maka masuk ke login admin dengan memasukkan username admin dan juga password admin, jika benar maka akan masuk ke menu admin.

### Registrasi Akun
![Screenshot 2024-11-07 193324](https://github.com/user-attachments/assets/a40f309d-36f7-460a-a45f-aaff79a301b6)
#### Jika anda memilih pilihan 2 maka masuk ke registrasi akun, mendaftarkan akun baru dengan nama dan password, jika nama sudah dipakai maka gunakan nama lain.

### Login Akun
![Screenshot 2024-11-07 193537](https://github.com/user-attachments/assets/b7ccd805-e5f1-4df2-a8a5-9a069a7cf0c2)
#### Jika anda memilih pilihan 3 maka anda akan login menggunakan akun yang sudah didaftarkan tadi. Jika berhasil login maka akan masuk ke menu user.

### Keluar 
![Screenshot 2024-11-07 214603](https://github.com/user-attachments/assets/3d930611-324f-4b49-af58-518b6cc760f7)
#### Jika anda memilih pilihan 4 maka anda akan keluar dari program kami.
## Menu Admin 
![Screenshot 2024-11-07 194556](https://github.com/user-attachments/assets/1f144405-08f1-4e59-a894-d9c80e0e44fa)
#### Berikut adalah menu admin jika di menu utama telah berhasil login sebagai admin.

### Buat Reservasi
![Screenshot 2024-11-07 195023](https://github.com/user-attachments/assets/98fe003e-ae4f-47ea-8a95-2047a7736717)
#### Jika memilih pilihan 1 maka membuat reservasi dan masukkan nama user.
![Screenshot 2024-11-07 195034](https://github.com/user-attachments/assets/25d47929-446c-42d4-b7b9-562ff43bf644)
#### Masukkan reservasi yang diinginkan contoh nya pengecatan dinding.
![Screenshot 2024-11-07 195045](https://github.com/user-attachments/assets/bd621ddf-16d7-4181-9d91-b2e91b48a603)
#### Masukkan harga dari reservasi tersebut conto nya 200000
![Screenshot 2024-11-07 195058](https://github.com/user-attachments/assets/b6b98da6-c330-4f4d-bf67-c454ee2d1fd8)
#### Masukkan status pembayaran yaitu lunas.
![Screenshot 2024-11-07 195110](https://github.com/user-attachments/assets/43f3884b-9a60-45fe-bdce-1dc4b177fb58)
#### Maka reservasi berhasil ditambahkan

### Lihat Data Reservasi
![Screenshot 2024-11-07 200848](https://github.com/user-attachments/assets/40f424f5-1c59-4650-a85e-893d6d4333d4)
#### Jika memilih pilihan 2 maka akan menampilkan tabel yang berisi data reservasi yang telah dipesan oleh user.

### Ubah Data Reservasi
![Screenshot 2024-11-07 201426](https://github.com/user-attachments/assets/03d30f88-97a2-4721-ba75-f4a6c4761b9d)
##### Jika memilih pilihan 3 maka akan menampilkan tabel.
![Screenshot 2024-11-07 201435](https://github.com/user-attachments/assets/edb2112b-5279-42eb-9a0c-c9d63bbcd152)
#### Lalu masukkan nomor reservasi yang ingin diubah pada tabel.
![Screenshot 2024-11-07 201541](https://github.com/user-attachments/assets/726d60dc-a835-4617-acad-ec78d1b69367)
#### Setelah memilih no reservasi mana yang ingin di ubah, ditampilkan data lama dan memasukkan nama user baru. Jika tidak ada kosongkan.
![Screenshot 2024-11-07 201553](https://github.com/user-attachments/assets/cf100ba5-dc01-4998-a877-e1d561157e8c)
#### Masukkan jasa reservasi yang baru, jika tidak ada kosongkan.
![Screenshot 2024-11-07 201606](https://github.com/user-attachments/assets/2d9f7abb-a5bd-4614-ad1b-d557da054e9e)
#### Masukkan harga renovasi yang baru.
![Screenshot 2024-11-07 201616](https://github.com/user-attachments/assets/00eed9cb-920d-42ce-b11c-fc9139f0657c)
#### Masukkan status pembayaran yang baru yaitu lunas.
![Screenshot 2024-11-07 214008](https://github.com/user-attachments/assets/d4bbc4a3-0c43-4630-8c0f-95a2016d8da7)
#### Menampilkan reservasi berhasil diubah.
### Hapus Data Reservasi
![Screenshot 2024-11-07 204138](https://github.com/user-attachments/assets/cf26240e-a48c-4547-b974-edcc35623cea)
#### Jika memilih pilihan 4 maka akan ditampilkan tabel data reservasi dan masukkan nomor reservasi yang ingin dihapus.
![Screenshot 2024-11-07 204157](https://github.com/user-attachments/assets/bd3ce205-d49e-4822-b6a9-896df52ea0fc)
#### Maka akan muncul data yang akan dipilih dan reservasi berhasil dihapus
### Keluar
![Screenshot 2024-11-07 214337](https://github.com/user-attachments/assets/995cd3ca-b29f-4379-8d4a-12aed05192f6)
#### Jika memilih pilihan 5 maka akan keluar dari menu admin dan kembali ke menu utama.

## Menu User
![Screenshot 2024-11-07 220331](https://github.com/user-attachments/assets/53459d2c-943f-43e0-ab24-871ec625d71e)
#### Setelah login user berhasil akan masuk ke menu user.
## Menu Saldo
![Screenshot 2024-11-07 220051](https://github.com/user-attachments/assets/204bea13-99cd-45eb-acf1-176f98e8651f)
#### Jika anda memilih pilihan 1 maka akan menuju ke menu saldo.
### Lihat Saldo
![Screenshot 2024-11-07 220100](https://github.com/user-attachments/assets/1b6498ec-5442-4d15-8fce-a4f846963f16)
#### Jika anda memilih pilihan 1 maka akan menampilkan tabel yanng berisikan informasi saldo anda.
### Tambah Saldo
![Screenshot 2024-11-07 220124](https://github.com/user-attachments/assets/7f5e61c9-23b1-4e22-bded-8d57234239ec)
#### Jika anda memilih pilihan 2 maka anda dapat menambahkan saldo maksimal 10 juta.
![Screenshot 2024-11-07 220137](https://github.com/user-attachments/assets/02b5e603-9a4a-4eb2-afdf-dbd7d76de1d8)
#### Saldo berhasil ditambahkan sesuai yang diinginkan user.
![Screenshot 2024-11-07 221035](https://github.com/user-attachments/assets/d6ee9a8f-8b58-460b-adb3-58b825308aa7)
#### Jika memilih pilihan 3 maka akan kembali ke menu user.

## Lihat Jasa Renovasi
![Screenshot 2024-11-07 221124](https://github.com/user-attachments/assets/22288acd-4b7b-44b9-b7c6-2eee5e135bc6)
#### Jika anda memilih pilihan 2 maka akan menampilkan tabel yang berisikan daftar jasa renovasi beserta harga.

## Buat Reservasi Renovasi
![Screenshot 2024-11-07 222053](https://github.com/user-attachments/assets/c1d120c5-7cf0-4378-a350-6e037193b8b9)
#### Jika anda memilih pilihan 3 maka akan masuk ke pemesanan reservasi renovasi rumah.
![Screenshot 2024-11-07 222305](https://github.com/user-attachments/assets/52adf7bd-bf79-43d2-ad1b-3310eac857c5)
#### Lalu masukkan nomor jasa yang ingin direservasi.
![Screenshot 2024-11-07 222115](https://github.com/user-attachments/assets/3005a21e-2c0b-4edf-83b7-3bfb5d4a49ac)
#### Setelah itu melakukan pembayaran pilihan y/n, jika memilih y maka pembayaran berhasil dan menampilkan sisa saldo. Apabila memilih n maka pembayaran dibatalkan.

## Lihat Bukti Reservasi
![Screenshot 2024-11-07 222530](https://github.com/user-attachments/assets/27ff3c21-cb11-460b-b2b8-e0a54d2383b1)
#### Jika memilih pilihan 4 maka akan menampilkan bukti reservasi yang berisikan nomor reservasi, user, reservasi, harga, status pembayaran.

## Cari Jasa Reservasi 
![Screenshot 2024-11-07 222901](https://github.com/user-attachments/assets/167a7772-fb71-4cdd-887f-222957601eca)
#### Jika anda memilih pilihan 5 maka anda bisa mencari jasa renovasi dengan mengetik keyword.

## Kembali
![Screenshot 2024-11-07 223121](https://github.com/user-attachments/assets/d282ec73-97ba-453c-ba05-d7427f0d8798)
#### Jika anda memilih pilihan 6 maka akan kembali ke menu utama.
