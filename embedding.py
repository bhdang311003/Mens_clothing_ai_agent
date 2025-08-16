import pandas as pd # type: ignore
from langchain_community.vectorstores import FAISS # type: ignore
from langchain_huggingface import HuggingFaceEmbeddings # type: ignore

df = pd.read_csv("Data/mens_clothing.csv", low_memory=False)

df["ratings"] = pd.to_numeric(df["ratings"], errors="coerce")
df["no_of_ratings"] = df["no_of_ratings"].str.replace(",", "", regex=False)
df["no_of_ratings"] = pd.to_numeric(df["no_of_ratings"], errors="coerce").astype("Int64")

products = df.to_dict(orient="records")

def build_text(product):
    return (
        f"Product: {product['name']}. "
        f"Category: {product['category']}. "
        f"Price: ${product['discount_price_usd']} (original ${product['actual_price_usd']}). "
        f"Rating: {product['ratings']} stars from {product['no_of_ratings']} reviews."
    )

product_texts = [build_text(prod) for prod in products]

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2") #all-mpnet-base-v2

vectorstore = FAISS.from_texts(product_texts, embeddings)
vectorstore.save_local("faiss_product_index")