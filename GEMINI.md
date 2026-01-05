# GEMINI.md

## Project Overview

This project is a Python-based Retrieval-Augmented Generation (RAG) system designed to answer questions about a microwave manual. It leverages LangChain for the overall RAG pipeline, FAISS for efficient similarity search on a local vector store, and Azure OpenAI for generating answers based on the retrieved context.

The system works by first creating a vector index of the microwave manual. When a user asks a question, the system retrieves the most relevant parts of the manual, augments the user's prompt with this context, and then uses a large language model to generate a precise answer.

## Building and Running

### 1. Install Dependencies

First, ensure you have Python 3.11+ and pip installed. Then, install the required Python packages:

```bash
pip install -r requirements.txt
```

### 2. Configure API Credentials

This project uses the DIAL service, which requires an API key.

1.  **Set Environment Variable:**
    Set the `DIAL_API_KEY` environment variable to your DIAL API key. You can do this in your shell:
    ```bash
    export DIAL_API_KEY='your-api-key-here'
    ```
    Or by creating a `.env` file in the root of the project and adding the following line:
    ```
    DIAL_API_KEY='your-api-key-here'
    ```

2.  **Update Constants (if necessary):**
    The `task/_constants.py` file contains the `DIAL_URL`. If this URL needs to be changed, you can update it there.

### 3. Running the Application

To start the RAG assistant, run the `app.py` script:

```bash
python task/app.py
```

The application will first build the FAISS index if it doesn't exist and then prompt you for questions.

## Development Conventions

*   **Code Structure:** The main logic is encapsulated in the `MicrowaveRAG` class in `task/app.py`. This class is responsible for setting up the vector store, retrieving context, augmenting the prompt, and generating answers.
*   **Constants:** API keys and URLs are managed in `task/_constants.py`.
*   **Dependencies:** Project dependencies are listed in `requirements.txt`.
*   **Knowledge Base:** The `task/microwave_manual.txt` file is the source of truth for the RAG system.
*   **TODOs:** The `README.md` file outlines the `TODO` items for completing the implementation in `app.py`.
