🩺 MEDIMATE – Medical Question Answering Chatbot 🤖

MEDIMATE is an AI-powered medical question-answering chatbot built using Python, NLP, and Streamlit.
It allows users to ask questions related to diseases, symptoms, diagnosis, treatments, medicines, and medical tests, and retrieves accurate answers from a verified medical dataset.

🚀 Features

💬 ChatGPT-style interactive chat interface

🧠 Intelligent text retrieval using TF-IDF + Cosine Similarity

📚 Powered by 47,000+ verified medical Q&A pairs

🏥 Covers diseases, symptoms, diagnosis, treatments & medical tests

⚡ Fast, lightweight & efficient

🧹 Clear chat functionality with a clean Streamlit UI

🛠 Tech Stack

Python

Streamlit

Pandas

NumPy

Scikit-learn

Natural Language Processing (NLP)

📂 Project Structure
MEDIMATE-Chatbot/
│
├── APP.py                  # Streamlit application
├── model.py                # TF-IDF retrieval model
├── dataset_QA.csv          # Medical Q&A dataset
├── dataextraction.ipynb    # Dataset preprocessing & exploration
├── requirements.txt        # Project dependencies
├── README.md               # Project documentation

📊 Dataset

This project uses the NIH MedQuAD (Medical Question Answering Dataset), a trusted and publicly available medical dataset.

🔗 Dataset Link:
👉 https://github.com/abachaa/MedQuAD

Dataset Highlights

47,000+ medical question–answer pairs

Curated from NIH-trusted medical sources

Covers diseases, drugs, diagnosis, treatments & tests

📦 Requirements
🔧 Python Version

Python 3.8 or higher

📚 Required Libraries

Install all dependencies using:

pip install -r requirements.txt

📝 requirements.txt
streamlit
pandas
numpy
scikit-learn

▶️ How to Run the Project
1️⃣ Clone the Repository
git clone https://github.com/your-username/MEDIMATE-Chatbot.git
cd MEDIMATE-Chatbot

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Run the Application
streamlit run APP.py

💡 How It Works

User enters a medical question

The query is cleaned and vectorized using TF-IDF

Cosine Similarity finds the most relevant question

The corresponding verified medical answer is displayed

⚠ Disclaimer

This chatbot is intended for educational and informational purposes only.
It is not a substitute for professional medical advice, diagnosis, or treatment.
Always consult a qualified healthcare provider for medical concerns.

👨‍💻 Author

Vishesh Chavda
Data Scientist | Machine Learning & NLP Enthusiast
