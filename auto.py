import streamlit as st
import webbrowser
import random

# Page configuration
st.set_page_config(
    page_title="Automation by Sarim",
    page_icon="🌐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
st.markdown(
    """
    <style>
    .stApp {
        background-color: #1e1e1e;
        color: white;
    }
    .stButton>button {
        background: linear-gradient(45deg, #4CAF50, #2E8B57);
        color: white;
        border-radius: 8px;
        padding: 10px 24px;
        transition: all 0.3s;
        width: 100%;
        border: none;
        font-weight: bold;
    }
    .stButton>button:hover {
        transform: scale(1.02);
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
    .restart-button {
        background: linear-gradient(45deg, #FF4B4B, #F9AB00) !important;
    }
    .new-word-button {
        background: linear-gradient(45deg, #2196F3, #21CBF3) !important;
    }
    .stTextInput>div>div>input {
        background-color: #2d2d2d;
        color: white;
        border-radius: 5px;
    }
    .stTextArea>div>div>textarea {
        background-color: #2d2d2d;
        color: white;
        border-radius: 5px;
    }
    .header-text {
        font-size: 2.5rem;
        background: linear-gradient(90deg, #FF4B4B, #F9AB00);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 2rem;
        font-weight: bold;
    }
    .platform-card {
        background-color: #2d2d2d;
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 15px;
        border-left: 4px solid #4CAF50;
    }
    .tab-container {
        background-color: #2d2d2d;
        border-radius: 10px;
        padding: 20px;
        margin-top: 15px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Header
st.markdown('<h1 class="header-text">🌐 Automation by Sarim</h1>', unsafe_allow_html=True)
st.markdown("### Web Search Automation Tool")

# Create tabs for better organization
tab1, tab2 = st.tabs(["🔍 Text Analysis", "🌐 Platform Search"])

# List of sample words for the "New Word" feature
SAMPLE_WORDS = [
    "Artificial Intelligence", "Machine Learning", "Data Science", 
    "Web Development", "Python Programming", "Streamlit Applications",
    "Natural Language Processing", "Computer Vision", "Deep Learning",
    "Cloud Computing", "Internet of Things", "Cybersecurity",
    "Blockchain Technology", "Virtual Reality", "Augmented Reality"
]

# Simple text analysis function (replaces the transformers model)
def analyze_text(text):
    # Simple text analysis without transformers
    word_count = len(text.split())
    char_count = len(text)
    sentiment = "Positive" if any(word in text.lower() for word in ["good", "great", "excellent", "awesome", "happy"]) else "Neutral"
    if any(word in text.lower() for word in ["bad", "terrible", "awful", "hate", "sad"]):
        sentiment = "Negative"
    
    return {
        "Word Count": word_count,
        "Character Count": char_count,
        "Sentiment": sentiment,
        "Readability": "Easy" if word_count < 20 else "Moderate" if word_count < 50 else "Complex"
    }

# Search functions
def search_youtube(query):
    url = f"https://www.youtube.com/results?search_query={query}+full+movie"
    webbrowser.open(url)
    return url

def search_google(query):
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)
    return url

def search_google_play_movies(query):
    url = f"https://play.google.com/store/search?q={query}+full+movie&c=movies"
    webbrowser.open(url)
    return url

def search_netflix(query):
    url = f"https://www.netflix.com/search?q={query}"
    webbrowser.open(url)
    return url

def search_instagram(username):
    username = username.replace('@', "")
    url = f"https://www.instagram.com/{username}/"
    webbrowser.open(url)
    return url

def search_facebook(query):
    url = f"https://www.facebook.com/search/top?q={query}"
    webbrowser.open(url)
    return url

def search_x(query):
    url = f"https://twitter.com/search?q={query}"
    webbrowser.open(url)
    return url

def search_chatgpt(query):
    url = f"https://chat.openai.com/?q={query}"
    webbrowser.open(url)
    return url

def search_github(query):
    url = f"https://github.com/search?q={query}"
    webbrowser.open(url)
    return url

def search_meta_ai():
    url = "https://ai.facebook.com"
    webbrowser.open(url)
    return url

def search_snapchat(query):
    url = f"https://story.snapchat.com/search?q={query}"
    webbrowser.open(url)
    return url

# Function to clear all inputs and results
def restart_app():
    st.session_state.text_input = ""
    st.session_state.query = ""
    st.rerun()

# Function to generate a new random word
def get_new_word():
    return random.choice(SAMPLE_WORDS)

with tab1:
    st.header("Text Analysis")
    
    # Initialize session state for text input
    if 'text_input' not in st.session_state:
        st.session_state.text_input = ""
    
    # Initialize session state for new word
    if 'current_word' not in st.session_state:
        st.session_state.current_word = get_new_word()
    
    # Create columns for buttons at the top
    col_buttons1, col_buttons2 = st.columns([1, 1])
    
    with col_buttons1:
        if st.button("🔄 Restart", key="restart_tab1", use_container_width=True, 
                    help="Clear all inputs and results"):
            restart_app()
    
    with col_buttons2:
        if st.button("✨ New Word", key="new_word_btn", use_container_width=True, 
                    help="Get a new random word to analyze"):
            st.session_state.current_word = get_new_word()
            st.session_state.text_input = st.session_state.current_word
            st.rerun()
    
    # Text area with current word as placeholder or value
    text_input = st.text_area(
        "Enter text for analysis:",
        value=st.session_state.text_input,
        placeholder=st.session_state.current_word,
        height=150,
        key="text_analysis_input"
    )
    
    # Buttons for analysis
    col_analyze1, col_analyze2 = st.columns([2, 1])
    
    with col_analyze1:
        if st.button("Analyze Text", key="analyze_btn", use_container_width=True):
            if text_input:
                with st.spinner("Analyzing..."):
                    analysis = analyze_text(text_input)
                
                col1, col2 = st.columns(2)
                with col1:
                    st.markdown('<div class="platform-card">', unsafe_allow_html=True)
                    st.metric("Word Count", analysis["Word Count"])
                    st.metric("Character Count", analysis["Character Count"])
                    st.markdown('</div>', unsafe_allow_html=True)
                
                with col2:
                    st.markdown('<div class="platform-card">', unsafe_allow_html=True)
                    st.metric("Sentiment", analysis["Sentiment"])
                    st.metric("Readability", analysis["Readability"])
                    st.markdown('</div>', unsafe_allow_html=True)
            else:
                st.warning("Please enter some text to analyze.")
    
    with col_analyze2:
        if st.button("Use Sample Word", key="sample_word_btn", use_container_width=True):
            st.session_state.text_input = st.session_state.current_word
            st.rerun()

with tab2:
    st.header("Platform Search")
    
    # Initialize session state for query
    if 'query' not in st.session_state:
        st.session_state.query = ""
    
    # Restart button at the top
    if st.button("🔄 Restart", key="restart_tab2", use_container_width=True, 
                help="Clear all inputs and results"):
        restart_app()
    
    query = st.text_input("Enter your search query:", 
                         value=st.session_state.query,
                         placeholder="Search for movies, profiles, or anything...",
                         key="search_query_input")
    
    # Organize buttons in columns for better layout
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("🎥 YouTube Movies", key="youtube_btn"):
            if query: 
                url = search_youtube(query)
                st.success(f"Searching YouTube for: {query}")
                st.info(f"URL: {url}")
            else: 
                st.warning("Please enter a search query first.")
        
        if st.button("📸 Instagram", key="instagram_btn"):
            if query: 
                url = search_instagram(query)
                st.success(f"Searching Instagram for: {query}")
                st.info(f"URL: {url}")
            else: 
                st.warning("Please enter a username first.")
        
        if st.button("🤖 ChatGPT", key="chatgpt_btn"):
            if query: 
                url = search_chatgpt(query)
                st.success(f"Searching ChatGPT for: {query}")
                st.info(f"URL: {url}")
            else: 
                st.warning("Please enter a search query first.")
    
    with col2:
        if st.button("🎥 Google Play Movies", key="play_btn"):
            if query: 
                
                url = search_google_play_movies(query)
                st.success(f"Searching Google Play Movies for: {query}")
                st.info(f"URL: {url}")
            else: 
                st.warning("Please enter a search query first.")
        
        if st.button("📘 Facebook", key="facebook_btn"):
            if query: 
                url = search_facebook(query)
                st.success(f"Searching Facebook for: {query}")
                st.info(f"URL: {url}")
            else: 
                st.warning("Please enter a search query first.")
        
        if st.button("✨ Gemini (Google)", key="gemini_btn"):
            if query: 
                url = search_google(query)
                st.success(f"Searching Google for: {query}")
                st.info(f"URL: {url}")
            else: 
                st.warning("Please enter a search query first.")
    
    with col3:
        if st.button("🎥 Netflix", key="netflix_btn"):
            if query: 
                url = search_netflix(query)
                st.success(f"Searching Netflix for: {query}")
                st.info(f"URL: {url}")
            else: 
                st.warning("Please enter a search query first.")
        
        if st.button("🐦 X (Twitter)", key="x_btn"):
            if query: 
                url = search_x(query)
                st.success(f"Searching X for: {query}")
                st.info(f"URL: {url}")
            else: 
                st.warning("Please enter a search query first.")
        
        if st.button("🐙 GitHub", key="github_btn"):
            if query: 
                url = search_github(query)
                st.success(f"Searching GitHub for: {query}")
                st.info(f"URL: {url}")
            else: 
                st.warning("Please enter a search query first.")
    
    # Special buttons that don't need a query
    st.markdown("---")
    col4, col5, col6 = st.columns(3)
    
    with col5:
        if st.button("🧠 Meta AI Homepage", key="meta_btn"):
            url = search_meta_ai()
            st.success("Opening Meta AI homepage")
            st.info(f"URL: {url}")
        
        if st.button("👻 Snapchat", key="snapchat_btn"):
            if query: 
                url = search_snapchat(query)
                st.success(f"Searching Snapchat for: {query}")
                st.info(f"URL: {url}")
            else: 
                st.warning("Please enter a search query first.")

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #888;'>Built with ❤️ by Sarim</div>", 
    unsafe_allow_html=True
)