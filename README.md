# 🎌 AI Anime Recommender

An AI-powered anime recommendation system that uses **semantic search,
vector embeddings, ChromaDB, and a Groq-hosted LLM** to recommend anime
based on natural-language user preferences.

Instead of relying only on exact genre or keyword matching, the
application converts anime descriptions into vector embeddings and
retrieves semantically relevant titles before using an LLM to generate a
concise, personalized recommendation.

## 🏗️ System Architecture

![AI Anime Recommender Architecture](architecture.png)

The architecture is organized into three major areas:

### 1. Project Setup

-   **Groq API** -- provides access to the LLM used for generating
    recommendations.
-   **Hugging Face** -- provides the embedding model, such as
    `all-MiniLM-L6-v2`, used for semantic representation of anime data.
-   **Virtual Environment** -- isolates project dependencies.
-   **Logging** -- captures application and pipeline events.
-   **Custom Exception Handling** -- provides structured error
    reporting.
-   **Project Structure** -- separates configuration, data loading,
    vector storage, recommendation logic, and application code.

### 2. Core Code

-   **Configuration** -- loads environment variables and model settings.
-   **Data Loader** -- reads and validates the anime dataset and
    prepares the data for indexing.
-   **ChromaDB** -- stores anime embeddings and enables similarity-based
    retrieval.
-   **Prompt Templates** -- define how retrieved anime information is
    presented to the LLM.
-   **Recommender Class** -- combines retrieval and LLM generation into
    the recommendation workflow.
-   **Train & Recommend** -- builds the vector store and serves
    recommendation requests.

### 3. Deployment

The application is designed with deployment options including:

-   **Streamlit App** -- user-facing web interface.
-   **Dockerfile** -- containerization for consistent deployment.
-   **GCP VM** -- virtual-machine deployment on Google Cloud.
-   **Kubernetes Deployment** -- deployment using Kubernetes.
-   **Kubernetes App/Service** -- exposes the application in a
    Kubernetes environment.
-   **GitHub Integration** -- source control and CI/CD integration.
-   **Grafana Cloud** -- monitoring and observability.

------------------------------------------------------------------------

## 🔄 Recommendation Flow

``` text
User Query
    │
    ▼
Streamlit App
    │
    ▼
Recommendation Pipeline
    │
    ├──► Hugging Face Embeddings
    │        │
    │        ▼
    │     ChromaDB
    │        │
    │        ▼
    │   Relevant Anime
    │
    └──► Prompt Template
             │
             ▼
          Groq LLM
             │
             ▼
     Personalized Recommendations
```

For example, a user can enter:

> I want to watch a fantasy anime with magic and adventure.

The system retrieves semantically related anime from ChromaDB and passes
the relevant context to the LLM. The LLM then produces recommendations
with explanations for why each title matches the request.

------------------------------------------------------------------------

## ✨ Key Features

-   Natural-language anime search
-   Semantic similarity-based retrieval
-   Hugging Face sentence embeddings
-   ChromaDB vector database
-   Groq LLM integration
-   Prompt-based recommendation generation
-   Streamlit user interface
-   Custom exception handling
-   Logging
-   Local development using a Python virtual environment
-   Docker-ready deployment
-   Kubernetes-ready architecture
-   Google Cloud VM deployment option
-   GitHub-based version control
-   Monitoring with Grafana Cloud

------------------------------------------------------------------------

## 🧰 Technology Stack

  Layer               Technology
  ------------------- --------------------------------------
  Language            Python
  UI                  Streamlit
  LLM                 Groq
  LLM Model           Configurable through `MODEL_NAME`
  Embeddings          Hugging Face / Sentence Transformers
  Embedding Model     `all-MiniLM-L6-v2`
  Vector Database     ChromaDB
  LLM/RAG Framework   LangChain
  Configuration       Python + `.env`
  Containerization    Docker
  Cloud               Google Cloud Platform
  Orchestration       Kubernetes
  Source Control      GitHub
  Monitoring          Grafana Cloud

------------------------------------------------------------------------

## 📁 Suggested Project Structure

``` text
AI anime recommender/
│
├── app/
│   └── app.py
│
├── data/
│   ├── raw/
│   └── processed/
│
├── pipeline/
│   ├── build_pipeline.py
│   └── pipeline.py
│
├── src/
│   ├── data_loader.py
│   ├── vector_store.py
│   ├── recommender.py
│   └── ...
│
├── config.py
├── .env
├── .gitignore
├── requirements.txt
├── Dockerfile
└── README.md
```

The exact structure can vary depending on the implementation.

------------------------------------------------------------------------

## ⚙️ Configuration

Create a `.env` file in the project root:

``` env
GROQ_API_KEY=your_groq_api_key
```

The application configuration can load the key with:

``` python
import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

MODEL_NAME = "your-groq-model"
```

Keep secrets out of source control.

Add the following to `.gitignore`:

``` gitignore
.env
venv/
__pycache__/
*.pyc
```

> A Hugging Face API token is generally not required when a public
> embedding model such as `sentence-transformers/all-MiniLM-L6-v2` is
> downloaded and executed locally. Add one only if your implementation
> requires authenticated Hugging Face Hub access.

------------------------------------------------------------------------

## 🚀 Local Setup

### 1. Clone the repository

``` bash
git clone <your-repository-url>
cd "AI anime recommender"
```

### 2. Create a virtual environment

On macOS/Linux:

``` bash
python3 -m venv venv
source venv/bin/activate
```

On Windows:

``` bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

``` bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create `.env` and add your Groq API key.

### 5. Build the vector store

Run the pipeline used by the project to load, process, embed, and index
the anime dataset:

``` bash
python pipeline/build_pipeline.py
```

### 6. Start the Streamlit application

``` bash
streamlit run app/app.py
```

Open the Streamlit URL shown in the terminal.

------------------------------------------------------------------------

## 🧠 How RAG Works in This Project

The recommender follows a Retrieval-Augmented Generation (RAG) pattern.

### Indexing

1.  Anime records are loaded from the dataset.
2.  Required fields are validated.
3.  Anime information is combined into searchable text.
4.  The text is converted into embeddings using `all-MiniLM-L6-v2`.
5.  Embeddings are stored in ChromaDB.

### Recommendation

1.  The user enters a natural-language query.
2.  The query is converted into an embedding.
3.  ChromaDB finds the most semantically similar anime records.
4.  Retrieved records are inserted into a prompt.
5.  The Groq LLM generates the final recommendations.
6.  Streamlit displays the response.

This allows queries such as:

-   `I want a dark fantasy anime`
-   `Recommend an anime with magic and adventure`
-   `I want something similar to an isekai`
-   `Find an anime with supernatural elements and romance`

------------------------------------------------------------------------

## 🐳 Docker Deployment

The architecture includes a Docker-based deployment path.

A typical workflow is:

``` bash
docker build -t anime-recommender .
docker run --env-file .env -p 8501:8501 anime-recommender
```

The exact Docker configuration depends on the project's `Dockerfile`.

------------------------------------------------------------------------

## ☸️ Kubernetes Deployment

The application can also be containerized and deployed to Kubernetes.

Typical deployment flow:

``` text
GitHub
   ↓
Docker Image
   ↓
Container Registry
   ↓
Kubernetes Deployment
   ↓
Kubernetes Service
   ↓
Streamlit Application
```

Secrets such as `GROQ_API_KEY` should be managed through Kubernetes
Secrets rather than committed to manifests or source control.

------------------------------------------------------------------------

## ☁️ Google Cloud Deployment

The architecture supports deployment on a Google Cloud VM.

A typical flow is:

``` text
Local Development
       ↓
GitHub
       ↓
Docker
       ↓
GCP VM
       ↓
Streamlit App
```

For production workloads, Kubernetes can be used instead of a single VM
when scaling and orchestration are required.

------------------------------------------------------------------------

## 📊 Monitoring

Grafana Cloud can be integrated for application and infrastructure
observability.

Useful metrics include:

-   Application availability
-   Request count
-   Recommendation latency
-   Error rate
-   Resource utilization
-   Container health
-   Model/API failures

Logging and custom exception handling should be used alongside
monitoring to make pipeline failures easier to diagnose.

------------------------------------------------------------------------

## 🔐 Security Considerations

-   Never commit `.env` files.
-   Never hard-code API keys in Python files.
-   Use environment variables or secret managers for credentials.
-   Use Kubernetes Secrets for Kubernetes deployments.
-   Rotate exposed API keys immediately.
-   Restrict API keys to the required services and permissions.
-   Avoid logging secret values.

------------------------------------------------------------------------

## 🛠️ Troubleshooting

### `ModuleNotFoundError`

Make sure the virtual environment is activated:

``` bash
source venv/bin/activate
```

Then verify:

``` bash
which python
python --version
```

### Groq API key error

If the application reports that `GROQ_API_KEY` is missing, verify that:

``` text
.env
```

exists in the project root and contains:

``` env
GROQ_API_KEY=your_key
```

Also make sure `load_dotenv()` runs before `ChatGroq` is initialized.

### Model not found

Groq model names can change over time. Keep the active model in
`config.py` rather than scattering the model name throughout the code.

### Vector store errors

Rebuild the vector store after changing the source dataset, embedding
model, or document-processing logic.

------------------------------------------------------------------------

## 📌 Future Improvements

-   Add anime posters and metadata to recommendations.
-   Add filters for genre, year, rating, and episode count.
-   Add user feedback and recommendation history.
-   Add evaluation metrics for retrieval quality.
-   Add automated tests for data loading and retrieval.
-   Add CI/CD through GitHub Actions.
-   Add structured application metrics.
-   Add production-grade secret management.
-   Add recommendation caching.
-   Improve duplicate-document handling in retrieval results.

------------------------------------------------------------------------

## 🎯 Project Goal

The goal of this project is to demonstrate how a modern **LLM + RAG +
vector database** application can be built from data ingestion through
local development and extended toward cloud-native deployment.

It combines:

**Data → Embeddings → ChromaDB → Retrieval → Prompting → LLM → Streamlit
→ Docker/Kubernetes → Monitoring**

to create an end-to-end AI anime recommendation system.
