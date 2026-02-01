def chunk_text(text, chunk_size=100, overlap=20):
    """
    Split text into overlapping chunks based on WORD count
    """

    if chunk_size < 1:
        chunk_size = 1
    if overlap < 0:
        overlap = 0
    if overlap >= chunk_size:
        overlap = chunk_size - 1

    words = text.split()   # split by whitespace
    chunks = []
    start = 0

    while start < len(words):
        end = start + chunk_size
        chunk_words = words[start:end]
        chunk = " ".join(chunk_words)
        chunks.append(chunk)
        start = end - overlap

    return chunks
