#!/bin/bash
# 3D Printing Training Agent — Linux/macOS Setup
# Run: chmod +x setup.sh && ./setup.sh

echo "============================================"
echo "Setting up: 3D Printing Training Agent"
echo "============================================"

if ! command -v python3 &>/dev/null; then
    echo "ERROR: python3 not found. Install Python 3.10+ from https://python.org"
    exit 1
fi
echo "[OK] $(python3 --version)"

if [ ! -d ".venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv .venv
    echo "[OK] Virtual environment created"
else
    echo "[OK] Virtual environment already exists"
fi

source .venv/bin/activate
pip install --upgrade pip --quiet
pip install -r requirements.txt --quiet
echo "[OK] Dependencies installed"

if [ ! -f ".env" ]; then
    cp .env.example .env
    echo "[OK] Created .env — fill in your API keys"
else
    echo "[OK] .env already exists"
fi

mkdir -p .tmp
echo "[OK] .tmp directory ready"

echo ""
echo "Setup complete!"
echo "Next steps:"
echo "  1. Edit .env and add your YOUTUBE_API_KEY"
echo "  2. Run: python execution/generate_curriculum_docs.py --all"
echo "  3. Open in VS Code and chat with the agent"
