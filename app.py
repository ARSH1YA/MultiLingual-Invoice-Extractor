from dotenv import load_dotenv
import streamlit as st
import os 
from PIL import Image
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure Google Generative AI with a new model
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-flash')  # Updated model

# Function to get the response from Gemini
def get_gemini_response(input, image, prompt):
    response = model.generate_content([input, image[0], prompt])
    return response.text

# Function to handle uploaded image
def input_image_details(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_parts = [
            {
                "mime_type": uploaded_file.type,     # Get the mime type of the uploaded file
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")

# Initialize Streamlit app
st.set_page_config(page_title="MultiLingual Invoice Extractor")

# Apply custom CSS for glassmorphism
st.markdown(
    """
    <style>
    .glassmorphism {
        backdrop-filter: blur(10px);
        background: rgba(255, 255, 255, 0.2);
        border-radius: 15px;
        border: 1px solid rgba(255, 255, 255, 0.18);
        padding: 2rem;
        box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
    }
    .main {
        background-color: rgba(0, 0, 0, 0.2);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Define input and layout
st.markdown('<div class="glassmorphism">', unsafe_allow_html=True)
st.header("MultiLingual Invoice Extractor")

input = st.text_input("Input Prompt: ", key="input")
uploaded_file = st.file_uploader("Choose an image of the invoice...", type=["jpg", "jpeg", "png"])

image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

submit = st.button("Tell me about the invoice")

# Input prompt
input_prompt = """
You are an expert in understanding invoices. We will upload an image as an invoice and you will have to answer any questions based on the uploaded invoice image.
"""

# Submit button action
if submit:
    image_data = input_image_details(uploaded_file)
    response = get_gemini_response(input_prompt, image_data, input)
    st.subheader("The Response is")
    st.write(response)

st.markdown('</div>', unsafe_allow_html=True)






