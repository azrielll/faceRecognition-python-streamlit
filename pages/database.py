import streamlit as st
import pandas as pd
import os

# Fungsi untuk memuat data pengguna dari folder 'user_data'
def load_user_data():
    """
    Memuat nama-nama pengguna yang terdaftar berdasarkan file dalam folder 'user_data'.
    
    Returns:
    list: Daftar nama pengguna (dari nama file tanpa ekstensi).
    """
    user_files = os.listdir('user_data')  # Mendapatkan daftar semua file dalam folder 'user_data'
    return [os.path.splitext(file)[0] for file in user_files]  # Menghapus ekstensi file dan mengembalikan nama pengguna

# Fungsi untuk memuat riwayat login dari file 'login_logs.csv'
def load_login_logs():
    """
    Memuat data riwayat login dari file CSV.
    
    Returns:
    DataFrame: Data login dengan kolom 'username' dan 'timestamp'.
    """
    if os.path.exists('login_logs.csv'):  # Mengecek apakah file 'login_logs.csv' ada
        return pd.read_csv('login_logs.csv')  # Memuat data dari file CSV jika ada
    return pd.DataFrame(columns=["username", "timestamp"])  # Mengembalikan DataFrame kosong jika file tidak ada

# Menampilkan daftar pengguna yang terdaftar
st.subheader("Data Pengguna:")
user_data = load_user_data()  # Memuat data pengguna
if user_data:
    st.write(user_data)  # Menampilkan daftar nama pengguna
else:
    st.info("Belum ada pengguna yang terdaftar.")  # Menampilkan pesan jika tidak ada data pengguna

# Menampilkan riwayat login
st.subheader("Riwayat Login:")
login_logs = load_login_logs()  # Memuat data login
if not login_logs.empty:
    st.dataframe(login_logs)  # Menampilkan data login dalam bentuk tabel
else:
    st.info("Belum ada riwayat login.")  # Menampilkan pesan jika tidak ada riwayat login
