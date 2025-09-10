from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
import joblib
import pandas as pd
import numpy as np

# Inisialisasi aplikasi Flask
app = Flask(__name__)

# Konfigurasi Koneksi MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root' # Ganti dengan username Anda
app.config['MYSQL_PASSWORD'] = '' # Ganti dengan password Anda
app.config['MYSQL_DB'] = 'bmw_sales_db'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor' # Mengembalikan hasil sebagai dictionary

# Kunci rahasia untuk flash messages
app.secret_key = 'kunci_rahasia_flask'

# Inisialisasi MySQL
mysql = MySQL(app)

# Memuat model .pkl yang sudah dilatih
try:
    model = joblib.load('best_bmw_sales_model.pkl')
    print("Model berhasil dimuat.")
except FileNotFoundError:
    print("File model tidak ditemukan! Pastikan 'best_bmw_sales_model.pkl' ada di direktori yang sama.")
    model = None

# Mapping hasil prediksi (0/1) ke label ('Low'/'High')
prediction_mapping = {0: 'Low', 1: 'High'}

# --- Routes untuk Fitur ---

# Halaman utama: Menampilkan data (Read) dan form prediksi
@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM cars ORDER BY id DESC")
    data = cur.fetchall()
    cur.close()
    return render_template('index.html', cars=data)

# Fitur Prediksi
@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        flash("Model Machine Learning tidak berhasil dimuat.", "danger")
        return redirect(url_for('index'))

    # Mengambil data dari form
    try:
        features = {
            'Model': [request.form['Model']],
            'Year': [int(request.form['Year'])],
            'Region': [request.form['Region']],
            'Color': [request.form['Color']],
            'Fuel_Type': [request.form['Fuel_Type']],
            'Transmission': [request.form['Transmission']],
            'Engine_Size_L': [float(request.form['Engine_Size_L'])],
            'Mileage_KM': [int(request.form['Mileage_KM'])],
            'Price_USD': [int(request.form['Price_USD'])],
            'Sales_Volume': [int(request.form['Sales_Volume'])]
        }
        
        # Membuat DataFrame dari input
        input_df = pd.DataFrame.from_dict(features)
        
        # Melakukan prediksi
        prediction_code = model.predict(input_df)[0]
        prediction_label = prediction_mapping.get(prediction_code, "Tidak diketahui")
        
        flash(f'Hasil Prediksi Klasifikasi Penjualan: {prediction_label}', 'success')

    except Exception as e:
        flash(f"Terjadi error saat prediksi: {e}", "danger")

    return redirect(url_for('index'))

# Fitur Tambah Data (Create)
@app.route('/add', methods=['POST'])
def add_car():
    if request.method == 'POST':
        details = request.form
        cur = mysql.connection.cursor()
        cur.execute(
            """
            INSERT INTO cars(Model, Year, Region, Color, Fuel_Type, Transmission, Engine_Size_L, Mileage_KM, Price_USD, Sales_Volume)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """,
            (details['Model'], details['Year'], details['Region'], details['Color'], details['Fuel_Type'],
             details['Transmission'], details['Engine_Size_L'], details['Mileage_KM'], details['Price_USD'], details['Sales_Volume'])
        )
        mysql.connection.commit()
        cur.close()
        flash('Data Mobil Berhasil Ditambahkan', 'success')
        return redirect(url_for('index'))

# Fitur Edit Data (Update)
@app.route('/edit/<int:id>', methods=['POST'])
def edit_car(id):
    details = request.form
    cur = mysql.connection.cursor()
    cur.execute(
        """
        UPDATE cars SET
        Model=%s, Year=%s, Region=%s, Color=%s, Fuel_Type=%s, Transmission=%s,
        Engine_Size_L=%s, Mileage_KM=%s, Price_USD=%s, Sales_Volume=%s
        WHERE id=%s
        """,
        (details['Model'], details['Year'], details['Region'], details['Color'], details['Fuel_Type'],
         details['Transmission'], details['Engine_Size_L'], details['Mileage_KM'],
         details['Price_USD'], details['Sales_Volume'], id)
    )
    mysql.connection.commit()
    cur.close()
    flash('Data Mobil Berhasil Diperbarui', 'success')
    return redirect(url_for('index'))

# Fitur Hapus Data (Delete)
@app.route('/delete/<int:id>')
def delete_car(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM cars WHERE id=%s", (id,))
    mysql.connection.commit()
    cur.close()
    flash('Data Mobil Berhasil Dihapus', 'warning')
    return redirect(url_for('index'))

# Menjalankan aplikasi
if __name__ == '__main__':
    app.run(host=82.197.71.171, port=2020, debug=True)