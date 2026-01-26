# embed_store.py   ← full corrected version
from fastembed import TextEmbedding
import numpy as np

# Choose a good lightweight model (very similar quality to all-MiniLM-L6-v2)
model = TextEmbedding(model_name="BAAI/bge-small-en-v1.5")  
# Alternatives: 
#   "sentence-transformers/all-MiniLM-L6-v2"  (quantized version works too)
#   "nomic-ai/nomic-embed-text-v1.5"
#   "mixedbread-ai/mxbai-embed-large-v1"     (strong but a bit heavier)

def create_embeddings(texts: list[str]) -> np.ndarray:
    """
    FastEmbed .embed() returns a generator → convert to numpy array
    Use batch_size to control memory (16–64 is usually good)
    """
    embeddings_gen = model.embed(
        texts,
        batch_size=32,          # adjust based on your RAM
        parallel=4              # optional: use multiple CPU cores
    )
    return np.array(list(embeddings_gen))  # or np.vstack(list(embeddings_gen)) if needed