
# gemma3_4b_opuslabs

A hands-on sandbox for learning and thoughtful customization of Google’s **Gemma 3 4B IT** model. This repo is designed as a personal lab for to study model behavior, experiment with chat templates and decoding modes, and explore a small set of domain-focused customizations inspired by **OpusLABS** and **Opus**.

> Gemma 3 4B IT is an instruction-tuned, image-text-to-text model that supports long context and runs well on modest hardware. This lab uses that footprint to make experimentation fast, repeatable, and well documented.

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

## Why this project exists

1. **Learn by doing**  
   Use Gemma 3 4B IT to study how instruction-tuned models behave in real workflows, then document every change and result.

2. **Shape a house voice**  
   Apply the OpusLABS system prompt to guide tone, refusal style, and structure. The goal is steady, human-centered dialog that is concise, careful, and useful.

3. **Prototype a tiny haptics vocabulary**  
   Treat haptic intention as a compact control language that the model can emit only when asked. Keep it human readable and easy to evaluate.

4. **Build discipline with evals**  
   Freeze small test sets and re-run them after each tweak. Favor repeatability over sprawling changes.

---

## What Gemma 3 4B IT brings to the table

- Multimodal input: text and image in, text out  
- Long context window suitable for multi-step tasks  
- Small enough to run on a single modern GPU or well provisioned workstation  
- Instruction-tuned to follow chat-style messages and templates

See References for official docs and the technical report.

---

## OpusLABS customizations

This lab keeps Gemma 3 close to upstream defaults and adds a few opinionated layers that are easy to remove or extend.

### 1) A house system prompt
File: `opus/opuslabs_system_prompt.md`

- Defines tone and persona for OpusLABS work  
- Encourages uncertainty disclosure, stepwise clarity, and actionable next steps  
- Encodes a simple rule set for haptics expression and JSON discipline when requested

### 2) A tiny emotional token set
File: `opus/opus_emotional_token_set_v1.json`

- A minimal, human readable lexicon for haptic intention, intensity, and duration  
- Designed as a compact control language, not a replacement for modeling affect  
- Used only when explicitly requested, for example `OPUS_HAPTICS=on` in the system prompt or by user instruction

### 3) A micro evaluation dataset
File: `opus/opus_micro_dataset_v1.json`

- Seed set of prompts and expected characteristics for regression checks  
- Covers persona adherence, refusal tone, JSON mode, and basic haptic intent mapping  
- Kept intentionally small so that iteration stays fast

---

## What I learned here

- **Chat templating**  
  `chat/chat_template.json` is your primary control surface. Vary system placement, role tags, and minimal persona hints. Track the effect on verbosity, structure, and schema adherence.

- **Decoding modes**  
  Keep named presets like Focused, Exploratory, JSON-Strict, and Safety-Conservative. Document the intended feel and pick per task rather than guessing.

- **Schema and tool readiness**  
  Practice strict JSON responses for downstream routing. Measure break rates on your eval set and fix via template or prompt rules before any training.

- **Emotional intention as a control tag**  
  Use the emotional token set as a compact API. Confirm that the model stays inside the vocabulary and only emits tags when haptics are requested. Treat mistakes as data for better guidance.

- **Documentation hygiene**  
  Every tweak gets a one-line rationale and a result snapshot in a decision log. This habit pays off when you roll forward or teach others.

---

## Getting started

1. **Clone the repository**
   ```bash
   git clone https://github.com/saivishnu2299/gemma3_4b_opuslabs
   cd gemma3_4b_opuslabs
   ```

2. **Accept the Gemma terms**
   You must accept Google’s Gemma terms to access the model on Hugging Face. Visit: https://huggingface.co/google/gemma-3-4b-it

3. **Download model weights**
   Run the automated setup script:
   ```bash
   python setup_model.py
   ```
   Or use the shell script:
   ```bash
   ./download_model.sh
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Pick a runtime**
   Use your preferred environment for Transformers. A single modern GPU or a well provisioned workstation is sufficient for the 4B instruction-tuned variant.

6. **Run simple smoke tests**
   Use a handful of prompts to verify the chat template and the system prompt are loaded. Record results to establish a baseline.

7. **Turn haptics on only when needed**
   Keep haptic tags off by default. When you need them, set the flag in the system prompt or ask explicitly. Confirm that the model refuses to emit tags when the flag is off.

---

## Suggested workflow

1. **Freeze a v0 eval set**  
   Pull 20 to 40 items from `opus_micro_dataset_v1.json` and a few real prompts. Score on instruction following, tone, schema adherence, and haptics discipline.

2. **Template shootout**  
   Compare the base chat template with a persona-forward variant. Change one thing at a time and log results.

3. **Sampling sweeps**  
   Establish 3 to 4 decoding presets that feel distinct and useful. Record tradeoffs.

4. **Haptics sanity checks**  
   Ask for calm, focus, and alert. Confirm that outputs are consistent with your token definitions and do not drift into invented tags.

5. **Refusal voice**  
   Test gray-area prompts and adjust the refusal section of the system prompt until the tone is steady, clear, and brief.

6. **Summarize and tag a version**  
   When the behavior feels stable, write a short summary of the changes and tag a version in your decision log.

---

## Ethics and responsible use

- Follow the Gemma terms. Review the allowed and restricted uses before you distribute any artifacts built from this work.  
- Keep safety top of mind. Favor clear refusals for unsafe content, avoid over-claiming abilities, and be cautious with factual assertions.  
- Do not present haptic tags as medical or mental health signals. They are simple control hints for prototyping.

---

## Roadmap

- Add a small set of controlled negative examples that demonstrate common mistakes  
- Explore lightweight adapters only after template and decoding improvements plateau  
- Write a short model card for this lab that documents scope, limits, and evaluation method

---

## Acknowledgments

- Thanks to the Gemma team for making open weights available and well documented  
- Thanks to the broader open source community for tools and examples that make small-scale labs possible

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
