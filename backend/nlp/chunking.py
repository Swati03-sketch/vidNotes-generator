def chunk_sen(sentences: list, chunk_size: int = 5):
    """Chunk sentences into manageable groups."""
    chunks = [sentences[i:i+chunk_size] for i in range(0, len(sentences), chunk_size)]
    return chunks               # output in list format 
