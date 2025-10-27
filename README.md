
# gemma3_4b_opuslabs

My personal laboratory for exploring and customizing Google's **Gemma 3 4B IT** model. This is where I experiment with model behavior, tinker with chat templates, and build small but meaningful customizations inspired by the **OpusLABS** philosophy.

> Gemma 3 4B IT is perfect for this kind of hands-on work - it's instruction-tuned, handles multimodal input, and runs comfortably on modest hardware. That makes iteration fast and documentation straightforward.

---

## Contents

- **README.md** ← you are here
- **setup_model.py** - automated model download script
- **download_model.sh** - shell script for model download
- **requirements.txt** - Python dependencies
- **LICENSE** - Apache 2.0 + Gemma terms
- **Gemma3Report.pdf** - reference paper for Gemma 3

### configs/ - model configuration files
- config.json
- generation_config.json
- preprocessor_config.json
- processor_config.json

### tokenizer/ - tokenizer and vocabulary files
- **tokenizer.json** - main tokenizer (32MB - LFS)
- tokenizer_config.json
- **tokenizer.model** - sentencepiece model (4.5MB - LFS)
- special_tokens_map.json
- added_tokens.json

### chat/ - chat template system
- **chat_template.json** - message formatting control surface

### weights/ - model weights (download via setup script)
- **[empty - run setup script to download 8GB of model files]**

### opus/ - OpusLABS customizations
- **opuslabs_system_prompt.md** - house style and safety rules
- **opus_emotional_token_set_v1.json** - tiny haptics-aware lexicon (49 tokens)
- **opus_micro_dataset_v1.json** - small eval seed set for regression checks

---

## What I'm building here

I started this lab with a few clear goals:

1. **Learn by experimenting**  
   Get my hands dirty with Gemma 3 to understand how instruction-tuned models actually behave in practice, not just in theory.

2. **Craft a consistent voice**  
   The OpusLABS system prompt helps me create responses that feel steady and human-centered - concise, thoughtful, and genuinely useful.

3. **Explore haptic feedback**  
   I'm fascinated by how we might translate emotional context into physical feedback. The token set here is my attempt at a minimal, human-readable control language.

4. **Stay disciplined**  
   Small evaluation sets keep me honest. I run them after every change to make sure I'm actually improving things, not just changing them.

---

## Why I chose Gemma 3 4B

This particular model is perfect for what I'm trying to do:

- **Multimodal by default** - handles both text and images as input, which opens up interesting experimentation possibilities
- **Long context window** - great for the kind of thoughtful, multi-step reasoning I want to explore
- **Hardware friendly** - runs comfortably on a single GPU, so I can iterate quickly without massive compute requirements
- **Already instruction-tuned** - comes ready to follow chat templates and system prompts, which saves me from doing the fine-tuning myself

The official docs and technical reports are in the References section below.

---

## My customizations

I'm keeping most of Gemma 3's defaults intact and just layering on a few thoughtful additions that I can easily modify or remove.

### 1) The Opus voice
File: `opus/opuslabs_system_prompt.md`

This is my attempt at creating a consistent, helpful assistant personality. It emphasizes:
- Clear communication without overconfidence
- Step-by-step thinking when helpful
- Practical next steps over abstract advice
- Safe handling of uncertain or sensitive topics

### 2) Haptic feedback vocabulary
File: `opus/opus_emotional_token_set_v1.json`

I'm experimenting with how language models might communicate emotional context through physical feedback. This tiny token set includes:
- Emotional states (calm, focus, alert, etc.)
- Intensity levels and timing controls
- Pattern definitions for different kinds of feedback
- Only activated when explicitly requested - safety first

### 3) Reality checks
File: `opus/opus_micro_dataset_v1.json`

A small set of test prompts that help me verify:
- The assistant maintains consistent personality
- Refusals are clear but not harsh
- Haptic tokens only appear when appropriate
- Everything still works after I make changes

---

## What I've learned so far

This has been an incredible learning experience. Here are the key insights I've picked up:

- **Chat templates are everything**  
  The `chat_template.json` is the main control surface. Small changes to system message placement, role tags, or persona hints have huge effects on how the model behaves. I've learned to track verbosity, structure, and adherence carefully.

- **Sampling strategies matter**  
  Having named presets (Focused, Exploratory, JSON-Strict, Safety-Conservative) prevents decision fatigue. Each one feels distinct and serves different use cases. I document the tradeoffs and pick deliberately rather than guessing.

- **Schema discipline before scaling**  
  Getting strict JSON responses working reliably is crucial for downstream integration. I've learned to measure break rates on my small eval set and fix issues through template and prompt design before considering any training.

- **Haptic tokens as a design problem**  
  The emotional token set works best as a compact API. I've learned that the model needs clear boundaries - it should stay within the defined vocabulary and only emit haptic tags when explicitly requested. Every mistake becomes data for better guidance.

- **Documentation as muscle memory**  
  Writing a one-line rationale for every change and keeping result snapshots has become second nature. It's already paying off when I need to roll back changes or explain my decisions to others.

---

## Getting started

Here's how to get up and running with my customizations:

1. **Clone and setup**
   ```bash
   git clone https://github.com/saivishnu2299/gemma3_4b_opuslabs
   cd gemma3_4b_opuslabs
   ```

2. **Accept the Gemma terms**
   You need to accept Google's Gemma terms to download the model. Visit: https://huggingface.co/google/gemma-3-4b-it

3. **Download the model**
   I made this easy with automated scripts:
   ```bash
   python setup_model.py    # Python script (recommended)
   ```
   Or if you prefer shell:
   ```bash
   ./download_model.sh      # Shell script version
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Choose your environment**
   This runs comfortably on a single modern GPU or a well-equipped workstation. I use it on my development machine without issues.

6. **Test that it works**
   Try a few prompts to verify the chat template and Opus personality are loaded correctly. This establishes your baseline for future changes.

7. **Haptics are opt-in**
   The emotional feedback system stays off by default. When you want to experiment with it, set `OPUS_HAPTICS=on` in the system prompt or ask explicitly. The model should refuse to emit haptic tokens when the flag is off.

---

## Ethics and responsible use

I'm very conscious about using this technology responsibly:

- **Always follow the Gemma terms** - I carefully review the allowed and restricted uses before sharing anything built from this work
- **Safety first** - I prioritize clear, kind refusals for unsafe content, avoid making unsubstantiated claims about capabilities, and I'm careful about factual assertions
- **Haptics aren't medical** - The emotional tokens are just simple control hints for prototyping - never for medical or mental health applications

---

## What's next

A few things I'm planning to explore:

- **Negative examples** - Add controlled examples of common mistakes to help understand where things go wrong
- **Lightweight fine-tuning** - Only after I max out what I can do with templates and decoding strategies
- **Model card** - Write up a clear summary of what this customized version can and cannot do

---

## Acknowledgments

This work builds on the generosity of others:

- **Huge thanks to the Gemma team** at Google for making these powerful models available as open weights with excellent documentation - it's made this kind of hands-on learning possible

- **Grateful to the open source community** for all the tools, examples, and shared knowledge that make independent research accessible to individuals like me

---

## References

- Gemma 3 4B IT on Hugging Face  
  https://huggingface.co/google/gemma-3-4b-it

- Gemma 3 model overview and model card  
  https://ai.google.dev/gemma/docs/core  
  https://ai.google.dev/gemma/docs/core/model_card_3

- Gemma 3 technical report (PDF)  
  https://storage.googleapis.com/deepmind-media/gemma/Gemma3Report.pdf  
  https://arxiv.org/abs/2503.19786

- Google blog announcements and developer guide  
  https://blog.google/technology/developers/gemma-3/  
  https://developers.googleblog.com/en/introducing-gemma3/

- Gemma terms of use  
  https://ai.google.dev/terms/gemma
