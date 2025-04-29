import os
import json

def process_dataset(dataset_dir):
    os.makedirs("data/processed", exist_ok=True)
    combined_texts = []
    
    for filename in os.listdir(dataset_dir):
        if filename.endswith(".txt"):
            with open(os.path.join(dataset_dir, filename), 'r', encoding='utf-8') as f:
                combined_texts.append(f.read())

    data = [{"prompt": text, "response": text} for text in combined_texts]
    with open("data/processed/train.json", "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
