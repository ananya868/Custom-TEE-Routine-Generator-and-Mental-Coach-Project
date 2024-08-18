from openai import OpenAI 
import openai 
from langchain.embeddings.openai import OpenAIEmbeddings


def response(prompt, api_key):
    """ 
    Function takes prompt and generates a well formulated answer using llm 
    """
    client = OpenAI(api_key = api_key)
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are an helpful assistant who needs to understand the prompt from the user and answer accordingly"},
            {"role": "user", "content": prompt}
        ]
    )
    return response 


def get_query_embeddings(query, api_key):
    """This function returns a list of the embeddings for a given query

    Args:
        query (str): The actual query/question

    Returns:
        list[float]: The embeddings for the given query
    """
    embedding_client = OpenAIEmbeddings(api_key = api_key)
    query_embeddings = embedding_client.embed_query(query)

    return query_embeddings

