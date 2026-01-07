import tiktoken

# Chunk text into tokens, leaves buffer under model max context. No overlap.
def chunk_text(text, max_tokens=7000, model="llama3.1-8b"):
    """
    Splits text into token-based chunks.
    Leaves buffer under model max context.
    """
    encoding = tiktoken.get_encoding("cl100k_base")
    tokens = encoding.encode(text)
    chunks = []
    for i in range(0, len(tokens), max_tokens):
        chunk_tokens = tokens[i:i + max_tokens]
        chunk_text = encoding.decode(chunk_tokens)
        chunks.append(chunk_text)
    return chunks






# COMMENTED OUT NEW CODE FOR FUTURE REFERENCE

# def chunk_text(
#     text: str,
#     max_tokens: int = 7000,
#     overlap: int = 500,
#     min_overlap_threshold: int = 5000
# ):
#     """
#     Splits text into token-based chunks.
    
#     - Uses overlap for long transcripts
#     - Skips overlap if token length < min_overlap_threshold
#     - Returns list of text chunks
#     """
#     encoding = tiktoken.get_encoding("cl100k_base")
#     tokens = encoding.encode(text)

#     # Short transcript → single chunk, no overlap
#     if len(tokens) < min_overlap_threshold:
#         return [text]

#     chunks = []
#     start = 0
#     step = max_tokens - overlap

#     while start < len(tokens):
#         end = start + max_tokens
#         chunk_tokens = tokens[start:end]
#         chunk_text = encoding.decode(chunk_tokens)
#         chunks.append(chunk_text)
#         start += step

#     return chunks

# def dedupe_actions(action_items):
#     """
#     Removes duplicate action items based on task text.
#     """
#     seen = set()
#     deduped = []
#
#     for item in action_items:
#         task_key = item["task"].strip().lower()
#         if task_key not in seen:
#             seen.add(task_key)
#             deduped.append(item)
#
#     return deduped