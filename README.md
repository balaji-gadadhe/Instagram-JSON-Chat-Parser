
# Instagram JSON Chat Parser for NotebookLM & Obsidian

A Python-based utility to convert messy Instagram JSON data exports into clean, structured Markdown files. This project is specifically optimized for analysis in **NotebookLM**, stripping out metadata and fixing character encoding (emojis) to keep your context window clean and efficient.

## 🚀 Features
- **Auto-Merging:** Combines multiple `message_x.json` files into a single chronological document.
- **Emoji Fix:** Repairs Instagram's unique `latin1` encoding so emojis and special characters display correctly.
- **Noise Reduction:** Filters out system messages (calls, link shares, attachments) to focus on the actual conversation.
- **AI-Ready:** Uses Markdown bolding and timestamps for better entity recognition in NotebookLM.

## 📁 Setup & Usage

### 1. Prepare your Data
1. Export your Instagram data in **JSON** format.
2. Navigate to `your_activity/messages/inbox/`.
3. Locate the folder for the specific chat you want to analyze.
4. Copy all `message_1.json`, `message_2.json`, etc., files into a new folder on your computer.

### 2. The Script (`cleaner.py`)
Create a file named `cleaner.py` in the same folder and paste the following code:

```python
import json
import datetime
import os
import glob

def clean_all_chats():
    # Find all message_*.json files
    json_files = glob.glob("message_*.json")
    
    # Sort files chronologically (Instagram numbers them 1=latest)
    json_files.sort(key=lambda x: int(x.split('_')[1].split('.')[0]), reverse=True)

    output_filename = "Our_Insta_Story.md"
    all_messages = []

    print(f"Found {len(json_files)} files. Starting conversion...")

    for file_path in json_files:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            messages = data.get('messages', [])
            all_messages.extend(messages)

    # Sort everything by timestamp
    all_messages.sort(key=lambda x: x.get('timestamp_ms', 0))

    with open(output_filename, 'w', encoding='utf-8') as out:
        out.write("# Full Chat History Analysis\\n\\n")
        
        for msg in all_messages:
            sender = msg.get('sender_name', 'Unknown')
            content = msg.get('content', '')
            
            # Fix Instagram's encoding for emojis
            if content:
                try:
                    content = content.encode('latin1').decode('utf8')
                except (UnicodeEncodeError, UnicodeDecodeError):
                    pass
            
            timestamp = msg.get('timestamp_ms', 0) / 1000
            date_str = datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M')

            if content and "sent an attachment" not in content and "shared a link" not in content:
                out.write(f"**{sender}**: {content} *({date_str})*\\n\\n")

    print(f"Success! '{output_filename}' is ready.")

if __name__ == '__main__':
    clean_all_chats()
```

### 3. Run the Script
Open your terminal in the folder and run:
```bash
python cleaner.py
```

## 🧠 NotebookLM & Obsidian Integration

- **NotebookLM:** Upload the generated `Our_Insta_Story.md`. It will be significantly more token-efficient than the 1000-page PDFs.
- **Obsidian:** Drag the file into your vault. You can now link specific dates to your Daily Notes or use it for relationship archiving.

---
*Created for personal knowledge management and digital archiving.*
