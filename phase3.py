import streamlit as st
import os
import json

def show_skills():
    st.write("#")
    st.header("Technical Skills")
    st.write("""\r\t✅**Backend Tech**: Python, Flask/Django/FastAPI, EC2, S3, Route53 , Lambda, REST API
    \n✅**AI-ML**: NLP, Data Science, Deep Learning, LLM, Generative AI, Transformers, Reinforcement Learning(RL)
    \n✅**Data Pipelines** : SQL, DataBricks, PySpark, Redshift, GLUE, ETL, Redis, Airflow
    \n✅**Cloud Tech** : Amazon Web Services(AWS), GCP, Azure
    \n✅**Devops** : Git, CI/CD, Docker, Kubernetes, EKS, ECS
    \n✅**ML Platform** : Tensorflow, Pytorch, NLTK, SpaCy, Sagemaker, scikit-learn, HuggingFace""")


def project_desc():
    st.write("\n")
    # st.header("Project Description")
    with open("projects.json") as file:
        valk=json.loads(file.read())
    for en,i in enumerate(valk):
        title=valk[i]["title"]
        link= valk[i]["link"]
        col1, col2 = st.columns([1,6])
        with col1:
            st.markdown(f"##### Project #{en+1}")
        with col2:
            st.markdown(f"##### [{title}]({link})")
        projects= valk[i]["project_desc"]
        for j in projects:
            st.write(f"🔥 {j}")
