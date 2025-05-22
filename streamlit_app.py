import streamlit as st

st.title("🎈 khalissanadyamukti28maps")
st.write(
    "khalissanadyamukti28maps."
)
st.image("655793c8-2ea1-4d35-ab29-24066561fd3a.jpeg")
st.harder("Aplikasi Mengecek Nilai Genap/Ganjil")
angka = st.number_input("Tulis sebuah Angka:", value=0, step=1)

if (angka % 2) == 0:
 st.write(f"{angka} adalah bilangan genap")
else:
 st.write(f"{angka} adalah bilangan ganjil")
