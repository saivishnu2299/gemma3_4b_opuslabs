#!/bin/bash
# Download script for Gemma 3 4B IT model weights

echo "🚀 Setting up Gemma 3 4B OpusLABS Lab"
echo "======================================"

# Check if weights already exist
if [ -d "weights" ] && [ -n "$(find weights -name "model-*.safetensors" 2>/dev/null)" ]; then
    echo "✅ Model weights already present!"
    echo "📁 Found model files in weights/"
    exit 0
fi

echo "🔄 Downloading Gemma 3 4B IT model weights..."
echo "📝 You must accept the Gemma terms of use at: https://huggingface.co/google/gemma-3-4b-it"
echo "💡 Make sure you're logged in with: huggingface-cli login"
echo ""

# Create weights directory
mkdir -p weights

# Try to download using huggingface-cli
if command -v huggingface-cli &> /dev/null; then
    echo "📥 Using huggingface-cli to download model..."
    if huggingface-cli download google/gemma-3-4b-it --local-dir weights --local-dir-use-symlinks false; then
        echo "✅ Model weights downloaded successfully!"
        echo "📁 Files saved to: weights/"
        exit 0
    else
        echo "❌ Failed to download with huggingface-cli"
    fi
else
    echo "⚠️  huggingface-cli not found"
fi

echo ""
echo "🔧 Manual setup instructions:"
echo "1. Accept Gemma terms at: https://huggingface.co/google/gemma-3-4b-it"
echo "2. Install huggingface-hub: pip install huggingface_hub"
echo "3. Login: huggingface-cli login"
echo "4. Download: huggingface-cli download google/gemma-3-4b-it --local-dir weights"
echo ""
echo "Or run: python setup_model.py"
