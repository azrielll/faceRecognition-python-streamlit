import streamlit as st
import face_recognition
import os
import pickle

# Fungsi untuk menyimpan data pengguna ke file
def save_user_data(username, encoding):
    """
    Menyimpan encoding wajah pengguna ke dalam file .pkl.
    
    Parameters:
    username (str): Nama pengguna yang akan disimpan.
    encoding (list): Encoding wajah pengguna.
    """
    user_file = os.path.join('user_data', f"{username}.pkl")  # Buat path file dengan nama pengguna
    with open(user_file, 'wb') as f:  # Buka file dalam mode tulis biner
        pickle.dump(encoding, f)  # Simpan encoding wajah ke file

# Menampilkan header halaman registrasi
st.header("Register")

# Input untuk nama pengguna
username = st.text_input("Masukkan Nama Pengguna")

# Input kamera untuk mengambil foto pengguna
captured_image = st.camera_input("Ambil foto untuk registrasi")

# Jika nama pengguna dan gambar tersedia
if username and captured_image is not None:
    img = face_recognition.load_image_file(captured_image)  # Memuat gambar dari input kamera
    face_locations = face_recognition.face_locations(img)  # Mendeteksi lokasi wajah dalam gambar
    face_encodings = face_recognition.face_encodings(img, face_locations)  # Mendapatkan encoding wajah

    # Jika encoding wajah ditemukan
    if face_encodings:
        save_user_data(username, face_encodings[0])  # Simpan encoding wajah ke file
        st.success(f"Registrasi berhasil! Selamat datang, {username}.")  # Tampilkan pesan sukses
    else:
        st.warning("Tidak ada wajah yang terdeteksi.")  # Tampilkan peringatan jika wajah tidak terdeteksi
