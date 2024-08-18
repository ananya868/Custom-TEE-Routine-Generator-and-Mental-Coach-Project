from pinecone import Pinecone
from langchain.embeddings.openai import OpenAIEmbeddings


def query_pinecone_index(papi, query_embeddings: list, index_name, include_metadata: bool = True):

    pc = Pinecone(api_key=papi)

    # get index
    if index_name == "data":
        index = pc.Index("data")
    elif index_name == "mental-data":
        index = pc.Index("mental-data")
    else: 
        print("Wrong Index name")

    # get response
    query_response = index.query(
        vector=query_embeddings, top_k=1, include_metadata=include_metadata
    )
    return query_response
    

