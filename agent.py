from langchain_community.chat_models import ChatOpenAI # type: ignore
from langchain.agents import initialize_agent, AgentType # type: ignore
from langchain_huggingface import HuggingFaceEmbeddings # type: ignore
from langchain_community.vectorstores import FAISS # type: ignore
from langchain.tools import tool # type: ignore
from langchain.chains import RetrievalQA # type: ignore
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent # type: ignore
import requests # type: ignore
import pandas as pd # type: ignore
import os


os.environ["OPENAI_API_KEY"] = "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"
os.environ["OPENAI_API_BASE"] = "https://openrouter.ai/api/v1"

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2") #all-mpnet-base-v2

vectorstore = FAISS.load_local(
    "faiss_product_index",
    embeddings,
    allow_dangerous_deserialization=True
)

llm = ChatOpenAI(
    model="openai/gpt-4.1-mini", 
    temperature=0
)

retriever = vectorstore.as_retriever(search_kwargs={"k": 10})

qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    return_source_documents=True  
)

df = pd.read_csv("Data/mens_clothing.csv", low_memory=False)

agent = create_pandas_dataframe_agent(
    llm,
    df,
    verbose=False,
    allow_dangerous_code=True
)

def ask_agent(agent, query):
    prompt = f"""
    You are a helpful shopping assistant. 
    Answer the following user question in a natural, conversational tone. 
    Do not mention 'dataframe', 'rows', or technical terms. 
    Just give a friendly answer as if you are helping a customer in a store.

    Question: {query}
    """
    return agent.run(prompt)

def classify_query(query):
    prompt = f"""
    You are a classifier for a shopping assistant.
    Classify the user question into one of two categories:
    - "RAG": If the question is about **searching, reading, or retrieving textual information** related to products or Q&A.
    - "AGENT": If the question requires **filtering, calculation, aggregation, comparison, or price-based queries** about products, such as cheapest, most expensive, average price, counting items, filtering by size/color/brand, or comparing multiple products.
    Only return one of these two words: RAG or AGENT.
    Question: {query}
    """
    result = llm.invoke(prompt)
    return result.content.strip()
    
def answer_query(query):
    intent = classify_query(query)

    if intent == "AGENT":
        print("[Agent Mode]")
        return ask_agent(agent, query)
    else:
        print("[RAG Mode]")
        # print("\n----------- Source documents -----------")
        # for doc in result["source_documents"]:
        #     print("-", doc.page_content)
        return qa_chain({"query": query})["result"]
    
# query = "Give me some products of NEVA"
# print(answer_query(query))
