import streamlit as st
import os
import json


def create_set(json_text):
    col1, col2 = st.columns([4, 2])
    with col1:
        st.markdown(f"#### **🌟 {json_text['company_name']}**")
        st.markdown(f"##### 🎖️ {json_text['position']}")
    with col2:
        st.markdown("\n")
        st.markdown(f"###### {json_text['time_served']}")
        st.markdown(f"###### {json_text['working_place']}")
    st.write("\n\n")
    points = json_text["points"]
    for point in points:
        st.write("🔥 " + point)

    st.write("---")

def worked_out_experience():
    st.title('Work Experience')
    with open("work_exp.json") as text:
        list_json= json.loads(text.read())
    for i in list_json:
        create_set(i)
