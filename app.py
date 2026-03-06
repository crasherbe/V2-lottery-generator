import streamlit as st
import pandas as pd

from strategy import analyze_history
from generator import generate_numbers
from analyzer import strongest_digits
from predictor import top_predictions

st.title("Smart Lottery Number Generator")

st.subheader("Penjelasan Sistem")

st.write("""
Aplikasi ini menghasilkan kombinasi angka berdasarkan analisa data result sebelumnya.
Generator menggunakan strategi statistik yang sering dipakai untuk membaca pola angka.
""")

st.subheader("Strategi yang Digunakan")

st.write("""
1. Hot Number → angka yang sering muncul pada history
2. Cold Number → angka yang jarang muncul
3. Pola Genap - Ganjil
4. Pola Besar - Kecil
5. Kombinasi berdasarkan analisa digit terkuat
""")

st.subheader("Input Data Result")

history_text = st.text_area(
"Masukkan history result (1 angka per baris)"
)

digit = st.selectbox(
"Pilih Digit",
[2,3,4,5]
)

total = st.number_input(
"Jumlah angka yang ingin di generate",
min_value=5,
max_value=500,
value=50
)

# Toggle warna
color_toggle = st.checkbox("Aktifkan Warna Analisa", value=True)

if st.button("Generate Angka"):

    history = history_text.split()

    hot, cold = analyze_history(history)

    st.write("Hot Numbers:", hot)
    st.write("Cold Numbers:", cold)

    numbers = generate_numbers(digit, total, hot, cold)

    top_numbers = top_predictions(numbers)

    st.subheader("Keterangan Warna Hasil Generator")

    st.markdown("""
🟩 **Hijau (Prediksi Terkuat)**  
Kombinasi ini termasuk dalam **10 kombinasi terbaik dari hasil analisa generator**.

🟥 **Merah (Hot Digit)**  
Kombinasi ini mengandung **digit yang sering muncul dalam history**.

🟦 **Biru (Cold Digit)**  
Kombinasi ini mengandung **digit yang jarang muncul dalam history**.
""")

    st.subheader("Hasil Generate")

    row_size = 10
    rows = [numbers[i:i+row_size] for i in range(0, len(numbers), row_size)]

    df = pd.DataFrame(rows)

    if color_toggle:

        def highlight_numbers(val):

            val_str = str(val)

            if val_str in top_numbers:
                return "background-color:#00ff00; color:black; font-weight:bold"

            if any(int(d) in hot for d in val_str):
                return "background-color:#ff4d4d; color:white"

            if any(int(d) in cold for d in val_str):
                return "background-color:#4da6ff; color:white"

            return ""

        styled = df.style.map(highlight_numbers)

        st.dataframe(styled, use_container_width=True)

    else:

        st.dataframe(df, use_container_width=True)

    st.subheader("10 Prediksi Kombinasi Terkuat")

    row_size2 = 5
    rows2 = [top_numbers[i:i+row_size2] for i in range(0, len(top_numbers), row_size2)]

    df2 = pd.DataFrame(rows2)

    st.dataframe(df2, use_container_width=True)

    # Copy angka terbaik
    copy_text = " ".join(top_numbers)

    st.text_area(
        "Copy 10 Angka Terbaik",
        value=copy_text,
        height=70
    )

    top_digits = strongest_digits(numbers)

    st.subheader("10 Angka Digit Terkuat")

    for num, count in top_digits:
        st.write(f"Angka {num} muncul {count} kali")
