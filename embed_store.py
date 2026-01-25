from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer("paraphrase-MiniLM-L3-v3")

def create_embeddings(chunks):
    embeddings = model.encode(chunks)
    return np.array(embeddings)
