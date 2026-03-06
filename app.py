import streamlit as st
import random
from collections import Counter

# ==============================
# KONFIGURASI HALAMAN
# ==============================

st.set_page_config(
    page_title="BeSt Number Generator",
    layout="wide"
)

# ==============================
# JUDUL DAN PENJELASAN
# ==============================

st.title("BeSt Smart Number Generator")

st.markdown("""
Generator angka berbasis analisis pola sederhana yang menggabungkan:
- Frekuensi angka
- Distribusi digit
- Randomisasi terarah

Digunakan untuk menghasilkan kombinasi angka 2D sampai 5D.
""")

# ==============================
# STRATEGI
# ==============================

st.subheader("Strategi yang Digunakan")

st.markdown("""
1. **Frekuensi Angka**  
   Angka yang lebih sering muncul dalam proses randomisasi akan dianggap lebih kuat.

2. **Distribusi Digit**  
   Generator berusaha menyebarkan digit agar tidak terlalu berat di satu angka saja.

Sistem kemudian melakukan randomisasi untuk menghasilkan kandidat angka.
""")

# ==============================
# KETERANGAN WARNA
# ==============================

st.subheader("Keterangan Warna")

st.markdown("""
🟢 **Hijau (Top 10)**  
Angka ini termasuk dalam 10 angka paling kuat berdasarkan frekuensi hasil generator.

🔴 **Merah (Panas)**  
Angka yang memiliki frekuensi kemunculan tinggi tetapi tidak masuk 10 besar.

🔵 **Biru (Dingin)**  
Angka dengan frekuensi kemunculan rendah dalam hasil generator.
""")

# ==============================
# PERINGATAN
# ==============================

st.warning("""
⚠️ PERINGATAN SISTEM

Generator ini menggunakan analisis pola statistik sederhana dan randomisasi.

Metode yang digunakan:
- Frekuensi kemunculan angka
- Analisis distribusi digit
- Randomisasi kombinasi angka

Alat ini hanya digunakan sebagai referensi analisis pola, bukan jaminan hasil pasti.
""")

# ==============================
# INPUT USER
# ==============================

st.subheader("Pengaturan Generator")

col1, col2 = st.columns(2)

with col1:
    digit = st.selectbox(
        "Pilih Digit",
        [2,3,4,5]
    )

with col2:
    total_generate = st.number_input(
        "Jumlah Angka Generate",
        min_value=10,
        max_value=500,
        value=100
    )

# ==============================
# GENERATOR ANGKA
# ==============================

def generate_numbers(digit,total):

    numbers = []

    for _ in range(total):
        num = "".join(str(random.randint(0,9)) for _ in range(digit))
        numbers.append(num)

    return numbers


# ==============================
# PROSES GENERATE
# ==============================

if st.button("Generate Angka"):

    numbers = generate_numbers(digit,total_generate)

    freq = Counter(numbers)

    # 10 terbaik
    top10 = [x[0] for x in freq.most_common(10)]

    # batas panas
    threshold = max(freq.values()) * 0.6

    # ==============================
    # GRID HASIL
    # ==============================

    st.subheader("Hasil Generator")

    cols_per_row = 10
    rows = [numbers[i:i+cols_per_row] for i in range(0,len(numbers),cols_per_row)]

    for row in rows:

        cols = st.columns(cols_per_row)

        for i,num in enumerate(row):

            color = "#ADD8E6"  # dingin

            if num in top10:
                color = "#4CAF50"  # hijau
            elif freq[num] >= threshold:
                color = "#FF4B4B"  # panas

            cols[i].markdown(
                f"""
                <div style="
                background:{color};
                padding:10px;
                border-radius:6px;
                text-align:center;
                font-weight:bold;
                ">
                {num}
                </div>
                """,
                unsafe_allow_html=True
            )

    # ==============================
    # 10 TERBAIK
    # ==============================

    st.subheader("10 Angka Terkuat")

    best_cols = st.columns(10)

    for i,n in enumerate(top10):

        best_cols[i].markdown(
            f"""
            <div style="
            background:#4CAF50;
            padding:12px;
            border-radius:6px;
            text-align:center;
            font-size:18px;
            font-weight:bold;
            ">
            {n}
            </div>
            """,
            unsafe_allow_html=True
        )
