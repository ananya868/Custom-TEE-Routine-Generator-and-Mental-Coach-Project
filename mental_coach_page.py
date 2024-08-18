import streamlit 
from llm import get_query_embeddings 
from pinecone_query import query_pinecone_index 
from llm import response


def mental_coach(pinecone_api_key, openai_api_key, index_name):

    def generate_answer(question: str): 

        ques = question
        
        # Query Embeddings 
        query_embeddings = get_query_embeddings(ques, openai_api_key)

        # Query Pinecone Index 
        query_response = query_pinecone_index(pinecone_api_key, query_embeddings, index_name)

        # Get the answer from the response
        text_answer = query_response['matches'][0].metadata['Answer']

        # Prompt
        prompt = f"You are a mental coach for baseball. Your duty is to provide players with proper guidance in a friendly manner. Analyze this para: {text_answer}, and create a concise, friendly answer for the player who is suffering from the problem. Make your answer properly structured"

        # Generate response
        answer = response(prompt, openai_api_key).choices[0].message.content

        return answer 

    
    # Streamlit app
    streamlit.markdown("# Mental Coach for Baseball/Softball 🧠")
    streamlit.write("Welcome to the Mental Coach for Baseball! Please ask your question below to get the best advice from our mental coach.")

    question = streamlit.text_area("Question", placeholder="Ask your question here...")

    if streamlit.button("Get Advice"):
        answer = generate_answer(question)
        streamlit.write("")
        streamlit.write("")
        streamlit.write(answer)