#pip install streamlit

#%%writefile deneme.py
import streamlit as st

#streamlit.config.theme.base = "dark"
st.title("Hisse Hedef Fiyat Hesaplayıcı")
st.set_page_config(
  page_title="Hisse Hedef Fiyat Hesaplayıcı",
  page_icon="https://example.com/icon.png",
  layout="centered",
)

import streamlit_tags as tags

st.write("Hisse Hedef Fiyat Hesaplayıcı")
# Hisse Fiyatı
c3 = st.number_input("Hisse Fiyatı:" )

# Hisse F/K Oranı
c10 = float(st.number_input("Hisse F/K Oranı:"))

# HİSSE PD/DD ORANI
c11 = st.number_input("Hisse PD/DD Oranı: ")

# BİST100 /SEKTÖR GÜNCEL F/K ORANI
c12 = st.number_input("BİST100 / Sektör Güncel F/K Oranı: ")

# BIST100 / Sektör Güncel P/D Oranı
c13 = float(st.number_input("BİST100 / Sektör Güncel PD/DD Oranı:"))

# Ödenmiş Sermaye
c4 = st.number_input("Ödenmiş Sermaye: ")

# Yıllık Net Kar
c7 = st.number_input("Yıllık Net Kar: ")

# Özsermaye
c8 = st.number_input("Özsermaye : ")

# Güncel Piyasa Değeri
#c9 = st.number_input("Güncel Piyasa Değeri: ")

operation = st.selectbox("İşlem Seçimi:", ["F/K Hedef Fiyat", "P/D Hedef Fiyat", "ÖDENMİŞ SERMAYEYE GÖRE HEDEF FİYAT"])

# Calculate the target price based on the selected operation
if operation == "F/K Hedef Fiyat":
  if c10 != 0:
    fk_hedef_fiyat = c3 / c10 * c13
  else:
    fk_hedef_fiyat = 0

elif operation == "P/D Hedef Fiyat":
  if c10 != 0:
    pd_hedef_fiyat = c3 / c11 * c13
  else:
    pd_hedef_fiyat = 0

elif operation == "ÖDENMİŞ SERMAYEYE GÖRE HEDEF FİYAT":
  if c10 != 0:
    odenmis_hedef_fiyat = (c7 / c4) * c10
  else:
    odenmis_hedef_fiyat = 0

# Print the result of the selection
if operation == "F/K Hedef Fiyat":
  st.write(f"F/K Hedef Fiyat: {fk_hedef_fiyat}")

elif operation == "P/D Hedef Fiyat":
  st.write(f"P/D Hedef Fiyat: {pd_hedef_fiyat}")

elif operation == "ÖDENMİŞ SERMAYEYE GÖRE HEDEF FİYAT":
  st.write(f"ÖDENMİŞ SERMAYEYE GÖRE HEDEF FİYAT: {odenmis_hedef_fiyat}")

if __name__ == "__main__":
  st.run()


#!streamlit run deneme.py & npx localtunnel --port 8501
