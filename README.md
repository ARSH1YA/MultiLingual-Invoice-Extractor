# MultiLingual-Invoice-Extractor
This project is a web application built using Streamlit and Google Gemini AI (gemini-1.5-flash), which extracts and analyzes information from uploaded invoice images. The app allows users to upload invoices in various image formats and uses advanced AI to interpret the content, making it particularly useful for multilingual and complex invoices.

# Features
 - Invoice Upload: Users can upload invoice images in .jpg, .jpeg, or .png format.
 - AI-based Invoice Analysis: Utilizes Google's Gemini AI (gemini-1.5-flash) for 
  generating intelligent responses based on the uploaded invoice image and user-provided prompts.
 - Multilingual Support: The AI can handle invoices in different languages, making it 
  versatile for global use.
 - Glassmorphism UI: The app includes a visually appealing interface with a glassmorphism 
  design.

## Getting Started

# Prerequisites
Before you begin, ensure you have met the following requirements:
 - Python 3.8 or higher
 - Streamlit
 - Google Generative AI API access
 - .env file containing the GOOGLE_API_KEY for authentication with Google Gemini AI.

# Usage
1. Upload the invoice image.
2. Input any prompt or question related to the invoice.
3. Click "Tell me about the invoice" to see the AI's response.
For example, you could ask questions like:
 "What is the total amount?"
 "Who is the recipient of the invoice?"
 "What is the due date?"
The AI will process the invoice and provide a textual response based on your input.

# Key Functions:
- get_gemini_response(input, image, prompt): Sends the input, image data, and prompt to the Gemini model and returns the AI-generated response.
- input_image_details(uploaded_file): Prepares the image data for processing by the AI.

# Technologies Used
![Python]

# Known Issues and Limitations
- Model Dependency: The app relies on the Google Gemini AI model, which may have rate limits depending on the API key's usage plan.
- Image Quality: The quality and clarity of the uploaded invoice images may impact the accuracy of the AI's response.

# Future Enhancements
- Adding support for more image formats (e.g., PDF).
- Improving multilingual support for complex invoice formats.
- Exporting the extracted information as structured data (e.g., CSV, JSON).







