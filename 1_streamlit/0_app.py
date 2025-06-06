import streamlit as st
import pandas as pd
import time

# https://docs.streamlit.io/

st.title("i am title")
st.header("i am header")
st.subheader("i am sub header")

st.markdown("""
            ## i am markdown
            - i love movies
            - i love webseries
            """)

st.code(""" 
    def func():
        return 'i am a function' 
        """)

st.latex("x^2+y^2=4")

df=pd.DataFrame({"name":["pankaj","harry","pankaj"],
                 "f1":["nope","n",None],
                 "columns":["i","dont","know"]})

st.dataframe(df)

st.metric("Revenue","3L","3%")
st.metric("Revenue","3L","-3%")

st.json({"name":["pankaj","harry","pankaj"],
                 "f1":["nope","n",None],
                 "columns":["i","dont","know"]})

st.image("https://plus.unsplash.com/premium_photo-1710965560034-778eedc929ff?fm=jpg&q=60&w=3000&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8YmVhdXRpZnVsJTIwd29ybGR8ZW58MHx8MHx8fDA%3D")

st.video("https://www.youtube.com/watch?v=5mnitCrNQzI&t=606s")

st.sidebar.title("i am sidebar")
# all things above can be added to a sidebar

col1,col2=st.columns(2)

with col1:
    st.title("i am col1")

with col2:
    st.title("i am col2")

st.error("i am error mesage")
st.success("i am sucess mesage")
st.info("i am info mesage")
st.warning("i am warning mesage")

pb=st.progress(0)

for i in range(1,101):
    # time.sleep(0.1)
    pb.progress(i)

a=st.text_input("enter your email")
a=st.number_input("enter your age")
a=st.date_input("enter your date")
g=st.selectbox("select your gender",["M","f"])
btn=st.button("click me")

if btn:
    st.success("i am clicked")
    st.balloons()


file=st.file_uploader("upload a csv file")

if file:
    df=pd.read_csv(file)
    st.write(df.describe())