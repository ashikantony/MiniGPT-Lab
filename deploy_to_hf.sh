#!/bin/bash

# Exit if any command fails
set -e

# ------------------- USER CONFIG --------------------
HF_USERNAME="ashikantony13"                    # 🔁 Replace this
SPACE_NAME="minigpt-lab"                          # 🔁 Replace this
TOKEN="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"     # 🔁 Replace this
REPO_URL="https://huggingface.co/spaces/${HF_USERNAME}/${SPACE_NAME}"
TARGET_DIR="hf_space_temp"

# ----------------- LOGIN TO HF ----------------------
echo "🔐 Logging into Hugging Face..."
pip install -q huggingface_hub
huggingface-cli login --token $TOKEN

# ----------------- CREATE SPACE (optional) ----------
echo "🆕 Creating space if not exists..."
huggingface-cli repo create $SPACE_NAME --type=space --sdk=streamlit --private || echo "✅ Space already exists."

# ----------------- CLONE AND COPY -------------------
echo "📁 Cloning existing repo or initializing..."
rm -rf $TARGET_DIR
git clone $REPO_URL $TARGET_DIR

echo "📦 Copying project files..."
rsync -av --exclude '.git' --exclude $TARGET_DIR ./ $TARGET_DIR/

# ----------------- COMMIT AND PUSH ------------------
cd $TARGET_DIR
git config user.email "ashikantony23@gmail.com"
git config user.name "ashikantony"
git add .
git commit -m "🚀 Auto-deploy: MiniGPT Lab"
git push origin main

echo "✅ Successfully deployed to Hugging Face!"
echo "🌍 Visit your Space: https://huggingface.co/spaces/${HF_USERNAME}/${SPACE_NAME}"
