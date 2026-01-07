from dotenv import load_dotenv
load_dotenv()

import os
import json
from cerebras.cloud.sdk import Cerebras
from utils.tokenize import chunk_text
from utils.merge_json import merge_json_arrays
from utils.validate_json import is_valid_action_item

"""
extract_actions.py

This script takes a meeting transcript, splits it into manageable chunks,
and sends each chunk to a Cerebras-hosted LLaMA 3.1-8b model to extract
explicit, work-related action items in JSON format. 

The script then:
- merges chunk outputs
- validates each item against a strict schema (task, owner, due_date)
- prints a final list of clean, validated action items

It uses environment variables to securely store the Cerebras API key 
and supports token-based chunking to handle long transcripts safely.
"""


client = Cerebras(api_key=os.environ.get("CEREBRAS_API_KEY"))

with open("prompts/textextraction_prompt.txt") as f:
    SYSTEM_PROMPT = f.read()

with open("data/ex_transcript_action.txt") as f:
    transcript = f.read()

# --- chunk transcript ---
chunks = chunk_text(transcript)

json_chunks = []

for idx, chunk in enumerate(chunks):
    print(f"🔹 Processing chunk {idx + 1}/{len(chunks)}")

    response = client.chat.completions.create(
        model="llama3.1-8b",
        stream=False,
        temperature=0.0,
        max_completion_tokens=512,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": chunk}
        ]
    )

    json_chunks.append(response.choices[0].message.content)

# --- merge + validate ---
merged_items = merge_json_arrays(json_chunks)
validated_items = [
    item for item in merged_items if is_valid_action_item(item)
]

print("\nFINAL ACTION ITEMS:")
print(json.dumps(validated_items, indent=2))
