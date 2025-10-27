#!/usr/bin/env python3
"""
Setup script to download Gemma 3 4B IT model weights.

This script downloads the required model files from Hugging Face after you accept the Gemma terms.
"""

import os
import sys
from pathlib import Path

def check_huggingface_hub():
    """Check if huggingface_hub is installed."""
    try:
        import huggingface_hub
        return True
    except ImportError:
        print("❌ huggingface_hub not found. Installing...")
        import subprocess
        subprocess.check_call([sys.executable, "-m", "pip", "install", "huggingface_hub"])
        return True

def download_model():
    """Download the Gemma 3 4B IT model weights."""
    try:
        from huggingface_hub import snapshot_download
    except ImportError:
        print("❌ Failed to import huggingface_hub")
        return False

    print("🔄 Downloading Gemma 3 4B IT model weights...")
    print("📝 You must accept the Gemma terms of use at: https://huggingface.co/google/gemma-3-4b-it")
    print("💡 Make sure you're logged in with: huggingface-cli login")
    print()

    try:
        # Download to weights directory
        weights_dir = Path("weights")
        weights_dir.mkdir(exist_ok=True)

        snapshot_download(
            repo_id="google/gemma-3-4b-it",
            local_dir=str(weights_dir),
            local_dir_use_symlinks=False
        )

        print("✅ Model weights downloaded successfully!")
        print(f"📁 Files saved to: {weights_dir}")
        return True

    except Exception as e:
        print(f"❌ Failed to download model: {e}")
        print()
        print("🔧 Manual setup instructions:")
        print("1. Accept Gemma terms at: https://huggingface.co/google/gemma-3-4b-it")
        print("2. Run: huggingface-cli login")
        print("3. Run: huggingface-cli download google/gemma-3-4b-it --local-dir weights")
        return False

def main():
    """Main setup function."""
    print("🚀 Setting up Gemma 3 4B OpusLABS Lab")
    print("=" * 40)

    # Check if model already exists
    weights_dir = Path("weights")
    if weights_dir.exists() and any(weights_dir.iterdir()):
        model_files = list(weights_dir.glob("model-*.safetensors"))
        if model_files:
            print("✅ Model weights already present!")
            print(f"📁 Found {len(model_files)} model files in weights/")
            return True

    # Check dependencies and download
    if check_huggingface_hub():
        return download_model()
    else:
        print("❌ Failed to setup dependencies")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
