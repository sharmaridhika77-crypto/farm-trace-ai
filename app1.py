import streamlit as st
import streamlit as st
import google.generativeai as genai

# Naya Code: Secrets se key uthane ke liye
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
else:
    st.error("API Key nahi mili! Settings mein check karo.")

# Baaki ka aapka code waisa hi rahega
model = genai.GenerativeModel('gemini-1.5-flash')

st.title("🌱 Farm-Trace: AI Carbon Credit Helper")
st.write("Apne khet ki photo upload karein aur AI se analysis paayein.")

# 2. File Uploader
uploaded_file = st.file_uploader("Khet ki photo chuniye...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)
    
    if st.button('Analyze with AI'):
        # 3. Gemini Model Calling
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        with st.spinner('AI analysis kar raha hai...'):
            response = model.generate_content([
                "Analyze this farm image. 1. Identify crop type. 2. Detect health issues. 3. Estimate carbon sequestration potential. Give output in Hindi and English.", 
                image
            ])
            
            st.subheader("Results:")
            st.write(response.text)

st.divider()
st.info("Built with Google Gemini for Solution Challenge 2026")
