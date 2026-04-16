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