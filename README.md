# EkşiSözlük Anlık Duygu Analizi Uygulaması
çalıştırmak için ->  `streamlit run app/app2.py`

## Projenin Amacı

Bu projenin amacı [www.eksisozluk.com](http://www.eksisozluk.com/) sitesinde “başlık” denen, o konu ile ilgili düşüncelerin yazıldığı alanlardan metinleri  anlık  olarak çekip bunun üzerinde sentiment analiz gerçekleştirdikten sonra bu analizin sonuçlarını bir arayüzde grafik gibi araçlarla göstermektir.

Bu analiz iki farklı çıktı verecektir. Bunlardan biri “olumlu, olumsuz”, diğeri girdinin hangi duyguyu yansıttığı olacak biçimde “korku, mutluluk, kızgınlık, üzgünlük, tiksinti, sürpriz” seçenekleridir. Olumlu/ olumsuz analizi kısmında derin öğrenme, altı farklı duygu analizinde ise çeşitli makine öğrenme yöntemleri denenerek en iyi sonucu veren seçenek projede kullanılmıştır.

## Aim of the project 
Eksisözlük, we can say that it is the oldest Forum site in Turkey. On this site, there are headings and comments called entries under that headings.
basically, you can find out users’ general opinions and emotions about a heading without reading all entries by entering a heading link in the input text box. Also, you can see graphs about a heading.
This app has two modules. One of these modules tries to predict whether the comment is positive or negative, and the other one tries to predict the emotion of the comment. 
Both are pre-trained using labeled datasets.

For the positive, negative prediction module I used Long Short-Term Memory (LSTM) which is a type of Recurrent Neural Network (RNN) that is specifically designed to handle sequential data.
For the emotion prediction module, I used various elementary machine learning algorithms and saved the most accurate algorithm. It was logistic regression. There are 6 labels (fear, happiness, surprise, anger, sadness, and disgust) in the dataset used for the train. For example, the module predicts fear, surprise and anger as the dominant emotion for the Istanbul earthquake heading.

## Kullanılan Teknolojiler
* Python
* Beautiful Soup
* Keras
* Streamlit
* Visual Studio Code
* Jupyter Notebook
* Seaborn
* Sci-kit Learn
* Matplotlib

## Projenin Çalışma Mantığı

![image](https://user-images.githubusercontent.com/59983461/211626243-adfc37cb-a4b2-4133-8520-068bb0990807.png)


## Ekran görüntüleri 

![ss](https://user-images.githubusercontent.com/59983461/211617651-f5e4e1f1-339d-4591-85fe-c2f12115b790.png)

![ankara_batikentte_kopek_katliami](https://user-images.githubusercontent.com/59983461/211617717-a53b5f7f-8d17-4356-8dbb-bfc2bcaf12ec.png)

![istanbul depremi](https://user-images.githubusercontent.com/59983461/211617824-cdfd628a-4ca3-4584-9391-8d772bbf9f60.png)

![grafik](https://user-images.githubusercontent.com/59983461/211617912-b01a39a6-af4b-4457-bba1-f5c3934785fb.png)




