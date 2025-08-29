# health_gemini_app.py
import streamlit as st
import os
import google.generativeai as genai
from dotenv import load_dotenv
import datetime

# Load environment variables
load_dotenv()

# Configure Google Gemini
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

# Set page config
st.set_page_config(
    page_title="Google Health Assistant",
    page_icon="🌿",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #4285F4; /* Google blue */
        text-align: center;
        margin-bottom: 1rem;
    }
    .google-button {
        background-color: #4285F4;
        color: white;
        border: none;
        padding: 15px 30px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 18px;
        margin: 10px 5px;
        cursor: pointer;
        border-radius: 8px;
        font-weight: bold;
        width: 250px;
    }
    .google-button:hover {
        background-color: #3367D6;
    }
    .button-container {
        display: flex;
        justify-content: center;
        gap: 20px;
        margin: 2rem 0;
    }
    .result-box {
        background-color: #f8f9fa;
        border-left: 5px solid #4285F4;
        padding: 2rem;
        border-radius: 10px;
        margin: 1rem 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .warning-box {
        background-color: #fef7e0;
        border-left: 5px solid #f4b400; /* Google yellow */
        padding: 1rem;
        border-radius: 5px;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

def get_gemini_response(prompt):
    """Get response from Google Gemini"""
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

def analyze_health_with_gemini():
    """Health analysis using Google Gemini"""
    prompt = f"""
    You are a helpful health assistant. The user wants general health analysis and recommendations.

    Provide:
    1. Comprehensive health assessment based on current best practices
    2. Lifestyle recommendations (sleep, exercise, stress management)
    3. Nutritional guidance
    4. Preventive health measures
    5. When to consult healthcare professionals

    Format the response in clear sections with emojis.
    Include practical, actionable advice.

    IMPORTANT: Always state that this is not medical advice and to consult healthcare providers.
    """
    return get_gemini_response(prompt)

def generate_meal_plan_with_gemini(duration="5 days", health_condition="general wellness"):
    """Generate meal plan using Google Gemini"""
    prompt = f"""
    Create a detailed {duration} meal plan for {health_condition}.

    Include:
    - Breakfast, Lunch, Dinner for each day
    - Two healthy snacks per day
    - Nutritional information and benefits
    - Shopping list suggestions
    - Preparation tips
    - Calorie range (if appropriate)
    - Hydration recommendations

    Make it practical, diverse, and delicious.
    Use common ingredients that are easy to find.

    For {health_condition}, focus on appropriate nutritional needs.

    Format with clear daily sections and use food emojis.

    DISCLAIMER: This is general nutritional advice, not medical prescription.
    """
    return get_gemini_response(prompt)

def get_health_tips_with_gemini():
    """Get general health tips using Google Gemini"""
    prompt = """
    Provide comprehensive health and wellness tips covering:

    1. Nutrition and Diet 🍎
    2. Physical Activity 🏃‍♂️
    3. Mental Health 🧠
    4. Sleep Hygiene 😴
    5. Preventive Care 🛡️
    6. Healthy Habits 📋

    For each category, provide 5-7 practical, evidence-based tips.
    Use emojis and make it engaging but professional.
    Include both immediate actions and long-term habits.

    Keep the tone encouraging and motivational.
    """
    return get_gemini_response(prompt)

def main():
    """Main Streamlit app"""
    
    # Header
    st.markdown('<h1 class="main-header">🌿 Google Health Assistant</h1>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center; font-size: 1.2rem; color: #666;">Powered by Google Gemini AI</p>', unsafe_allow_html=True)
    
    # Warning disclaimer
    st.markdown("""
    <div class="warning-box">
    ⚠️ <strong>Medical Disclaimer:</strong> This app provides general health information only. 
    It is not medical advice. Always consult qualified healthcare professionals for 
    medical concerns, diagnoses, and treatment.
    </div>
    """, unsafe_allow_html=True)

    # Three Main Buttons
    st.markdown('<div class="button-container">', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        health_btn = st.button("🏥 Health Analysis", key="health", use_container_width=True, 
                              help="Get comprehensive health assessment and recommendations")
    
    with col2:
        meal_btn = st.button("🍽️ Meal Plan", key="meal", use_container_width=True,
                            help="Generate personalized meal plans")
    
    with col3:
        tips_btn = st.button("💡 Health Tips", key="tips", use_container_width=True,
                            help="Get general wellness advice")
    
    st.markdown('</div>', unsafe_allow_html=True)

    # Meal Plan Options (only show if meal button might be clicked)
    if st.session_state.get('show_meal_options', False) or meal_btn:
        st.session_state.show_meal_options = True
        
        st.markdown("---")
        st.subheader("🍽️ Meal Plan Options")
        
        col1, col2 = st.columns(2)
        
        with col1:
            duration = st.selectbox(
                "Plan Duration:",
                ["3 days", "5 days", "7 days", "14 days"],
                key="duration"
            )
            
        with col2:
            health_condition = st.selectbox(
                "Health Focus:",
                [
                    "General Wellness", "Weight Management", "Heart Health",
                    "Diabetes Management", "Gut Health", "Energy Boost",
                    "Immune Support", "Muscle Building", "Anti-Inflammatory"
                ],
                key="condition"
            )
        
        generate_meal = st.button("Generate My Meal Plan", type="primary", key="generate_meal")

    # Handle button clicks
    if health_btn:
        with st.spinner("🔍 Analyzing health with Google Gemini..."):
            result = analyze_health_with_gemini()
            st.markdown("### 🏥 Your Health Analysis")
            st.markdown('<div class="result-box">', unsafe_allow_html=True)
            st.markdown(result)
            st.markdown('</div>', unsafe_allow_html=True)

    elif meal_btn:
        st.session_state.show_meal_options = True
        st.rerun()

    elif tips_btn:
        with st.spinner("✨ Gathering health tips with Google Gemini..."):
            result = get_health_tips_with_gemini()
            st.markdown("### 💡 Health & Wellness Tips")
            st.markdown('<div class="result-box">', unsafe_allow_html=True)
            st.markdown(result)
            st.markdown('</div>', unsafe_allow_html=True)

    # Handle meal plan generation
    if st.session_state.get('show_meal_options', False) and 'generate_meal' in st.session_state:
        if st.session_state.generate_meal:
            with st.spinner("🍳 Creating your meal plan with Google Gemini..."):
                result = generate_meal_plan_with_gemini(
                    st.session_state.duration, 
                    st.session_state.condition
                )
                st.markdown(f"### 🍽️ {st.session_state.duration} Meal Plan for {st.session_state.condition}")
                st.markdown('<div class="result-box">', unsafe_allow_html=True)
                st.markdown(result)
                st.markdown('</div>', unsafe_allow_html=True)
                
                # Download button
                st.download_button(
                    label="📥 Download Meal Plan",
                    data=result,
                    file_name=f"google_meal_plan_{datetime.date.today()}.txt",
                    mime="text/plain",
                    key="download_meal"
                )

    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #666; margin-top: 3rem;">
        <p>Powered by Google Gemini AI • Not a substitute for professional medical advice</p>
        <p>Always consult healthcare providers for medical concerns</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()