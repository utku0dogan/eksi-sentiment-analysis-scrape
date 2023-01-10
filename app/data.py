import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
from sentiment import * 
def datadf(entries_dict):
    entriesdf = pd.DataFrame.from_dict(entries_dict)
    return entriesdf


def plotly(df):
    #date_data = df.groupby(["Date"], as_index = False).count().sort_values(by=['Entry'],ascending=True)
    fig = px.scatter(
    df['Date'].value_counts()[:10],
)  
    return fig

def linechart(df):
    date_data = df.groupby(["Date"], as_index = False).count().sort_values(by=['Entry'],ascending=False)
    date_data.Date = pd.to_datetime(date_data.Date)
    date_data.set_index('Date', inplace=True)
    # fig = plt.plot(date_data['Entry'])
    # ticklabels = date_data.index.strftime('%Y-%m-%d')
    fig = plt.figure(figsize=(9,7))
    plt.grid(True)
    sns.lineplot(data = date_data)
    return fig


def sentimentchart(tahminler):
    sns.set_theme(style="whitegrid")
    fig = plt.figure(figsize=(9,7))
    sns.countplot(x=tahminler)
    return fig

def emotionchart(results):
    sns.set_theme(style="whitegrid")
    fig = plt.figure(figsize=(9,7))
    sns.countplot(x=results)
    return fig
    



