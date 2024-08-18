from tee_routine_gen_page import tee_routine_generator 
from mental_coach_page import mental_coach
import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the API key from the environment variables
openai_api_key = os.getenv('OPENAI_API_KEY')
pinecone_api_key = os.getenv('PINECONE_API_KEY')


# Navigation
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Select a page", ["Home", "TEE Routine Generator", "Mental Coach"])


def Home():
    st.markdown(
        """
        # Custom TEE Routine Generator and Mental Coach 🧢

        Welcome to the **TEE Routine and Mental Coach** app - your virtual mentor for enhancing your baseball or softball gameplay! This app is like having a personal coach and a supportive teammate right by your side.
        
        ## What We Offer ⚾️

        Our app brings to you personalized training routines and mental coaching advice extracted from the wisdom shared by expert players and coaches on YouTube. Think of it as the best baseball advice, all in one place!

        ### Tailored Training 🏋️‍♂️

        Whether you're just starting out or you're a seasoned player, our app generates training routines tailored to your specific player profile. We take into account:
        - Your **Age**: Because training needs evolve.
        - Your **Experience**: Novice or pro? We've got you covered.
        - Your **Sport**: Baseball or Softball, the routines are crafted for your game.
        - **Common Issues**: We address the hurdles you're facing.
        - **Training Time**: Your routine fits into your schedule, not the other way around.

        ### Mental Coaching 🧠

        Stuck with a mental block? Struggling with focus? Type in your issue, and get back on track with advice from players who've been right where you are. Our AI-powered mental coach is trained on Q&A datasets to provide you with solutions to conquer the mental game.

        ### Our Journey 🚀

        This app is the culmination of extensive research and data curation. We've delved into countless hours of expert content and transcribed wisdom from the best baseball and softball channels on YouTube. After cleaning and structuring this gold mine of information into datasets, we've employed RAG (Pinecone) and large language models to make sure you get advice that's spot-on.

        ### About me 🤝

        I'm an Ai engineer interested in building RAG based systems, fine-tuning LLMs for certain business use-case, building multi-ai agent apps.
        Contact me from the following links below 👇🏻
        
        *links*
        - [Github] (https://github.com/ananya868)
        - [LinkedIn] (https://www.linkedin.com/in/ananya8154/)
        ---
        """
    )
        

if page == "Home":
    Home()
elif page == "TEE Routine Generator":
    tee_routine_generator(pinecone_api_key, openai_api_key, index_name="data")
elif page == "Mental Coach":
    mental_coach(pinecone_api_key, openai_api_key, "mental-data")
