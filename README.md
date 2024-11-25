# Advanced-HR-Q&A-Chatbot

### Project Description:

This project is an **Advanced HR Q&A Chatbot** built using **Python**, **Flask**, **MongoDB**, **LangChain**, and **VectorDB**. The chatbot leverages **Retrieval-Augmented Generation (RAG)** architecture to automate and optimize the recruitment process. It includes two key phases: 

1. **Phase 1: Job Role & Resume Matching (ATS)**: Analyzes candidate resumes against job descriptions using embeddings.
2. **Phase 2: Question Generation**: Automatically generates multiple-choice questions (MCQs) for HR and candidates based on the job role, categorized by difficulty (Beginner, Intermediate, Advanced).

The system incorporates **RAG Landscape and Architectures** to ensure relevant results through semantic search and efficient data retrieval and generation.

### Key Features:

- **Query Translation and Routing**:
  - **Query translation techniques** like pseudo-documents are used to split long job descriptions or queries into smaller, more meaningful chunks.
  - **Semantic routing** determines which database (resumes, job roles, or MCQs) is most appropriate for a query.

- **Hierarchical Indexing**:
  - **Hierarchical indexing** organizes embeddings into categories such as skills, industry, or experience level to improve retrieval accuracy.

- **Embedding Generation**:
  - Generates dense embeddings for resumes, job descriptions, and questions using **Large Language Models (LLMs)** such as **OpenAI’s GPT**, or **Sentence-Transformers**.
  - Embeddings are stored in a **Vector Database (VectorDB)** for efficient and fast retrieval.

- **Two-Stage RAG Architecture**:
  - **Stage 1: Retrieve**: Retrieves relevant candidates (resumes) using **VectorDB**.
  - **Stage 2: Generate**: Uses the retrieved documents (job descriptions and resumes) to generate tailored MCQs or interview questions for HR and candidates.

