import os
import google.generativeai as genai
import pandas as pd
from contextlib import redirect_stdout
from io import StringIO
import streamlit as st
import numpy as np
from dotenv import load_dotenv
    
def my_function(data):
  """This function performs some action on the provided data.

  Args:
      data: Any data type that the function can process.

  Returns:
      The processed data or None if the function doesn't return anything.
  """
  # Implement your function logic here
  processed_data = data * 2  # Example: Double the input data
  return processed_data

# Load Google API key from .env file
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Gemini Pro model
model = genai.GenerativeModel("gemini-pro")

def get_gemini(Question):
    # Assuming model.generate_content is a function that generates a response based on the input question
    response = model.generate_content(Question)
    return f"{response.text}"

# Streamlit App
st.title("Gemini Pro Generator")

# File Upload
uploaded_file = st.file_uploader("Upload CSV/Excel file", type=["csv", "xlsx"])
print(uploaded_file)
if uploaded_file is not None:
    # # Check if the file exists
    # if not os.path.isfile(uploaded_file.name):
    #     st.error(f"Error: File '{uploaded_file.name}' does not exist.")
    #     st.stop()

    # Read uploaded file into a DataFrame
    df = pd.read_csv(uploaded_file)

    # Display top 10 rows of the DataFrame
    st.subheader("Top 10 Rows of the DataFrame:")
    st.write(df.head(10))

# User Input
    variable = st.text_input("Enter the prompt:")

    # Generate Question based on user input and DataFrame
    question = f"Use the dataframe with name df with columns {df.columns} and generate python code for " + variable

    # Generate response using Gemini Pro
    response = get_gemini(question)

    start_index1 = response.find('#')
    start_index2 = response.rfind(')')
    exec_code = response[start_index1:start_index2 + 1]

    with StringIO() as output_buffer:
        with redirect_stdout(output_buffer):
            exec(exec_code)
        captured_output = output_buffer.getvalue()
    st.subheader("Captured Output:")
    st.code(captured_output, language='python')


