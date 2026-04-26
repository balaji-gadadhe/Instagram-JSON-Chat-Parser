
# Insta-Json-Chat-Parser 🚀

A high-performance Python utility designed to transform fragmented Instagram JSON exports into clean, structured datasets. Optimized specifically for **NotebookLM** context windows and **Obsidian** Personal Knowledge Management (PKM) workflows.

## 🌟 Why This Exists
Instagram's "Download Your Data" exports are notoriously messy—split across dozens of JSON files with broken emoji encoding and redundant metadata. This tool solves the "2000-page PDF" problem by converting raw data into a dense, AI-readable format that doesn't crash NotebookLM or clutter your Obsidian vault.

## ✨ Key Features
- **📦 Intelligent Merging:** Automatically detects and chronologically merges multiple `message_x.json` files.
- **🛠️ Encoding Repair:** Fixes Instagram's `latin1` encoding bug, restoring emojis and special characters to their proper UTF-8 state.
- **🧹 Zero-Noise Output:** Strips out system messages (reactions, link shares, call logs) to maximize AI token efficiency.
- **📅 Dynamic Splitting:** Optional monthly auto-splitting to bypass NotebookLM's source file limits.
- **🎨 Multi-Format Support:** - **.txt:** For maximum stability and ultra-low token usage.
  - **.md:** For beautiful Obsidian rendering with horizontal separators.

## 🚀 Getting Started

### 1. Setup
1. Export your Instagram data in **JSON** format.
2. Locate the specific chat folder: `your_activity/messages/inbox/[chat_name]`.
3. Move the `message_x.json` files and `Insta-Json-Chat-Parser.py` into a single directory.

### 2. Execution
Run the script via your terminal:

```bash
python Insta-Json-Chat-Parser.py
````

### 3. Usage

Follow the interactive CLI prompts to select your preferred format and splitting logic.

## 🧠 Technical Deep-Dive

- **Interactive CLI:** No hardcoding required; the script asks for preferences on every run.
- **Sanitization:** Implements an `isprintable` filter to remove hidden null bytes and control characters that frequently trigger upload errors in Google Drive and NotebookLM.    
- **Vibe Preservation:** Unlike standard parsers, this preserves internal line breaks within messages, ensuring the original tone of the conversation remains intact.
    
---

_Developed for digital archiving and relationship analysis. Optimized for the INFJ "Old Soul" workflow._
