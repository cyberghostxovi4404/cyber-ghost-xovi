#!/usr/bin/env python3
import os
import sys

# কনফিগারেশন
hosts_path = "/etc/hosts"
redirect = "127.0.0.1"

# ANSI Color Codes
G = "\033[1;32m"  # Green
R = "\033[1;31m"  # Red
W = "\033[1;37m"  # White
X = "\033[0m"     # Reset

def banner():
    os.system('clear' if os.name == 'posix' else 'cls')
    print(f"""{G}
╔══════════════════════════════════════════════════════════╗
║     ░█▀▀░█▀█░█▀▄░█▀▀░█░█░░░█▀▀░█░█░█▀█░█▀▄░█▀▀░█▀▀     ║
║     ░█░░░█░█░█░█░█▀▀░▄▀▄░░░█▀▀░█▀█░█░█░█░█░█▀▀░▀▀█     ║
║     ░▀▀▀░▀▀▀░▀▀░░▀▀▀░▀░▀░░░▀▀▀░▀░▀░▀▀▀░▀▀░░▀▀▀░▀▀▀     ║
║                                                          ║
║                  CYBER GHOST X OVI                       ║
║                         v2.0                             ║
║                    Created by Ovi                        ║
╚══════════════════════════════════════════════════════════╝
{W}
    [!] ------------------------ [!]{X}
    """)

def block_website():
    if os.geteuid() != 0:
        print(f"\n{R}[!] Error: {W}Root পারমিশন বা 'sudo' প্রয়োজন।{X}")
        return

    website = input(f"\n{G}[?]{W} যে সাইটটি ব্লক করতে চান (যেমন: facebook.com): {X}")
    if not website or "." not in website:
        print(f"{R}[!] Error: {W}সঠিক ডোমেইন নাম দিন।{X}")
        return

    try:
        with open(hosts_path, 'a') as file:
            file.write(f"\n# blocked by CYBER GHOST X OVI\n")
            file.write(f"{redirect} {website}\n")
            file.write(f"{redirect} www.{website}\n")
        print(f"\n{G}[✓] {W}{website} সফলভাবে ব্লক করা হয়েছে!{X}")
    except PermissionError:
        print(f"\n{R}[!] Error: {W}সিস্টেম ফাইল রাইট করা যায়নি।{X}")
    except Exception as e:
        print(f"\n{R}[!] ভুল হয়েছে: {e}{X}")

def main():
    banner()
    print(f"{G}১.{W} ওয়েবসাইট ব্লক করুন{X}")
    print(f"{G}২.{W} এক্সিট{X}")
    choice = input(f"\n{G}[+]{W} অপশন সিলেক্ট করুন: {X}")

    if choice == '1':
        block_website()
    else:
        print(f"\n{G}[!] {W}বিদায়!{X}")
        sys.exit()

if __name__ == "__main__":
    main()
