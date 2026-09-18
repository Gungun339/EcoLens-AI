import streamlit as st
from google import genai

st.set_page_config(page_title="EcoLens AI", page_icon="🌱", layout="centered")

st.title("🌱 EcoLens AI - Carbon Footprint Assistant")
st.write("Calculate your daily carbon emissions and get eco-friendly recommendations!")

st.sidebar.header("Configuration")
api_key = st.sidebar.text_input("Enter Gemini API Key", type="password")

user_activity = st.text_area(
    "Describe your daily activity:",
    placeholder="e.g., I commuted 15 km by petrol scooter and ate a meat-based lunch."
)

if st.button("Analyze Footprint"):
    if not api_key:
        st.error("Please enter your Gemini API key in the sidebar!")
    elif not user_activity:
        st.warning("Please enter an activity to analyze.")
    else:
        try:
            client = genai.Client(api_key=api_key)
            
            prompt = f"""
            You are EcoLens AI, a carbon footprint assistant. 
            Analyze the following user activity and provide a response in clear structured sections:
            1. Estimated Carbon Footprint (in kg CO2)
            2. Actionable Eco-Swap Recommendation
            3. Daily Sustainability Tip

            User Activity: {user_activity}
            """
            
            with st.spinner("Analyzing footprint..."):
                response = client.models.generate_content(
                    model='gemini-3.6-flash',
                    contents=prompt
                )
                
                st.success("Analysis Complete!")
                st.subheader("Results")
                st.write(response.text)
                
        except Exception as e:
            st.error(f"An error occurred: {e}")
