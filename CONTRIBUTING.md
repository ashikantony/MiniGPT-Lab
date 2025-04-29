✅ Option 1: Use GitHub Actions (CI/CD Deployment)

If you're deploying from GitHub using **GitHub Actions** to Hugging Face:

🔐 Step 1: Add Hugging Face Token to GitHub Secrets

1. Go to your **GitHub repository**.
2. Click **Settings > Secrets and variables > Actions > New repository secret**.
3. Add the following:
   - **Name:** `HF_TOKEN`
   - **Value:** your Hugging Face token (from https://huggingface.co/settings/tokens)

### 🛠️ Step 2: Use It in GitHub Workflow

Inside `.github/workflows/huggingface.yml`, reference it like this:

```yaml
env:
  HF_TOKEN: ${{ secrets.HF_TOKEN }}

steps:
  - name: Login to Hugging Face CLI
    run: huggingface-cli login --token $HF_TOKEN
```

---

✅ Option 2: For Hugging Face Spaces with Git-Based Deployment

If you're pushing code directly to a **Hugging Face Space repo** (e.g., `https://huggingface.co/spaces/yourname/yourspace`):

🔐 Step 1: Login via `huggingface-cli`

```bash
huggingface-cli login
# Paste your token when prompted
```

This saves your token locally (`~/.huggingface/token`) so that you can use `git push`:

```bash
git remote add origin https://huggingface.co/spaces/yourusername/minigpt-lab
git push origin main
```

---

✅ Optional: Use `.env` File for Local Dev

If your backend code (FastAPI/Streamlit) needs the Hugging Face token at runtime:

### Create a `.env` file:

```env
HF_TOKEN=your-hugging-face-token
```

And load it using Python:

```python
from dotenv import load_dotenv
import os

load_dotenv()
hf_token = os.getenv("HF_TOKEN")
```
