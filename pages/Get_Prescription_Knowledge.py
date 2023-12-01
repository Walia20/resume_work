import openai
from openai import OpenAI
import json
import pandas as pd
import numpy as np
import os
import time
import streamlit as st

sess= st.session_state
client = OpenAI(api_key= st.secrets["openai_api"])
# Set up your OpenAI API credentials
# prompt = "Once upon a time"

if "text_input" not in sess:
    sess["text_input"]= False
if "example" not in sess:
    sess["example"] = False
if "butn_press" not in sess:
    sess["butn_press"]=False


def provide_output(prompt):
    response = client.chat.completions.create(
      model="gpt-3.5-turbo-1106",
      response_format={ "type": "json_object" },
      messages=[
        {"role": "system", "content": """You are a Data Scientist having 3+ yrs experience in medical field and provide output in JSON format with following field:
             {
                 "medication":drug_name,
                 "value": value_asked
             }
         """},
        {"role": "user", "content": prompt},
      ]
    )
    dict_val = json.loads(response.choices[0].message.content)
    return dict_val


def description_prompt(name):
    desc=f"Explain the Question Briefly\n Give a Brief Description about the {name} for medicational purpose about what is it? and where it used ?\n"
    a=provide_output(desc)
    return a["value"]

def tell_doctor_prompt(name):
    tell_doc=f"Explain in brief \nWhile using the {name},  Tell your Doctor when you have : \n"
    a= provide_output(tell_doc)
    return a["value"]

def how_to_take(name):
    taking=f"Explain the Question Briefly\n How should you take the {name}, write down the steps below in point for consumption about the {name}\n"
    a= provide_output(taking)
    return a["value"]

def dosing(name):
    doses=f"Explain Briefly \n Write about the dosage using the drug {name}, write down the dosage for adults as well as children in point manner \n"
    a= provide_output(doses)
    return a["value"]


#st.subheader("APP #3")
st.title("Get Any Prescription Drug Knowledge")
st.write("This project call the drug name as input and uses transformers like bloom and t5 to predict specific information like when to take the drug or which people should consult doctor first.")

st.title('Drug Name')
text_input=st.text_input("Enter your Drug Name ", value="Cabometyx")
col1,col2= st.columns(2)


def predict_it():
    sess["butn_press"] =True

with col1:
    st.button("Find out", on_click=predict_it)

if sess["example"]!= False:
    text_input = sess["example"]
    sess["text_input"] = text_input

if text_input!="" and text_input!=" ":
    sess["text_input"]= text_input
else:
    sess["text_input"] = False
    sess["butn_press"]=False


def get_other_part(text_input):
    with st.spinner('Wait for it...'):
        call_desc= description_prompt(text_input)
        time.sleep(2)
    st.subheader(f"Description about the {text_input}")
    st.write(call_desc)

    with st.spinner('Wait for it...'):
        call_doc=  tell_doctor_prompt(text_input)
        time.sleep(3)
    st.subheader(f"Tell your Doctor When using {text_input}")
    st.write(call_doc)


    with st.spinner('Wait for it...'):
        how_take= how_to_take(text_input)
        time.sleep(3)
    st.subheader(f"How to take {text_input}")
    st.write(how_take)

    with st.spinner('Wait for it...'):
        dosage = dosing(text_input)
        time.sleep(3)
    st.subheader(f"Daily Dosage")
    st.write(dosage)


if sess['text_input']!=False and sess["butn_press"]==True:
    get_other_part(text_input)
