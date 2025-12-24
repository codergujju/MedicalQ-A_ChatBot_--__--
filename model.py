import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re                                 
import numpy as np 

# -----------------------------
# 1. Load Dataset
# -----------------------------
df = pd.read_csv("dataset_QA.csv")

# Clean missing values
df["question"] = df["question"].fillna("").astype(str)
df["answer"] = df["answer"].fillna("").astype(str)

# Create a combined searchable text column
df["combined"] = df["question"].str.lower().str.strip()


# -----------------------------
# 2. Vectorize Text
# -----------------------------
vectorizer = TfidfVectorizer(stop_words="english")
tfidf_matrix = vectorizer.fit_transform(df["combined"])

# =====================================================
def clean_text(text):
    text = text.replace("\n", " ")             
    text = re.sub(r"\s+", " ", text)               
    text = re.sub(r"\-+", "", text)                 
    return text.strip()

# -----------------------------
def short_note(text, max_sentences=2):
    text = clean_text(text)

    # Split into sentences
    sentences = re.split(r'(?<=[.!?])\s+', text)

    if len(sentences) <= max_sentences:
        return text

    # Return first informative sentences
    return " ".join(sentences[:max_sentences])


# 3. Retrieval Function
# -----------------------------
def get_answer(query, top_k=1):
    if not query or query.strip() == "":
        return ["Please enter a valid question."]

    # Preprocess query
    query_clean = query.lower().strip()
    query_vec = vectorizer.transform([query_clean])

    # Similarity scores
    similarity = cosine_similarity(query_vec, tfidf_matrix)[0]

    # Top match indices
    top_indices = similarity.argsort()[-top_k:][::-1]

    for idx in top_indices:
        answer_text = df.iloc[idx]["answer"]

        if answer_text.strip() == "":
            answer_text = "No answer available in the dataset."

        return answer_text


# Example query
query = "What is diabetes?"

# Get answer
results = get_answer(query)

# Print result
for i, ans in enumerate(results, 1):
    print(f"Answer {i}: {ans}")