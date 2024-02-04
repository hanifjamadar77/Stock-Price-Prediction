import pandas as pd
import pandas_datareader as dr
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np
import yfinance as yfin
from keras.models import load_model
import streamlit as st
yfin.pdr_override()

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html= True)

st.sidebar.image("https://img.freepik.com/free-vector/buy-sell-concept-design-showing-bull-bear_1017-13716.jpg?w=2000")

st.title("Stock Trend Prediction")
ticker = st.text_input("Ticker",'AAPL')
start_date = st.text_input('Start Date','2015-01-01')
end_date = st.text_input('End Date','2022-03-25')

df = dr.data.get_data_yahoo(ticker, start=start_date, end= end_date)

# user_input = st.text_input("Enter Stock Ticker",'AAPL')
# df = dr.data.get_data_yahoo(user_input, start="2011-01-01", end= "2022-3-25")
# # df.tail()

# Describing Data
st.header('Data Set')
st.write(df.describe())

open , close, low , high,chat = st.tabs(["Opening Price","Closing Price ","Low Price","High Price","ChatGPT"])

with open:
     # visvalizations
    st.header('Opening Price vs Time chart')
    fig = plt.figure(figsize = (8,4))
    plt.plot(df.Open)
    plt.xlabel('Time')
    plt.ylabel('Price')
    st.plotly_chart(fig)


    st.header('Opening Price vs Time chart with 100MA and 200MA')
    ma100 = df.Open.rolling(100).mean()
    fig3 = plt.figure(figsize = (8,4))
    plt.plot(ma100)
    plt.plot(df.Open)
    plt.xlabel('Time')
    plt.ylabel('Price')
    st.plotly_chart(fig3)

    st.header('Opening Price vs Time chart with 200MA')
    ma100 = df.Open.rolling(100).mean()
    ma200 = df.Open.rolling(200).mean()
    fig4 = plt.figure(figsize = (8,4))
    plt.plot(ma100)
    plt.plot(ma200)
    plt.plot(df.Open)
    plt.xlabel('Time')
    plt.ylabel('Price')
    st.plotly_chart(fig4)

    # Spliting Data into Training and Testing

    data_training = pd.DataFrame(df['Open'][0:int(len(df)*0.70)])
    data_testing = pd.DataFrame(df['Open'][int(len(df)*0.70):int(len(df))])

    from sklearn.preprocessing import MinMaxScaler
    scaler = MinMaxScaler(feature_range=(0,1))

    data_training_array = scaler.fit_transform(data_training)

    # load my model
    model = load_model('keras_model.h5')

    # Testing part
    past_100_days = data_training.tail(100)
    final_df = past_100_days.append(data_testing, ignore_index = True)
    input_data = scaler.fit_transform(final_df)

    x_test = []
    y_test = []

    for i in range(100, input_data.shape[0]):
        x_test.append(input_data[i-100: i])
        y_test.append(input_data[i, 0])

    x_test, y_test = np.array(x_test), np.array(y_test)
    y_predicted = model.predict(x_test)
    scaler = scaler.scale_

    scale_factor = 1/scaler[0]
    y_predicted = y_predicted * scale_factor
    y_test = y_test * scale_factor

    # Final Graph
    st.header('Prediction vs Original')
    fig2 = plt.figure(figsize= (8,4))
    plt.plot(y_test, 'b',label = 'Original Price')
    plt.plot(y_predicted, 'r', label = 'Predicted Price')
    plt.xlabel('Time')
    plt.ylabel('Price')
    plt.legend()
    st.plotly_chart(fig2)


with close:
    # visvalizations
    st.header('Closing Price vs Time chart')
    fig = plt.figure(figsize = (8,4))
    plt.plot(df.Close)
    plt.xlabel('Time')
    plt.ylabel('Price')
    st.plotly_chart(fig)


    st.header('Closing Price vs Time chart with 100MA and 200MA')
    ma100 = df.Close.rolling(100).mean()
    fig3 = plt.figure(figsize = (8,4))
    plt.plot(ma100)
    plt.plot(df.Close)
    plt.xlabel('Time')
    plt.ylabel('Price')
    st.plotly_chart(fig3)

    st.header('Closing Price vs Time chart with 200MA')
    ma100 = df.Close.rolling(100).mean()
    ma200 = df.Close.rolling(200).mean()
    fig4 = plt.figure(figsize = (8,4))
    plt.plot(ma100)
    plt.plot(ma200)
    plt.plot(df.Close)
    plt.xlabel('Time')
    plt.ylabel('Price')
    st.plotly_chart(fig4)

    # Spliting Data into Training and Testing

    data_training = pd.DataFrame(df['Close'][0:int(len(df)*0.70)])
    data_testing = pd.DataFrame(df['Close'][int(len(df)*0.70):int(len(df))])

    from sklearn.preprocessing import MinMaxScaler
    scaler = MinMaxScaler(feature_range=(0,1))

    data_training_array = scaler.fit_transform(data_training)

    # load my model
    model = load_model('keras_model.h5')

    # Testing part
    past_100_days = data_training.tail(100)
    final_df = past_100_days.append(data_testing, ignore_index = True)
    input_data = scaler.fit_transform(final_df)

    x_test = []
    y_test = []

    for i in range(100, input_data.shape[0]):
        x_test.append(input_data[i-100: i])
        y_test.append(input_data[i, 0])

    x_test, y_test = np.array(x_test), np.array(y_test)
    y_predicted = model.predict(x_test)
    scaler = scaler.scale_

    scale_factor = 1/scaler[0]
    y_predicted = y_predicted * scale_factor
    y_test = y_test * scale_factor

    # Final Graph
    st.header('Prediction vs Original')
    fig2 = plt.figure(figsize= (8,4))
    plt.plot(y_test, 'b',label = 'Original Price')
    plt.plot(y_predicted, 'r', label = 'Predicted Price')
    plt.xlabel('Time')
    plt.ylabel('Price')
    plt.legend()
    st.plotly_chart(fig2)


with low :
     # visvalizations
    st.header('Lower Price vs Time chart')
    fig = plt.figure(figsize = (8,4))
    plt.plot(df.Low)
    plt.xlabel('Time')
    plt.ylabel('Price')
    st.plotly_chart(fig)


    st.header('Lower Price vs Time chart with 100MA and 200MA')
    ma100 = df.Low.rolling(100).mean()
    fig3 = plt.figure(figsize = (8,4))
    plt.plot(ma100)
    plt.plot(df.Low)
    plt.xlabel('Time')
    plt.ylabel('Price')
    st.plotly_chart(fig3)

    st.header('Lower Price vs Time chart with 200MA')
    ma100 = df.Low.rolling(100).mean()
    ma200 = df.Low.rolling(200).mean()
    fig4 = plt.figure(figsize = (8,4))
    plt.plot(ma100)
    plt.plot(ma200)
    plt.plot(df.Low)
    plt.xlabel('Time')
    plt.ylabel('Price')
    st.plotly_chart(fig4)

    # Spliting Data into Training and Testing

    data_training = pd.DataFrame(df['Low'][0:int(len(df)*0.70)])
    data_testing = pd.DataFrame(df['Low'][int(len(df)*0.70):int(len(df))])

    from sklearn.preprocessing import MinMaxScaler
    scaler = MinMaxScaler(feature_range=(0,1))

    data_training_array = scaler.fit_transform(data_training)

    # load my model
    model = load_model('keras_model.h5')

    # Testing part
    past_100_days = data_training.tail(100)
    final_df = past_100_days.append(data_testing, ignore_index = True)
    input_data = scaler.fit_transform(final_df)

    x_test = []
    y_test = []

    for i in range(100, input_data.shape[0]):
        x_test.append(input_data[i-100: i])
        y_test.append(input_data[i, 0])

    x_test, y_test = np.array(x_test), np.array(y_test)
    y_predicted = model.predict(x_test)
    scaler = scaler.scale_

    scale_factor = 1/scaler[0]
    y_predicted = y_predicted * scale_factor
    y_test = y_test * scale_factor

    # Final Graph
    st.header('Prediction vs Original')
    fig2 = plt.figure(figsize= (8,4))
    plt.plot(y_test, 'b',label = 'Original Price')
    plt.plot(y_predicted, 'r', label = 'Predicted Price')
    plt.xlabel('Time')
    plt.ylabel('Price')
    plt.legend()
    st.plotly_chart(fig2)


with high:
     # visvalizations
    st.header('Higher Price vs Time chart')
    fig = plt.figure(figsize = (8,4))
    plt.plot(df.High)
    plt.xlabel('Time')
    plt.ylabel('Price')
    st.plotly_chart(fig)


    st.header('Higher Price vs Time chart with 100MA and 200MA')
    ma100 = df.High.rolling(100).mean()
    fig3 = plt.figure(figsize = (8,4))
    plt.plot(ma100)
    plt.plot(df.High)
    plt.xlabel('Time')
    plt.ylabel('Price')
    st.plotly_chart(fig3)

    st.header('Higher Price vs Time chart with 200MA')
    ma100 = df.High.rolling(100).mean()
    ma200 = df.High.rolling(200).mean()
    fig4 = plt.figure(figsize = (8,4))
    plt.plot(ma100)
    plt.plot(ma200)
    plt.plot(df.High)
    plt.xlabel('Time')
    plt.ylabel('Price')
    st.plotly_chart(fig4)

    # Spliting Data into Training and Testing

    data_training = pd.DataFrame(df['High'][0:int(len(df)*0.70)])
    data_testing = pd.DataFrame(df['High'][int(len(df)*0.70):int(len(df))])

    from sklearn.preprocessing import MinMaxScaler
    scaler = MinMaxScaler(feature_range=(0,1))

    data_training_array = scaler.fit_transform(data_training)

    # load my model
    model = load_model('keras_model.h5')

    # Testing part
    past_100_days = data_training.tail(100)
    final_df = past_100_days.append(data_testing, ignore_index = True)
    input_data = scaler.fit_transform(final_df)

    x_test = []
    y_test = []

    for i in range(100, input_data.shape[0]):
        x_test.append(input_data[i-100: i])
        y_test.append(input_data[i, 0])

    x_test, y_test = np.array(x_test), np.array(y_test)
    y_predicted = model.predict(x_test)
    scaler = scaler.scale_

    scale_factor = 1/scaler[0]
    y_predicted = y_predicted * scale_factor
    y_test = y_test * scale_factor

    # Final Graph
    st.header('Prediction vs Original')
    fig2 = plt.figure(figsize= (8,4))
    plt.plot(y_test, 'b',label = 'Original Price')
    plt.plot(y_predicted, 'r', label = 'Predicted Price')
    plt.xlabel('Time')
    plt.ylabel('Price')
    plt.legend()
    st.plotly_chart(fig2)

# from pyChatGPT import ChatGPT
# from selenium.webdriver import Chrome
# browser = Chrome(executable_path="/path/to/chromedriver.exe")
# session_token = 'eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..BdV6c1WJ0xFn56oY.jMzbNP47gZZIiz1t63WQwe1uwW1g2zgQ9rpOsU2i6lC5RJNentnLqB90ckgKjcW3YNCuSDJoRSlc83HfKOqDlEb0-DqAqJwXslFAOHOZityyuSPpfLeGXHu-K6BKN_6y8ad0N6B2k9WApB1oflNWQLybf7VPRdsHXWTn3qIzHIGqoWcoYWSNbkrr-HarF0IkW40SeG0aMKjmLVuxj9iGjwcULF4-3BCXlffmMjqVzNlhNiYnQiBqJb8_EktSiy07uRGM13cAT3gWP4suf7Jb5xwVh77M1cXs5cqR7B5Ero8oZn0tsIMksxgyPoREudZO2UuZTt2oU56JnPSZ7nizTKH8dCVWn0oDB0_ypVyZfiLYzyjD9mKdwTx0F38i60dI-qP5ifjRCrJ1Vro-3XniyYZlHQqmrevdR3woU-I-X4MBJ4LF2P-Tu31Gjqg29EFI1WTb2XXsSEwTCZk8imHTar-98ibltmDbaDcRi3ZQgTujIvgGh-_a9eAy4lL01juhPVm-igzJJEA0beHNJSpYRSR9tAOIJTVOfbGivGWDT7HxrQ5H8cHP3QRAghGaAg44re_ew7YG_KU6rSVtnrRWQDXjXcY9CD29y0-s_N_2px-18XviHbALntyoZ2hqMWo-NINdNw78PuBV3u4VkKfU8etSwi_HzKGekFZCDLhs_eRXuWIIcTw4Jk2mXZY9XyfaGaTEJc2jHf_g6SUKjAvvvdu2M8lLIjt6otX-ablRiB-cChXXTyzypYZTzoGq1fYqos3u_5KZyl2qFz7CefMYID_9FpB6C7y-f6ePb_5VefErCgBNikShbBXLb8_gF0c9WlYYTGmwDK_QI-rH-gN70-2pXGDEQjqm78_55vDq7MKl8-J4OcbSdgRS884ZdyBycS7rxWSj1RK7RQ80ZuXLB0c_BeMfjC-Wq7pwDpKynMeyjvYLDvtLZLZR7FOVVOCNdikCKDIUq5B8OBtozx0Pn_QdFzGePYUL_XmhcFLxZW2OBGtXms2iEfwJbDdpYcSEfN72fm7b1dUVGCSqlQilNAr5DIx_aNp2Y5eVdpEOhtbSUfBi4JXpfxzGHpTDWpVTHEANVC6F5wmvlokgCATIRCN9DkYHiyBcLL2diYMygiyM86X0AHvItW9OPW_bC2lOHA29NTxHMrMT2jtZmndMAi0wvQvfmIKyePzw4oUCIuBke_X3cscxZJ9hyV2b9hk3ffXZFQEhGivxk45w3McSAezjFqWM_cQkbXFqj1n7hf9oVilGlkJigvjeMKLIUHPTec1GZOWNZc_eQyVC5SWcp3zafvCldXWOrFg87fdZg4X_UZ875eGu2dCVwBpmK9IuK8Q3MaM7qEsQXjQ-a-zpleyGr8xIZYFj2sm3Jxo5Txvp9XI4lD2Fm_YKTDrMM3swlySxCCwLasGPK7EljzUJeGCm0jg0Ieg4-xE8REKGUcY0vd9EQYr3Cj7brw8qYbaUgIaQW7Zc3PMJ7gs449zFXbL5gY5DY1XObDw2Y71E8f_JiSsNy_K-AiQmIhNDcg-VoikZQEjF82TzcT28Md8atkrw79W4wdX3seFDZM-a_cLuC07Es48k5Sl6uDBeP7mYyGxbp9z_TnHYCoxmP5wmIAeUm4OCBNYGNhWB95lg0jjbk8tyrJsWccqGYxiwTTWPUdxhdfu_I2foWxWxhppqLPgkKR9ufM5YlZRIqp2KMxEo12KyA-80WFgyOunS1d5ZWF6vx8pvztFJyuCxLt7ngNJfPBAbToyL1KGf3GrHZiD_mvx-YE_zvabZVzUXfwH13D98YZipywSGgAyBZqlSPHkJnkhi2lhFl00rtd0zCdFvZ4QD0BG0jxrxAf-HVjCDC2gTJ41jzZzeAki3XJPyaLwwflDpbaZFNxAZ-00cwAZgzIn2N0p1vOvuOEUSTLLSK7wiFfPaTngF8yfWrZhFUPMsYt-9zvadX8HDtza6ZlXy1QR2mtwLQ4vJE_WV0WfvZDX_58rs_iylMfTOgQ1T-fxA9BII2L-VCEbbV_YF371gNvvj6RINqppimz-j36ZAc1Bw9QWiuQ_cftGbR7gF1lB6Hf3yzQCgzxqrXb0fVLajYbTeBoRMYDtpJFf4Q4nXisXBRvEDtsVK9cTfc4aAcWcEKdhNi4iQoecUFx41hfu47HzsvQZJkHPxaZcTp6ZAaxb1skXucOZSt8tUP3hcFyq5nCKMkBuXuT62p8fZaUAeaL5iWR37WOsoIfI80EXj4SVFpWOsqdt1chQXr7nZmHUMaaB5pspCjvqxH1o89gPp2joAxjLFQm6-BqYGqB3AZCjxiYmVMLuLbYMqp101PNk50GiJSyLsMJEmL72UKEcp4whasL5EceWfOupSXhHDgVJdtBXWMU-HSqiuFBZMtfgHAUi_xOtH4-mqW5972EtI390ZrXkIkDr3XYoX0t_RyhdzY_kKxUpflB2kvSZk0P8F36q8aE_-WxCzxaMRgfAwqRN9eDI8HMxEsrdXThbHVi0xRkhWa-sIouQJyDTN6E97OOU3uxw8awbB-UrmKeJg16EBCYYayKvUzspVO3ayp3VvDNQEkLgI9H__-e7rXxS7ETCypAPA-AzijEYOxd97FlebZ_k2YWyDcME6ONy724KezHtlqMYOXftzpWmvNlZwNQVdHsNrchctBI1I4mANi2OUucQTPhCK.kaY8M11Sp-UxH-0_Psg8Zw' 
# api2 = ChatGPT(session_token)
# buy = api2.send_message(f'3 Reasons to buy{ticker} stock')
# sell = api2.send_message(f'3 Reasons to sell{ticker} stock')
# swot = api2.send_message(f'SWOT analysis{ticker} stock')
    
# with chat:
#     st.title("Welcome to ChatGPT")
#     buy_reason,sell_reason,swot_analysis = st.tabs(['3 Reasons to buy','3 Reasons to sell','SWOT analysis'])

#     with buy_reason:
#         st.subheader(f'3 Reasons to buy{ticker} stock')
#         st.write(buy['message'])
    
#     with sell_reason:
#         st.subheader(f'3 Reasons to sell{ticker} stock')
#         st.write(sell['message'])

#     with swot_analysis:
#         st.subheader(f'SWOT analysis{ticker} stock')
#         st.write(swot['message'])


# with news:
#     from stocknews import StockNews
#     import nltk
#     nltk.download('vader_lexicon')
#     st.header (f'News of (ticker)')
#     sn= StockNews(ticker , save_news=False)
#     df_news = sn.read_rss()
#     for i in range(10):
#         st.subheader(f'News (i+1)')
#         st.write(df_news['Published'][i])
#         st.write(df_news['Title'][i])
#         st.write(df_news['Summary'][i])
#         title_sentiment = df_news['Sentiment_title'][i]
#         st.write(f'Title Sentiment {title_sentiment}')
#         news_sentiment = df_news['Sentiment_summary'][i]
#         st.write (f'News Sentiment {news_sentiment}')



