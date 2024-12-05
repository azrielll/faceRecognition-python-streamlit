import streamlit as st


# Header Utama
st.title("Sistem Absensi Berbasis Face Recognition")
st.markdown(
    """
    Selamat datang di **Sistem Absensi Otomatis Berbasis Pengenalan Wajah**.  
    Aplikasi ini dirancang untuk mempermudah proses absensi dengan teknologi pengenalan wajah yang akurat.
    """
)



# Informasi tambahan
st.write(
    """
    ### Fitur Utama:
    - **Login:** Absen otomatis dengan memindai wajah Anda.
    - **Registrasi:** Menambahkan data wajah baru ke database.
    - **Database:** Lihat riwayat pengguna absensi dan waktu absensi yang telah terekam.

    Silakan gunakan tombol di bawah ini untuk menavigasi ke fitur yang tersedia.
    """
)

# Tambahkan tautan navigasi ke halaman login di sidebar
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Login"):
        st.switch_page("pages/login.py")

with col2:
    if st.button("Register"):
        st.switch_page("pages/register.py")

with col3:
    if st.button("Database"):
        st.switch_page("pages/data.py")



