import streamlit as st
import mplfinance as mpf
import yfinance as yf



st.title("basic chart")
st.text("銘柄コードを入力してください。")
aa = st.text_input("","^N225")
ds = yf.download(aa).tail(100)


fig, ax = mpf.plot(ds,
                   title=aa,
                   type="candle",
                   volume=True,
                   mav=[5,10,60],
                   figratio=[2,1],
                   style="yahoo",


                   returnfig=True
                   )

#st.pyplot(fig)
st.dataframe(ds)

