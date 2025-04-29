#!/bin/bash
# 📁 File: deploy_to_hf.sh

echo "🚀 Deploying to Hugging Face Spaces..."

# Login (only needed once)
huggingface-cli login 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

# Create space (only needed once)
# huggingface-cli repo create mini-gpt-lab --type=space --sdk=streamlit --private

# Upload all files
huggingface-cli upload mini-gpt-lab . --repo-type=space --commit-message "Deploy MiniGPT Lab"

echo "✅ Deployed Successfully!"
