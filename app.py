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
Generator menggunakan strategi yang sering digunakan dalam analisa angka.
""")

st.subheader("Strategi yang Digunakan")

st.write("""
1. Hot Number (angka yang sering muncul)
2. Cold Number (angka yang jarang muncul)
3. Pola Genap - Ganjil
4. Pola Besar - Kecil
5. Kombinasi dari hasil analisa history
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

if st.button("Generate Angka"):

    history = history_text.split()

    hot, cold = analyze_history(history)

    st.write("Hot Numbers:", hot)
    st.write("Cold Numbers:", cold)

    numbers = generate_numbers(digit, total, hot, cold)

    st.subheader("Hasil Generate")

    row_size = 10
    rows = [numbers[i:i+row_size] for i in range(0, len(numbers), row_size)]

    df = pd.DataFrame(rows)

    st.dataframe(df, use_container_width=True)

    top_digits = strongest_digits(numbers)

    st.subheader("10 Angka Digit Terkuat")

    for num, count in top_digits:
        st.write(f"Angka {num} muncul {count} kali")

    st.subheader("10 Prediksi Kombinasi Terkuat")

    top_numbers = top_predictions(numbers)

    row_size2 = 5
    rows2 = [top_numbers[i:i+row_size2] for i in range(0, len(top_numbers), row_size2)]

    df2 = pd.DataFrame(rows2)

    st.dataframe(df2, use_container_width=True)
