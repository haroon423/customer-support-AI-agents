# Customer Support AI Agents 🤖📞

This project implements a conversational AI assistant for customer support using **LangGraph**, **LangChain**, and **Groq**. It automates responses to customer queries using graph-based logic and large language models.

---

## 🚀 Features

- 🔄 **Graph-Based Workflow** with LangGraph
- 🧠 **LLM Integration** via Groq (Supports LLaMA3, Gemma, etc.)
- 🗣️ Dynamic Customer Question Handling
- 📦 Simple CLI for asking questions
- 🛠️ Easily customizable logic and models

---

## 📁 Project Structure

.
├── main1.py # Entry point: ask question and get LLM response
├── support_graph.py # LangGraph logic: defines state, nodes, edges
├── .env # Contains your Groq API key
├── config/ # Agent & Task YAML config files (for CrewAI-based version)
├── requirements.txt # Python dependencies
└── README.md # Project overview and usage instructions

---

## 🧪 Example

```bash
$ python main1.py
Enter your customer question: What is your refund policy?
Response: We offer a 30-day refund on all international orders if returned unused and in original packaging.

🔧 Setup Instructions
1. Clone the repository

git clone git@github.com:haroon423/customer-support-AI-agents.git
cd customer-support-AI-agents

2. Create and activate a virtual environment

python -m venv myenv
myenv\Scripts\activate   # On Windows

3. Install dependencies

pip install -r requirements.txt

4. Create .env file

GROQ_API_KEY=your_groq_api_key_here

🔄 Switch Models
You can switch the model in support_graph.py

ChatGroq(
    temperature=0.2,
    model_name="llama3-8b-8192",
    api_key=os.environ["GROQ_API_KEY"]
)

Supported models:

llama3-8b-8192

gemma-7b-it

(avoid deprecated: mixtral-8x7b)

💡 Future Enhancements
Integrate documentation RAG

Add web interface with Streamlit or Gradio

Enable multi-turn chat flow

👤 Author
Haroon Khan
GitHub: @haroon423

📜 License
MIT License

---

✅ You can now place this content in your `README.md` file and commit it. Let me know if you want to include badges (like Python version, license, etc.) or deploy it on Streamlit or Hugging Face Spaces.


