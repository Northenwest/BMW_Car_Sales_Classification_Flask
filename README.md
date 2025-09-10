# BMW_Car_Sales_Classification_Flask
Aplikasi web berbasis Flask untuk memprediksi klasifikasi penjualan mobil BMW menggunakan model Scikit-learn. Dilengkapi dengan dashboard manajemen data (CRUD) yang terintegrasi dengan database MySQL.


 🚗 Dashboard Prediksi & Manajemen Data Penjualan Mobil BMW

Ini adalah sebuah aplikasi web yang dibangun dengan Flask yang memiliki dua fungsi utama:
1.  Prediksi Machine Learning: Memprediksi klasifikasi penjualan mobil ('High' atau 'Low') berdasarkan fitur-fitur mobil menggunakan model yang sudah dilatih sebelumnya dengan Scikit-learn.
2.  Manajemen Data (CRUD): Menyediakan antarmuka untuk membuat (Create), membaca (Read), memperbarui (Update), dan menghapus (Delete) data mobil yang disimpan dalam database MySQL.

Aplikasi ini dirancang sebagai contoh integrasi antara data science dan web development dalam satu proyek yang fungsional.


(Sangat disarankan untuk menambahkan screenshot aplikasi Anda di sini agar lebih menarik!)

---

 ✨ Fitur Utama

-   Prediksi Penjualan: Form interaktif untuk memasukkan data mobil dan mendapatkan prediksi klasifikasi penjualan secara real-time.
-   Dashboard Data: Menampilkan semua data mobil dari database dalam bentuk tabel yang rapi.
-   Operasi CRUD Lengkap:
    -   Create: Menambah data mobil baru melalui modal form.
    -   Read: Melihat seluruh data dengan mudah.
    -   Update: Mengedit informasi mobil yang sudah ada.
    -   Delete: Menghapus data mobil dari database.
-   Antarmuka Responsif: Dibangun dengan Bootstrap 5 agar nyaman diakses dari berbagai perangkat.
-   Notifikasi Aksi: Memberikan pesan flash untuk setiap operasi yang berhasil (misal: "Data berhasil ditambahkan").

---

 🛠️ Teknologi yang Digunakan

-   Backend: Flask
-   Database: MySQL (dengan `Flask-MySQLdb`)
-   Machine Learning: Scikit-learn, Pandas
-   Frontend: HTML, CSS, Bootstrap 5, JavaScript (jQuery)
-   Bahasa: Python 3

---

 🚀 Panduan Instalasi & Setup

Ikuti langkah-langkah berikut untuk menjalankan proyek ini di lingkungan lokal Anda.

 1. Clone Repositori
```bash
git clone [https://github.com/NAMA_USER_ANDA/NAMA_REPO_ANDA.git](https://github.com/NAMA_USER_ANDA/NAMA_REPO_ANDA.git)
cd NAMA_REPO_ANDA
```

 2. Buat dan Aktifkan Virtual Environment
Sangat disarankan untuk menggunakan virtual environment.
```bash
 Membuat environment
python -m venv env

 Mengaktifkan di Windows
.\env\Scripts\activate

 Mengaktifkan di macOS/Linux
source env/bin/activate
```

 3. Install Dependensi
Install semua library Python yang dibutuhkan.
```bash
pip install -r requirements.txt
```

 4. Setup Database MySQL
-   Pastikan server MySQL Anda sudah berjalan.
-   Buat database baru (misalnya `bmw_sales_db`).
-   Buka file `schema.sql` dan jalankan isinya di SQL client Anda (seperti phpMyAdmin, DBeaver, atau terminal MySQL) untuk membuat tabel `cars`.

 5. Konfigurasi Aplikasi
Buka file `app.py` dan sesuaikan konfigurasi koneksi database dengan informasi Anda:
```python
 Ganti sesuai dengan konfigurasi MySQL Anda
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''  Isi password Anda jika ada
app.config['MYSQL_DB'] = 'bmw_sales_db'
```

---

 🏃 Cara Menjalankan Aplikasi

Setelah semua langkah setup selesai, jalankan perintah berikut dari terminal di direktori utama proyek:

```bash
python app.py
```
Aplikasi akan berjalan dalam mode debug di port 2020. Buka browser Anda dan kunjungi:
http://127.0.0.1:2020

---

 📂 Struktur Proyek
```
/
├── app.py                    Logika utama aplikasi Flask
├── best_bmw_sales_model.pkl  Model machine learning yang sudah dilatih
├── requirements.txt          Daftar dependensi Python
├── schema.sql                Skema untuk setup database
└── templates/
    └── index.html            File antarmuka web (frontend)
```

---

 📄 Lisensi

Proyek ini dilisensikan di bawah Lisensi MIT. Lihat file `LICENSE` untuk detail lebih lanjut.
(Anda bisa menambahkan file LICENSE.md dengan lisensi MIT jika mau)
