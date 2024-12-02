import streamlit as st
import face_recognition
import cv2
import os
import pickle
import pandas as pd
from datetime import datetime

# Fungsi untuk memuat data pengguna dari file .pkl di folder 'user_data'
def load_user_data():
    user_encodings = {}  # Dictionary untuk menyimpan encoding wajah pengguna
    for user_file in os.listdir('user_data'):  # Iterasi semua file di folder 'user_data'
        with open(os.path.join('user_data', user_file), 'rb') as f:
            encoding = pickle.load(f)  # Membaca encoding dari file
            username = os.path.splitext(user_file)[0]  # Mendapatkan nama pengguna dari nama file
            user_encodings[username] = encoding  # Menyimpan encoding dengan username sebagai kunci
    return user_encodings

# Fungsi untuk mencocokkan encoding wajah yang diambil dengan encoding pengguna yang tersimpan
def login(face_encoding, user_encodings):
    for username, stored_encoding in user_encodings.items():  # Iterasi semua encoding pengguna
        match = face_recognition.compare_faces([stored_encoding], face_encoding)  # Perbandingan wajah
        if match[0]:  # Jika cocok, kembalikan nama pengguna
            return username
    return None  # Jika tidak cocok, kembalikan None

# Fungsi untuk mencatat login ke file 'login_logs.csv'
def record_login(username):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Mendapatkan waktu saat ini
    if os.path.exists('login_logs.csv'):  # Jika file log sudah ada, muat data
        df = pd.read_csv('login_logs.csv')
    else:  # Jika tidak ada, buat DataFrame kosong dengan kolom yang sesuai
        df = pd.DataFrame(columns=["username", "timestamp"])
    
    # Membuat data baru untuk log login
    new_entry = pd.DataFrame({"username": [username], "timestamp": [timestamp]})
    df = pd.concat([df, new_entry], ignore_index=True)  # Gabungkan dengan data log yang ada
    df.to_csv('login_logs.csv', index=False)  # Simpan ke file CSV

# Tampilan header halaman login
st.header("Login")

# Memuat data pengguna
user_encodings = load_user_data()

# Input kamera untuk mengambil foto saat login
captured_image = st.camera_input("Ambil foto untuk login")

# Placeholder untuk kotak input nama pengguna (jika terdeteksi)
name_box = st.empty()

# Jika gambar dari kamera sudah diambil
if captured_image is not None:
    img = face_recognition.load_image_file(captured_image)  # Memuat gambar dari input kamera
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Konversi gambar ke RGB untuk OpenCV
    face_locations = face_recognition.face_locations(img)  # Deteksi lokasi wajah
    face_encodings = face_recognition.face_encodings(img, face_locations)  # Dapatkan encoding wajah

    # Jika ada wajah yang terdeteksi
    if face_encodings:
        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            # Gambarkan kotak hijau di sekitar wajah
            cv2.rectangle(img_rgb, (left, top), (right, bottom), (0, 255, 0), 2)
            
            # Mencoba mencocokkan wajah dengan data pengguna
            username = login(face_encoding, user_encodings)
            if username:
                # Jika wajah cocok dengan data pengguna, Menampilkan pesan berhasil
                st.success(f"Login berhasil! Selamat datang, {username}.")
                record_login(username)  # Catat login ke file CSV
                
                # Menambahkan nama pengguna di atas kotak hijau
                cv2.putText(img_rgb, username, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
                # Menampilkan nama pengguna di kotak input Streamlit
                name_box.text_input("Nama Pengguna:", value=username, disabled=True)
            else:
                # Jika wajah tidak cocok, menampilkan pesan error
                st.error("Wajah tidak dikenali. Silakan coba lagi.")
                cv2.putText(img_rgb, "Tidak Dikenal", (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
                name_box.text_input("Nama Pengguna:", value="Tidak Dikenal", disabled=True)
        
        # menampilkan gambar dengan kotak hijau dan teks nama pengguna
        st.image(img_rgb, channels="RGB")

    else:
        # Jika tidak ada wajah yang terdeteksi, menampikan peringatan
        st.warning("Tidak ada wajah yang terdeteksi.")
