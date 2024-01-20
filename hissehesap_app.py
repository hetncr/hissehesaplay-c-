#pip install streamlit

#%%writefile deneme.py
import streamlit as st

#streamlit.config.theme.base = "dark"
st.title("Hocalar Hisse Hesaplıyor  :chart:")
st.subheader("Road to Kıbrıs :airplane_departure: :sunglasses:")
#st.set_page_config(
# page_title="Hisse Hedef Fiyat Hesaplayıcı",
#  page_icon="https://example.com/icon.png",
#  layout="centered",
#)

#import streamlit_tags as tags

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

operation = st.selectbox("İşlem Seçimi:", ["F/K Hedef Fiyat", "P/D Hedef Fiyat", "ÖDENMİŞ SERMAYEYE GÖRE HEDEF FİYAT", "ÖZSERMAYE KARLILIĞINA GÖRE HEDEF FİYAT"])

# Calculate the target price based on the selected operation
if operation == "F/K Hedef Fiyat":
  if c10 != 0:
    fk_hedef_fiyat = c3 / c10 * c12
  else:
    fk_hedef_fiyat = 0

elif operation == "P/D Hedef Fiyat":
  if c11 != 0:
    pd_hedef_fiyat = c3 / c11 * c13
  else:
    pd_hedef_fiyat = 0

elif operation == "ÖDENMİŞ SERMAYEYE GÖRE HEDEF FİYAT":
  if c4 != 0:
    odenmis_hedef_fiyat = (c7 / c4) * c10
  else:
    odenmis_hedef_fiyat = 0

# Print the result of the selection
if operation == "F/K Hedef Fiyat":
  st.write(f"F/K HEDEF FİYAT: {fk_hedef_fiyat:,.2f}")

elif operation == "P/D Hedef Fiyat":
  st.write(f"P/D HEDEF FİYAT: {pd_hedef_fiyat:,.2f}")

elif operation == "ÖDENMİŞ SERMAYEYE GÖRE HEDEF FİYAT":
  st.write(f"ÖDENMİŞ SERMAYEYE GÖRE HEDEF FİYAT: {odenmis_hedef_fiyat:,.2f}")

elif operation == "ÖZSERMAYE KARLILIĞINA GÖRE HEDEF FİYAT":
  if c10 != 0:
    ozsermaye_hf = (c7/c8)*10/c11*c3
    st.write(f"ÖZSERMAYE KARLILIĞINA GÖRE HEDEF FİYAT: {ozsermaye_hf:,.2f}")

#if __name__ == "__main__":
#  st.run()


#!streamlit run deneme.py & npx localtunnel --port 8501
