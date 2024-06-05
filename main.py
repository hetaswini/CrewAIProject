import pandas as pd
import streamlit as st

#from crew import get_geminiresponse
from crew import get_geminiresponse


# Title and file upload
st.title("Select Record for Crew Function")
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # Display dataframe
    st.dataframe(df)

    # Select record
    selected_value = st.selectbox("Select a record", df["statement"].unique().tolist())

    # Pass to crew function
    if st.button("Pass to Crew Function"):
      #crew(selected_row.to_dict())
      
      ## starting the task execution process wiht enhanced feedback
      #result=get_geminiresponse(selected_value)
      st.write(selected_value)