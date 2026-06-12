# Artificial Intelligence: GreenMind Assistant & Classic AI Solutions

Welcome to the **Artificial Intelligence** repository! This project serves as a dual-purpose AI collection, featuring a modern **RAG (Retrieval-Augmented Generation)** based Personal Assistant and a comprehensive library of **Classic AI Algorithm Solutions**.

---

## 🤖 GreenMind: Your Personal AI Assistant

**GreenMind** is a state-of-the-art AI assistant project designed to leverage the power of Large Language Models (LLMs) combined with document-based knowledge retrieval.

### 🌟 Key Features
- **Retrieval-Augmented Generation (RAG)**: Combines retrieved information from your own documents with advanced language modeling.
- **Large Language Model**: Powered by the **Qwen2.5 7B** model.
- **Efficient Embedding**: Uses **Qwen3-Embedding-0.6B** for fast and accurate semantic search.
- **Smart Retrieval**: Utilizes **LangChain** retrievers to act as a "Smart Librarian," finding relevant data within a large corpus of unstructured text.

### 🛠️ Technologies & Tools
- **Language**: Python
- **Frameworks**: LangChain, Transformers, PyTorch
- **Vector Database**: ChromaDB
- **PDF Processing**: PyPDF
- **Model**: Qwen2.5 (LLM) & Qwen3 (Embeddings)

> [!NOTE]
> You can find the implementation in the `GreenMind_Assistant/` directory.

---

## 🧠 Classic AI Solutions

This section of the repository contains a variety of Python implementations for fundamental AI topics, ranging from basic programming exercises to complex search algorithms.

### 📂 Categorized Solutions

#### 🔍 Search & Optimization Algorithms
Located in `Classic_AI_Solutions/Search_Algorithms/`:
- **BFS & DFS**: Topological sorting and grid-based pathfinding.
- **IDDFS**: Iterative Deepening Depth-First Search for dynamic graphs.
- **Pathfinding**: Finding paths from source to destination with obstacle handling.
- **Graph Theory**: Adjacency lists and parent tracking implementations.

#### 🐍 Basic Python AI Exercises
Located in `Classic_AI_Solutions/Basic_Python_Exercises/`:
- **Core Logic**: Factorials, Fibonacci sequences, Odd/Even detection.
- **Data Structures**: List and Tuple manipulations, range indexing.
- **Math-based AI**: Primality tests, largest numbers, and summation parameters.

---

## 🏗️ Project Structure

```text
Artificial-intelligence/
├── GreenMind_Assistant/           # Dedicated folder for the AI Assistant
│   └── GreenMind_AI.ipynb         # Main RAG Pipeline Notebook
├── Classic_AI_Solutions/          # Collection of AI topic solutions
│   ├── Basic_Python_Exercises/    # Core Python & Logic exercises
│   └── Search_Algorithms/         # Pathfinding & Graph search scripts
└── README.md                      # Project documentation
```

---

## 🚀 Getting Started

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/Fuad2e3/Artificial-intelligence.git
    cd Artificial-intelligence
    ```

2.  **For GreenMind Assistant**:
    - Open `GreenMind_Assistant/GreenMind_AI.ipynb` in Google Colab or Jupyter Lab.
    - Follow the notebook cells to install dependencies and run the RAG pipeline.

3.  **For Classic Solutions**:
    - Navigate to `Classic_AI_Solutions/` and run any script using Python:
    ```bash
    python Classic_AI_Solutions/Search_Algorithms/topology_bfs.py
    ```

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

<p align="center">
  Developed with ❤️ by <b>Team Softece</b><br>
  <i>Artificial-intelligence | Green University of Bangladesh</i>
</p>
