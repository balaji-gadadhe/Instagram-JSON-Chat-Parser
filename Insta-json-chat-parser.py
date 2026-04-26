import json
import datetime
import os
import glob
import re

def get_input_choice(prompt, options):
    while True:
        choice = input(prompt).lower().strip()
        if choice in options:
            return choice
        print(f"Invalid choice. Please pick from: {options}")

def parse_insta_chats():
    # 1. Setup & File Discovery
    json_files = glob.glob("message_*.json")
    if not json_files:
        print("No message_*.json files found! Make sure they are in this folder.")
        return

    # User Preferences
    file_ext = get_input_choice("Choose output format (txt/md): ", ['txt', 'md'])
    split_logic = get_input_choice("Split by Month or keep as One file? (month/one): ", ['month', 'one'])

    # Sort files chronologically (Instagram numbers them latest-first)
    json_files.sort(key=lambda x: int(re.search(r'message_(\d+)', x).group(1)), reverse=True)

    all_messages = []
    print(f"Reading {len(json_files)} files...")

    for file_path in json_files:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            all_messages.extend(data.get('messages', []))

    # Sort all messages by timestamp
    all_messages.sort(key=lambda x: x.get('timestamp_ms', 0))

    # 2. Processing & Writing
    print("Parsing and cleaning data...")
    
    current_file_key = None
    file_handle = None

    for msg in all_messages:
        sender = msg.get('sender_name', 'Unknown')
        content = msg.get('content', '')
        
        # Filter system noise
        if not content or any(x in content for x in ["sent an attachment", "shared a link", "started a video call"]):
            continue

        try:
            # Fix Instagram's latin1 encoding bug
            content = content.encode('latin1').decode('utf8')
            # Remove non-printable junk but keep newlines/tabs
            content = "".join(char for char in content if char.isprintable() or char in "\n\r\t")
        except:
            pass

        ts = msg.get('timestamp_ms', 0) / 1000
        dt = datetime.datetime.fromtimestamp(ts)
        date_header = dt.strftime('%y-%m-%d %H:%M')
        month_key = dt.strftime('%Y-%m')

        # Logic for splitting or single file
        if split_logic == 'month':
            if month_key != current_file_key:
                if file_handle: file_handle.close()
                current_file_key = month_key
                filename = f"Chat_{month_key}.{file_ext}"
                file_handle = open(filename, 'w', encoding='utf-8')
                print(f"Creating {filename}...")
        else:
            if not file_handle:
                filename = f"Full_Chat_History.{file_ext}"
                file_handle = open(filename, 'w', encoding='utf-8')
                print(f"Creating {filename}...")

        # Write formatting
        if file_ext == 'md':
            file_handle.write(f"### {sender} *({date_header})*\n{content}\n\n")
        else:
            file_handle.write(f"[{date_header}] {sender}:\n{content}\n\n")

    if file_handle:
        file_handle.close()
    
    print("\n✅ Success! Your chats are ready for NotebookLM and Obsidian.")

if __name__ == "__main__":
    parse_insta_chats()