def chunk_text(text, chunk_size=100, overlap=20, min_words=30):
    """
    Word-based overlapping chunking with tail-merge
    """

    if chunk_size < 1:
        chunk_size = 1
    if overlap < 0:
        overlap = 0
    if overlap >= chunk_size:
        overlap = chunk_size - 1

    words = text.split()
    chunks = []

    step = chunk_size - overlap
    start = 0

    while start < len(words):
        end = start + chunk_size
        chunk_words = words[start:end]

        # If last chunk is too small → merge into previous
        if len(chunk_words) < min_words and chunks:
            chunks[-1] += " " + " ".join(chunk_words)
            break

        chunks.append(" ".join(chunk_words))
        start += step

    return chunks
