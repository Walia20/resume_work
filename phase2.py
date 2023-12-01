import os
import pandas as pd
import streamlit as st
from phase3 import project_desc
import json

sess= st.session_state

if "project_show" not in sess:
    sess["project_show"]=False

def change_showcase():
    sess["project_show"]=not sess["project_show"]


def project_card(num, dict_projs):
    cur_card= dict_projs[f"val{num+1}"]
    st.markdown(f"<h5>Project #{num+1}</h5>", unsafe_allow_html=True)
    st.markdown(f"<h4>{cur_card['title']}</h4>", unsafe_allow_html=True)
    st.write(f"**Tech Stack**: {cur_card['tech_stack']}")
    _,co,__= st.columns([0.3,1,0.4])
    with co:
        st.image(cur_card["img_desc"], width=130)
    _,co,__= st.columns([0.4,1,0.4])
    with co:
        st.link_button("Check It 👉", cur_card["link"])

def show_projects():
    with open("project_case.json") as file:
        dict_projs= json.load(file)
    for num,i in enumerate(st.columns(3)):
        with i:
            project_card(num, dict_projs)


def real_projects():
    col1, col2 = st.columns(2)
    with col1:
        st.header("Project Showcase")
    with col2:
        st.write("")
        if sess["project_show"]==False:
            st.button("Show Desc", on_click= change_showcase)
        else:
            st.button("Close Desc", on_click= change_showcase)
    st.write("\n")
    if sess["project_show"]==False:
        show_projects()
    else:
        project_desc()
