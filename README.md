# Sentiment Analysis for News Articles
This project provides a comprehensive sentiment analysis of news articles concerning Lion Air. The primary goal is to evaluate public perception and media portrayal of the airline by systematically collecting and processing a dataset of news reports. Using NaturalLanguage Processing (NLP) techniques, this analysis automatically classifies articles as positive, negative, or neutral, offering insights into the prevailing opinions and tracking sentiment trends related to the airline's operations, incidents, and public relations.
<br><img src="image/image.jpg" width="1024" height="512"><br>
## 🗒️ Paper Information
Title | Author | Date
---|---|---
Analisis Sentimen untuk Artikel Berita : Studi Kasus Lion Air | Ahmad Fadhino Tegar Permana, Nur Ghulam Musthafa Al Kautsar, Dafa Fawwaz Alfarisi | ??/??/????

## 📂 Project Structure
```bash
sentiment-analysis-Lion-Air/
├── notebook
│   ├── 1_Articles_preprocessing.ipynb
│   ├── 2_Articles_EDA.ipynb
│   ├── 3_Articles_Sentiment_Analysis.ipynb
│   ├── 4_Articles_POS_NER.ipynb
│   └── data
│       ├── articles_raw.csv
│       └── cleaned_article.csv
└── scrapping_script
    └── main.py
```

## 🎯 Research Objective
The primary aim of this research is to comprehensively analyze the sentiment and thematic content of online news articles related to Lion Air.
<br>
To achieve this, the following specific objectives have been established:
- **To analyze and quantify public sentiment** towards Lion Air as reflected in online news articles, classifying each article as positive, negative, or neutral using the TextBlob library.
- **To compile a diverse dataset** by systematically scraping over 150 news articles concerning Lion Air from various online media sources.
- **To perform Exploratory Data Analysis (EDA),** generating visualizations to provide a clear understanding of sentiment distribution, key topics, and temporal trends.
- **To identify and group underlying themes** within the news corpus by applying unsupervised clustering algorithms, specifically DBSCAN, K-Means, and Agglomerative Clustering, using both Bag-of-Words (BoW) and TF-IDF feature extraction methods.
- **To conduct a detailed linguistic analysis** of the articles, employing Part-of-Speech (POS) tagging and Named Entity Recognition (NER) to extract key entities (such as people, organizations, and locations) and understand the grammatical context driving the sentiment.

## 📊 Dataset Features

## 🪜 Methodology

## 💡 Key Insights

## ✅ Conclusion