import streamlit as st

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html= True)

st.sidebar.image("https://img.freepik.com/free-vector/buy-sell-concept-design-showing-bull-bear_1017-13716.jpg?w=2000")

st.title("ABOUT US")

st.subheader("Created By")

st.write("__👉👉 Hanif Jamadar","__👉👉 Omkar Take","__👉👉 Somesh Thombare")
st.write("__👉👉 Komal Birajadar","__👉👉 Muskan Jamadar")

st.subheader("Contact Us")
st.write("__👉👉 Mob No. 8485037484","__👉👉Mob No. 7248971847")
st.write("__👉👉Mob No. 8485830316","__👉👉Mob No. 8080837830")
st.write("__👉👉Mob No. 9422707674")

st.subheader("You can contact us through Email")
st.write("jamadarmhanif77@gmail.com")
st.write("omkartake97@gmail.com")
st.write("someshthombre199@gmail.com")
