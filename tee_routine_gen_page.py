import streamlit 
from llm import get_query_embeddings
from pinecone_query import query_pinecone_index
from llm import response


def tee_routine_generator(pinecone_api_key, openai_api_key, index_name):

    def generate_answer(
        name: str, age: int, sport: str, experience: str, common_issue: str, training_time: int
    ) -> str: 

        query = f"Name is {name}, age is {age}, sport is {sport}, have experience in {experience} and are facing the common issue of {common_issue}. Training time is {training_time} minutes."
        
        # Query embeddings
        query_embeddings = get_query_embeddings(query, openai_api_key)

        # Query Pinecone index
        query_response = query_pinecone_index(pinecone_api_key, query_embeddings, index_name) # returns 2 matches

        # Get the answer from the query response
        routine = query_response['matches'][0].metadata['routine']
        issue = query_response['matches'][0].metadata['common issue']
        # time = query_response['matches'][0].metadata['training time']

        # Prompt for LLM 
        prompt = f"Create a detailed, concise TEE routine based on the following paragraph: {routine}.The routine should include specific exercises, repetitions, and sets, along with time for each drill. \nThe routine should focus on common issue: {issue} and the overall routine training time should be {training_time}.\nPrioritize exercises whose target is to solve the common issue of the player."
        
        # Generate response
        answer = response(prompt, openai_api_key).choices[0].message.content

        return answer

    # streamlit.title("Custom TEE Routine Generator")
    streamlit.markdown("# Custom TEE Routine Generator 🏋🏻")
    # streamlit.image("logo.png", width=150)
    streamlit.write("Welcome to the TEE Routine Generator! Please fill in the details below to generate a custom routine for you.", )


    name = streamlit.text_input("Name", placeholder= "Your name here")
    age = streamlit.text_input("Age", placeholder= "Your age here e.g 14")
    sport = streamlit.text_input("Sport", placeholder="Which sport you want help with? Baseball or Softball")
    experience = streamlit.text_input("Experience", placeholder="Whats you experience? Intermediate or Beginner")

    common_issue = streamlit.text_input("Common Issue", placeholder="Describe common issue you face")
    
    # issues
    issues = [
        "Improving hitting skills in baseball",
        "Hitting to the opposite field",
        "Hitting mechanics and bat control",
        "Generating power while maintaining control",
        "Hitting pitches in different locations",
        "Improper swing mechanics and coordination",
        "Poor hitting mechanics",
        "lack of control and consistency in the swing",
        "lack of proper lower body mechanics in swinging"
        ]

    streamlit.write(
        "**Note**: Don't select any suggestion if you have entered your personal common issue above!"
    )
    suggested_issue = streamlit.selectbox("You can also select an issue from our suggestions", options=issues, index=None, help="You can choose from the suggestions", placeholder="Describe the common issue you face or select from the suggestions")

    training_time = streamlit.text_input("Training Time", placeholder="Your training time in minutes e.g 45")


    # Run the Routine Generator
    if streamlit.button("Generate Routine"):
        if suggested_issue: 
            issue = suggested_issue
            answer = generate_answer(name, age, sport, experience, issue, training_time)
            streamlit.write(answer)
        else:
            if common_issue == None:
                st.write("Please Enter common_issue!")
            else:
                issue = common_issue
                answer = generate_answer(name, age, sport, experience, common_issue, training_time)
                streamlit.write("")
                streamlit.write("")
                streamlit.write("")
                streamlit.write(answer)


