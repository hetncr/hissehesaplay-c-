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

#operation = st.selectbox("İşlem Seçimi:", ["F/K Hedef Fiyat", "P/D Hedef Fiyat", "ÖDENMİŞ SERMAYEYE GÖRE HEDEF FİYAT", "ÖZSERMAYE KARLILIĞINA GÖRE HEDEF FİYAT"])

# Calculate the target price based on the selected operation
#if operation == "F/K Hedef Fiyat":
  #if c10 != 0:
    #fk_hedef_fiyat = c3 / c10 * c12
  #else:
    #fk_hedef_fiyat = 0

#elif operation == "P/D Hedef Fiyat":
  #if c11 != 0:
    #pd_hedef_fiyat = c3 / c11 * c13
  #else:
    #pd_hedef_fiyat = 0

#elif operation == "ÖDENMİŞ SERMAYEYE GÖRE HEDEF FİYAT":
  #if c4 != 0:
    #odenmis_hedef_fiyat = (c7 / c4) * c10
  #else:
    #odenmis_hedef_fiyat = 0

# Print the result of the selection
#if operation == "F/K Hedef Fiyat":
  #st.write(f"F/K HEDEF FİYAT: {fk_hedef_fiyat:,.2f}")

#elif operation == "P/D Hedef Fiyat":
  #st.write(f"P/D HEDEF FİYAT: {pd_hedef_fiyat:,.2f}")

#elif operation == "ÖDENMİŞ SERMAYEYE GÖRE HEDEF FİYAT":
  #st.write(f"ÖDENMİŞ SERMAYEYE GÖRE HEDEF FİYAT: {odenmis_hedef_fiyat:,.2f}")

#elif operation == "ÖZSERMAYE KARLILIĞINA GÖRE HEDEF FİYAT":
  #if c10 != 0:
    #ozsermaye_hf = (c7/c8)*10/c11*c3
    #st.write(f"ÖZSERMAYE KARLILIĞINA GÖRE HEDEF FİYAT: {ozsermaye_hf:,.2f}")

#if __name__ == "__main__":
#  st.run()

#!streamlit run deneme.py & npx localtunnel --port 8501

operation = st.selectbox(":blue[**HİSSE FİYAT HESAPLAMARI İÇİN İŞLEM SEÇİN:**]", ["İŞLEM SEÇİN", "F/K HEDEF FİYAT", "PD/DD HEDEF FİYAT", "ÖDENMİŞ SERMAYEYE GÖRE HEDEF FİYAT", "ÖZSERMAYE KARLILIĞINA GÖRE HEDEF FİYAT", "TÜM HESAPLAMALARIN SONUÇLARINI GÖSTER"])
  #if operation == "Tüm Hedef Fiyatları Göster":
if operation == "İŞLEM SEÇİN":
  st.write(f"İŞLEM SEÇİN")
  st.write(f":red[Aşağıdaki kırmızı uyarı yazısı veriler girilmediği için çıkmaktadır. Lütfen verileri girip yapmak istediğiniz işlemi seçin.]")

elif operation == "F/K HEDEF FİYAT":
  if c10 != 0:
    fk_hedef_fiyat = c3 / c10 * c12
  else:
    fk_hedef_fiyat = 0
    st.write(f":blue[**F/K HEDEF FİYAT:**] {fk_hedef_fiyat:,.2f}")
    st.write(f" :chart:**:blue[HİSSE FİYATI:]**  {kapanıs}")

elif operation == "PD/DD HEDEF FİYAT":
   if c11 != 0:
     pd_hedef_fiyat = c3 / c11 * c13
   else:
     pd_hedef_fiyat = 0
     st.write(f":blue[**PD/DD HEDEF FİYAT:**] {pd_hedef_fiyat:,.2f}")
     st.write(f" :chart:**:blue[HİSSE FİYATI:]**  {kapanıs}")

  elif operation == "ÖDENMİŞ SERMAYEYE GÖRE HEDEF FİYAT":
    if c4 != 0:
      odenmis_hedef_fiyat = (c7 / c4) * c10
    #else:
      #odenmis_hedef_fiyat = 0
      st.write(f":blue[ÖDENMİŞ SERMAYEYE GÖRE HEDEF FİYAT:] {odenmis_hedef_fiyat:,.2f}")
      st.write(f"   :chart:**:blue[HİSSE FİYATI:]**  {kapanıs}")
  #elif operation == "ÖDENMİŞ SERMAYEYE GÖRE HEDEF FİYAT":
    #st.write(f"ÖDENMİŞ SERMAYEYE GÖRE HEDEF FİYAT: {odenmis_hedef_fiyat:,.2f}")
      st.write(f":red[Not: Hisse verilerini kontrol ediniz. Eksik veri nedeniyle altta kırmızı alanda hata mesajı çıkmaktadır]")
  elif operation == "ÖZSERMAYE KARLILIĞINA GÖRE HEDEF FİYAT":
    #if c10 != 0:
    ozsermaye_hf = (c7/c8)*10/c11*c3
    st.write(f":blue[ÖZSERMAYE KARLILIĞINA GÖRE HEDEF FİYAT]: {ozsermaye_hf:,.2f}")
    st.write(f" :chart:**:blue[HİSSE FİYATI:]**  {kapanıs}")
    st.write(f":red[Not: Hisse verilerini kontrol ediniz. Eksik veri nedeniyle altta kırmızı alanda hata mesajı çıkmaktadır]")
  elif operation == "TÜM HESAPLAMALARIN SONUÇLARINI GÖSTER":
    c21 = (c7*7)+(c8*0.5)
    potansiyel_fiyat = c21/c4
    st.write(f":blue[**POTANSİYEL DEĞERİNE GÖRE HİSSE FİYATI:**] {potansiyel_fiyat:,.2f}")
    #st.write(f":red[Not: Hisse verilerini kontrol ediniz. Eksik veri nedeniyle altta kırmızı alanda hata mesajı çıkmaktadır]")
  #operation = st.selectbox("[ORTALAMA HEDEF FİYAT]")
    fk_hedef_fiyat = c3 / c10 * c12
    pd_hedef_fiyat = c3 / c11 * c13
    ozsermaye_hf = (c7/c8)*10/c11*c3
    odenmis_hedef_fiyat = (c7 / c4) * c10
    c21 = (c7*7)+(c8*0.5)
    potansiyel_fiyat = c21/c4
    ortalama_hesap = ( fk_hedef_fiyat + pd_hedef_fiyat + odenmis_hedef_fiyat + ozsermaye_hf + potansiyel_fiyat ) / 5
  #if operation == "ORTALAMA HEDEF FİYAT":
  #st.write(ortalama_hesap)
  #if ortalama_hesap < kapanıs :
    #st.write(f":blue[**TÜM HESAPLAMALARIN ORTALAMA FİYATI:**] {ortalama_hesap:,.2f}")
  #else :
    #st.write(f"**TÜM HESAPLAMALARIN ORTALAMA FİYATI:** :green[{ortalama_hesap:,.2f}]")
  #elif operation == "TÜM HESAPLAMALARIN SONUÇLARINI GÖSTER":
    st.write(f":blue[**F/K HEDEF FİYAT:**] {fk_hedef_fiyat:,.2f}")
    st.write(f":blue[**PD/DD HEDEF FİYAT:**] {pd_hedef_fiyat:,.2f}")
    st.write(f":blue[**ÖDENMİŞ SERMAYEYE GÖRE HEDEF FİYAT:**] {odenmis_hedef_fiyat:,.2f}")
    st.write(f":blue[**ÖZSERMAYE KARLILIĞINA GÖRE HEDEF FİYAT**]: {ozsermaye_hf:,.2f}")
    st.write(f":chart:**:blue[TÜM HESAPLAMALARIN ORTALAMA FİYATI:]** {ortalama_hesap:,.2f}")
    st.write(f" :chart:**:blue[HİSSE FİYATI:]**  {kapanıs}")
