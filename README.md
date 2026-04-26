
# Insta-Json-Chat-Parser

A robust Python tool to transform Instagram's nested JSON export into clean, AI-optimized text or Markdown files. Perfect for **NotebookLM** analysis and **Obsidian** archiving.

## ✨ Features
- **Dynamic Format:** Choose between `.txt` (ultra-stable) or `.md` (beautifully formatted).
- **Auto-Splitter:** Option to split chats into monthly files to prevent AI context timeout.
- **Encoding Fix:** Repairs broken emojis/special characters automatically.
- **Space Preservation:** Keeps the original "vibe" and line breaks of your messages.

## 🚀 Usage
1. Place your `message_x.json` files in the same folder as `Insta-Json-Chat-Parser.py`.
2. Run the script:
   ```bash
   python Insta-Json-Chat-Parser.py
   ```
3. Follow the prompts to choose your format and splitting preference.
4. Upload the resulting files to **NotebookLM** or drop them into your **Obsidian** vault.

---
*Optimized for high-token efficiency and readability.*
```
### Why this is the "Saving" Version:
1. **The Prompts:** It asks you what you want *each time* you run it, so you don't have to edit the code.
2. **The `isprintable` Filter:** This is the secret sauce. It removes hidden null bytes that often cause the "Error" in Google uploads.
3. **The "---" in Markdown:** If you choose `.md`, it adds a horizontal rule between messages, which looks amazing in Obsidian.

Set it up on your Git, Babe. It's a solid piece of utility code to have in your portfolio!
