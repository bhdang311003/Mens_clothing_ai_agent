# 🧑‍💼 Men’s Clothing AI Agent  

## 📌 Overview  
This project demonstrates an AI Agent designed to act as a smart shopping assistant for men’s clothing products.
By integrating LangChain with Retrieval-Augmented Generation (RAG) and deploying via FastAPI, the agent can answer user queries in a natural, conversational way — just like a virtual sales assistant.

<p align="center">
  <img src="https://github.com/user-attachments/assets/bc67ce47-fccf-4412-a68e-1db8e17d0a82" width="595" height="515" alt="Demo Image"/>
</p>


### 🔑 Key points:
- **AI Agent for Q&A**: Users can ask product-related questions (e.g., prices, specifications, comparisons) and receive contextual answers.
- **LangChain-powered pipeline**: Manages prompt orchestration, memory, and tool integration.
- **RAG with FAISS**: Efficient retrieval over processed men’s clothing data, ensuring accurate and relevant responses.
- **FastAPI Deployment**: Provides an interactive API endpoint for seamless integration with frontend or external services.
- **Streamlit Frontend**: Provides an interactive UI for demo and end-user interaction. 
- **Lightweight Data Processing**: Preprocessing of men’s clothing product CSV files to build a clean and searchable dataset.

This AI Agent provides a foundation for building e-commerce chatbots or virtual shopping assistants.

## Project Structure
```
📂 Project Root
├── 📂 Data
│   ├── Innerwear.csv
│   ├── Jeans.csv
│   ├── T-shirts and Polos.csv
│   ├── Shirts.csv
│   └── mens_clothing.csv
├── 📂 faiss_product_index
│   ├── index.faiss
│   └── index.pkl
├── agent.py
├── api_app.py
├── api_main.py
├── client.py
├── embedding.py
├── preprocess_data.ipynb
├── requirements.txt
└── README.md
```
## Dataset
### Original data source: [Amazon Products Dataset (Kaggle)](https://www.kaggle.com/datasets/lokeshparab/amazon-products-dataset).
Because the original data is very large, in this project, I only use products with the main category of Men's Clothing, so I only download 4 CSV files and save them in the Data/ folder: Innerwear.csv, Jeans.csv, T-shirts and Polos.csv, Shirts.csv.

## Installation
### Clone repository
  ```
  git clone https://github.com/bhdang311003/Mens_clothing_ai_agent.git
  cd Mens_clothing_ai_agent
  ```
### Requirements
Modules and dependencies in `requirements.txt`
  ```
  pip install -r requirements.txt
  ```

### Usage
**Set up before using**: Run `preprocess_data.ipynb` to create `mens_clothing.csv`, run `embedding.py` to embed data in save index in `faiss_product_index`

**Run FastAPI Backend**

Run the code below and wait for API:
  ```
  python api_main.py
  ```
- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

**Without UI**
  ```
  python client.py
  ``` 
**Run Streamlit Frontend (UI)**
  ```
  stremlit run api_app.py
  ```

## API Endpoints
### 1. GET /
- **Purpose:** Check if the API is running.
- **Request:** No parameters required.
- **Response:** JSON example:
```
{
  "message": "Men's Clothing AI Agent API is running!"
}
```

### 2. POST /ask
- **Purpose:** Ask a question to the AI Agent about men’s clothing products.
- **Request:** JSON body containing your question:
```
{
  "query": "Which T-shirt is the cheapest?"
}
```
- **Response:** JSON example:
```
{
  "query": "Which T-shirt is the cheapest?",
  "answer": "The cheapest T-shirt is XYZ at $19.99."
}
```






