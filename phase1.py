import os
import pandas as pd
import streamlit as st

def show_link(link="", text=""):
    if link=="" and text=="":
        link= "https://www.linkedin.com/in/datawalia20/"
        text="🏆 LinkedIN"
    style="font-size: 24px; color: white; text-decoration: none; font-weight: bold;"
    return f"<h3><a href='{link}' style='{style}'>{text}</a></h3>"


def header_section():
    col1, col2 = st.columns([2,3], gap="small")
    with col1:
        st.image("imgs/face.png")
    with col2:
        st.header("Hi, I'm Gunpreet 👋")
        st.write("I'm an accomplished data scientist renowned for my expertise in Language Models, NLP, and adept handling of AWS technologies.")
        with open("Walia.pdf", "rb") as file:
            data= file.read()
        st.download_button("📄 Download Resume", data, "walia_resume.pdf")
        # st.markdown("")
        st.markdown('📨 <a href="mailto:itswalia20@gmail.com">itswalia20@gmail.com</a>', unsafe_allow_html=True)
    st.write("\n\n")
    col1,coln, col2,colm, col3= st.columns([2,1,2,0.5,3])
    with col1:
        st.markdown(f"{show_link()}", unsafe_allow_html=True)
    with col2:
        st.markdown(f"{show_link('https://github.com/Walia20','👨‍💻 Github')}", unsafe_allow_html=True)
    with col3:
        st.markdown(f"{show_link('','📞 +918860963457')}", unsafe_allow_html=True)
    st.write("---")
