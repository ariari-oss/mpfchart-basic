import streamlit as st
import mplfinance as mpf
import yfinance as yf



st.title("basic chart")

st.text("ティッカー、証券コードを入力してください\n" +
        "例）AAPL,7203.T,^N225,JPY=X,BTC-USD")
#ticker = st.text_input("ティッカーコード:",'^N225')
if st.checkbox("自分で銘柄を指定する", value=False):
    ticker = st.text_input("ティッカーコード:")
else:
    ticker = st.selectbox("ティッカーコード:",options=['^N225','AAPL','JPY=X','BTC-USD'], index=0)


st.write('&nbsp;')
show_dataset = st.checkbox('データ表示', False)
    
dsp_days = st.slider("表示日数（日）:",min_value=30,max_value=1000,value=100)   
st.markdown("---")


if ticker:
    ds = yf.download(ticker).tail(dsp_days)

    fig, ax = mpf.plot(ds,
                    title=ticker,
                    type="candle",
                    volume=True,
                    mav=[5,10,60],
                    figratio=[2,1],
                    style="yahoo",
                    returnfig=True
                    )
    

    st.pyplot(fig)
    st.markdown('---')
    if show_dataset:
        st.dataframe(ds)

