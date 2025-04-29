# 📁 File: backend/trainer.py

from transformers import AutoModelForCausalLM, AutoTokenizer, Trainer, TrainingArguments
import torch
import json

MODEL_NAME = "sshleifer/tiny-gpt2"

def train_model(data_dir):
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)

    with open(f"{data_dir}/train.json", "r", encoding='utf-8') as f:
        data = json.load(f)

    inputs = tokenizer([item["prompt"] for item in data], return_tensors="pt", padding=True, truncation=True)
    labels = tokenizer([item["response"] for item in data], return_tensors="pt", padding=True, truncation=True).input_ids

    class SimpleDataset(torch.utils.data.Dataset):
        def __init__(self, encodings, labels):
            self.encodings = encodings
            self.labels = labels

        def __getitem__(self, idx):
            item = {key: torch.tensor(val[idx]) for key, val in self.encodings.items()}
            item["labels"] = torch.tensor(self.labels[idx])
            return item

        def __len__(self):
            return len(self.labels)

    dataset = SimpleDataset(inputs, labels)

    training_args = TrainingArguments(
        output_dir="./results",
        num_train_epochs=3,
        per_device_train_batch_size=2,
        warmup_steps=10,
        weight_decay=0.01,
        logging_dir="./logs",
        logging_steps=5,
        save_strategy="epoch",
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=dataset,
    )

    trainer.train()
    return model
