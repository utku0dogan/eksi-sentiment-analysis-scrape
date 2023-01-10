import streamlit as st
from bs4 import BeautifulSoup
import requests
import re
from datetime import datetime
import csv
import pandas as pd 
from scrape import scrape
from data import *
from sentiment import *

def app():

    st.title(""" 

    **Ekşi Sözlük Duygu Analizi Uygulaması**                                      

    """)

    entries_dic = []

    with st.form("my_form"):
            
            URL = st.text_input(label= "analiz edilmesini istediğiniz başlığın linkini giriniz.")
            # Every form must have a submit button.
            try:
                submitted = st.form_submit_button("Submit")
                if submitted:
                    with st.spinner("veriler çekiliyor, lütfen bekleyin. bu biraz zaman alabilir."):
                        entries_dic, runtime = scrape(URL)
                        st.write("Çekilen entry sayisi: ", len(entries_dic))
                        st.write("Geçen süre: ", runtime)
            except:
                st.write("lütfen, geçerli bir link giriniz. Ör -> https://eksisozluk.com/eksi--60755?p=1")

    veri_cont = st.container()
    
    with veri_cont:
        
        if entries_dic:
            st.subheader("Örnek İlk 5 Girdi")
            df = datadf(entries_dic)        
            st.write(df.head())
            st.subheader("En Çok Girdi Girilen 10 Tarih")
            st.plotly_chart(plotly(df))
            st.subheader("Girdi Sayısına Göre Zaman Çizelgesi")
            st.pyplot(linechart(df))
            st.subheader("Duygu Analizine Göre Pozitif Negatif Girdi Sayısı")
            st.pyplot(sentimentchart(sentiment(df.Entry.to_list())))
            st.subheader("Duygu Analizine Göre Girdiler Hangi Duyguya Ait")
            st.pyplot(emotionchart(emotion(df.Entry.to_list())))            
            
        

   

if __name__ == "__main__":
	app()







