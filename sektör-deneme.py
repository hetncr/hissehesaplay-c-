!pip install streamlit

pip install beautifulsoup4

pip install requests

pip install pandas

import requests
from bs4 import BeautifulSoup
import streamlit as st

# Load the hisse_adlari[] list
hisse_adlari = ["A1CAP", "ACSEL", "ADEL"]

# Create the selectbox
hisse_select = st.selectbox("Hisse Seçin:", hisse_adlari)

# Get the selected stock
hisse = hisse_select

# Web scrapping code to get the sektör name
url = "https://www.isyatirim.com.tr/tr-tr/analiz/hisse/Sayfalar/Temel-Degerler-Ve-Oranlar.aspx?"
response = requests.get(url)
temeldegerler = BeautifulSoup(response.text, "html.parser")

# Find the table with the desired data
table = temeldegerler.find("tbody", id="temelTBody_Ozet")

# Iterate over the rows in the table
for row in table.find_all("tr"):
    # Get the cells in the row
    cells = row.find_all("td")

    # Get the stock name
    stock_name = cells[0].find("a").text

    # Get the sector
    sector = cells[2].text

    # Check if the stock name matches the selected stock
    if stock_name == hisse:
        # Print the values
        st.write("Hisse Adı:", hisse)
        st.write("Sektör Alanı:", sector)

