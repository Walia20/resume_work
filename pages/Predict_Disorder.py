import requests
import plotly.graph_objects as go
import streamlit as st
sess= st.session_state

if 'values_taken' not in sess:
    sess["values_taken"]=False


API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-mnli"
headers = {"Authorization": "Bearer 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"}
main_example_prompt=  "John noticed that his hands would shake slightly, especially when he was resting or feeling relaxed. He also found it increasingly difficult to move smoothly and quickly, feeling like his body was slowing down. Sometimes, he would struggle to maintain his balance and would feel stiff and achy. These symptoms made simple tasks like writing and walking more challenging for him"


# Here the prompt is taken as >
# candidate_labels > choose from the given below
#st.subheader("APP #2")
st.title("Predict the Disorder based on Symptoms")
st.subheader("Description")
st.write("Here we are using zero shot classification to predict the Disorder any person might be suffering based on the symptoms they are noticing in theier daily life")
# Define your input parameters
def get_file_data():
    with open('pages/disorders.txt') as file:
        fil= file.read()
    main_list= [i.strip() for i in fil.split("\n")]
    return main_list


prompt = st.text_area("Enter the Symptoms you've noticed in a Person", value=main_example_prompt)
if prompt:
    pass
else: prompt = main_example_prompt

# Disorder you might think you have
# Here the candidate labels are fixed

def select_options():
    options = get_file_data()
    selected_options = st.multiselect("Select the Disorder You think you might have :", options, [], key="options")

    if len(selected_options) > 5:
        st.warning("Please select a maximum of 5 options.")
        selected_options = selected_options[:5]

    return selected_options


candidate_labels= select_options()




if len(candidate_labels) >= 2 and prompt !="":
    sess["values_taken"]=True
else:
    st.error("Please choose 2 or more values ")
    sess["values_taken"]=False



def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()

def get_query(prompt, candidate_labels):
    output = query({
        "inputs": prompt,
        "parameters": {"candidate_labels": candidate_labels},
    })
    return output

def get_results(prompt, candidate_labels):
    result= get_query(prompt, candidate_labels)

    # Get the predicted label and confidence score
    predicted_label = result["labels"][0]
    confidence_scores = result["scores"]

    # Create the horizontal bar plot using Plotly
    fig = go.Figure(go.Bar(
        y=candidate_labels,
        x=confidence_scores,
        orientation='h',
    ))

    fig.update_layout(
        title="Prediction Confidence",
        xaxis_title="Confidence Score",
        yaxis_title="Labels",
    )

    # Display the plot using Streamlit
    st.plotly_chart(fig)

if sess["values_taken"]==True:
    get_results(prompt, candidate_labels)
