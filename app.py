import datetime
import streamlit as st

st.set_page_config(
    page_title = "DIGITOP",
    page_icon = "🛒"
)

with st.sidebar :
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.image("digitop-logo-bulat.png")
    st.title("🛒💎DIGITOP")
    menu = st.selectbox("Pilihan Menu", ["💎Beli Diamond", "🔍Cek Riwayat Transaksi", "📌Deskripsi Mobile Legends"])
    st.caption("Dibuat dengan :fire: oleh **Kelompok 9**")


# --- 1. DATA KATALOG & PROMO (Menggunakan Tuple)
KATALOG_DIGITOP_ML = (
    ("💎Weekly Diamond Pass", 28000),
    ("💎86 Diamonds (78 + 8 Bonus)", 20000),
    ("💎172 Diamonds (156 + 16 Bonus)", 40000),
    ("💎257 Diamonds (234 + 23 Bonus)", 60000),
    ("💎344 Diamonds (312 + 32 Bonus)", 80000),
    ("💎514 Diamonds (468 + 46 Bonus)", 120000),
    ("💎706 Diamonds (625 + 81 Bonus)", 160000),
)

DAFTAR_PROMO = (
    ("Tanpa Promo", 0.0, 0),
    ("NEWTOP (Spesial Akun Baru - Diskon 20%)🎁", 0.20, 0),
    ("JUMATBERKAH (Spesial Hari Jumat - Diskon 15%)🔥", 0.15, 0),
    ("PROMOGAMERS (Min. Belanja Rp 50.000 - Diskon 10%)⭐", 0.10, 50000),
)

# --- 2. INISIALISASI SESSION STATE UNTUK RIWAYAT ---
if "riwayat_transaksi" not in st.session_state:
    st.session_state.riwayat_transaksi = []

# --- 3. TAMPILAN WEB (UI) ---
st.title("🛒 DIGITOP 💎 - Digital Top Up Diamond Mobile Legends: Bang Bang 🎮")
st.markdown ("⚡️Proses Cepat & Otomatis, 💬Jaminan Layanan 24 Jam, ✅Pembayaran Aman & Terpercaya📞💵")

if menu == "💎Beli Diamond":
    st.subheader("Beli Diamond Mobile Legends: Bang Bang 🎮")

    # Input User ID & Zone ID
    akun_id = st.text_input("Masukkan Akun ID (Cth: 12345678 / Min 8 digit)")
    server_id = st.text_input("Masukkan Server ID (Cth: 1234 / Min 4 digit)")

    # Pilihan Produk (Dropdown)
    pilihan_produk = st.selectbox(
        "Pilih Produk",
        KATALOG_DIGITOP_ML,
        format_func=lambda x: f"{x[0]} - Rp {x[1]:,}"
    )

    # Pilihan Promo
    pilihan_promo = st.selectbox(
        "Pilih Promo 🎟️", 
        DAFTAR_PROMO,
        format_func=lambda x: x[0]
    )

    # Pilihan Metode Pembayaran
    pilihan_metode = st.selectbox(
        "Metode Pembayaran 💳",
        (
              "1. GoPay (Admin Rp 0)",
              "2. OVO (Admin Rp 1.000)",
              "3. DANA (Admin Rp 1.000)",
              "4. ShoppePay (Admin Rp 1.000)",
              "5. Virtual Account Bank (Admin Rp 1.500)",
              "6. Alfamart / Indomaret (Admin Rp 2.500)",
        ),
    )
    nama_metode = ""
    biaya_admin = 0

    if pilihan_metode == "1. GoPay (Admin Rp 0)":
        nama_metode = "E-Wallet: GoPay"
        biaya_admin = 0
    elif pilihan_metode == "2. OVO (Admin Rp 1.000)":
        nama_metode = "E-Wallet: OVO"
        biaya_admin = 1000
    elif pilihan_metode == "3. DANA (Admin Rp 1.000)":
        nama_metode = "E-Wallet: DANA"
        biaya_admin = 1000
    elif pilihan_metode == "4. ShoppePay (Admin Rp 1.000)":
        nama_metode = "E-Wallet: ShopeePay"
        biaya_admin = 1000
    elif pilihan_metode == "5. Virtual Account Bank (Admin Rp 1.500)":
        nama_metode = "Virtual Account Bank"
        biaya_admin = 1500
    elif pilihan_metode == "6. Alfamart / Indomaret (Admin Rp 2.500)":
        nama_metode = "Alfamart/Indomaret"
        biaya_admin = 2500
    else:
        nama_metode = "E-Wallet: GoPay (Default)"
        biaya_admin = 0
    
    # --- PERHITUNGAN OTOMATIS HARGA ---
    harga_dasar = pilihan_produk[1]
    diskon_persen = pilihan_promo[1]
    min_belanja = pilihan_promo[2]

    # Cek apakah memenuhi syarat minimum belanja promo
    if harga_dasar >= min_belanja:
        potongan_harga = harga_dasar * diskon_persen
    else:
        potongan_harga = 0.0

    harga_setelah_diskon = harga_dasar - potongan_harga
    total_bayar = harga_setelah_diskon + biaya_admin

        # Tombol Eksekusi
    if st.button("Pesan Sekarang", type="primary"):
        # Logika validasi sederhana
        if (
            not akun_id.isdigit()
            or len(akun_id) < 8
            or not server_id.isdigit()
            or len(server_id) < 4
        ):
            st.error("User ID atau Zone ID tidak valid!")
        else:
            st.success("✅Transaksi Berhasil! Diamond otomatis masuk ke akun Mobile Legends Anda..")

            # Simpan ke riwayat (Session State)
            waktu_trx = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            st.session_state.riwayat_transaksi.append(
                {
                    "waktu": waktu_trx,
                    "tujuan": f"{akun_id} ({server_id})",
                    "produk": pilihan_produk[0],
                    "metode": nama_metode,
                    "promo": pilihan_promo[0],
                    "total": f"Rp {int(total_bayar):,}",
                }
            )

elif menu == "🔍Cek Riwayat Transaksi":
    st.subheader("🔍Daftar Riwayat Transaksi Sesi Ini")
    if len(st.session_state.riwayat_transaksi) == 0:
        st.info("Belum ada transaksi.")
    else:
        for idx, trx in enumerate(st.session_state.riwayat_transaksi, 1):
            st.write(
                f"**{idx}. Waktu:** {trx['waktu']} | **Tujuan:** {trx['tujuan']} | **Produk:** {trx['produk']} | **Metode:** {trx['metode']} | **Promo:** {trx['promo']} | **Total:** {trx['total']}"
            )

elif menu == "📌Deskripsi Mobile Legends":
    st.subheader("Mobile Legends: Bang Bang 🎮")
    # --- 4. KOTAK DESKRIPSI / PERATURAN & PANDUAN DI BAGIAN BAWAH ---
    # Menggunakan st.container dengan border (Streamlit v1.30+)
    with st.container(border=True):
        st.markdown("### 📌 **Informasi & Panduan Transaksi DIGITOP**")
        st.markdown(
        """
        **DIGITOP** mempersembahkan penawaran istimewa untuk para gamers sejati! Kami hadir dengan layanan Top Up resmi dan 100% legal untuk **Mobile Legends : Bang Bang**, yang dirancang khusus untuk meningkatkan pengalaman bermain game Anda. Nikmati kemudahan, keamanan, dan harga yang terjangkau dalam setiap transaksi Top Up Anda.
        
        #### **Top Up Mobile Legends : Bang Bang Resmi, Murah, Aman, & Terpercaya**
        Berikut adalah langkah-langkah sederhana untuk Top Up Mobile Legends : Bang Bang:
        
        1. **Masukkan Data Akun Mobile Legends : Bang Bang** (Pastikan User ID dan Server ID yang Anda masukkan sudah benar dan lengkap).
        2. **Pilih Nominal Diamond** (Kami menyediakan berbagai pilihan nominal yang bisa Anda sesuaikan dengan kebutuhan).
        3. **Pilih Metode Pembayaran** (Kenyamanan Anda adalah prioritas kami. Kami menyediakan berbagai metode pembayaran yang mudah dan aman).
        4. **Pilih Kode Promo** (Gunakan kode promo untuk mendapatkan penawaran spesial dan diskon menarik).
        5. **Klik Pesan Sekarang** (Proses mudah dan cepat, kini Anda tinggal selangkah lagi untuk meningkatkan pengalaman gaming Anda).
        6. **Diamond Akan Masuk Otomatis ke Akun Anda** (Tunggu dan rasakan sensasi permainan yang lebih seru dengan cepat dan aman).
        
        *DIGITOP Sahabat Para Gamers!* 🎮💎
        """
    )