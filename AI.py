from colorama import Fore, Style, init
import time
import os
import random
import sys

init(autoreset=True)

def clear():
    print('\n'*50)
def typing(text, color):
    for c in text:
        print(color + c, end="")
        sys.stdout.flush()
        time.sleep(0.04)
    print()

def visualizer_bar():
    columns = 8  # số cột
    max_height = 8
    print()
    for h in range(max_height, 0, -1):
        line = "  "
        for _ in range(columns):
            if random.randint(1, max_height) >= h:
                line += Fore.GREEN + "▇ "
            else:
                line += "  "
        print(line)
    print()


def progress(current, total, length=30):
    filled = int(length * (current / total))
    bar = "█" * filled + "░" * (length - filled)
    return f"[{bar}]"

def loading_animation():
    frames = ["⠋","⠙","⠹","⠸","⠼","⠴","⠦","⠧","⠇","⠏"]
    for _ in range(15):
        for f in frames:
            print(Fore.YELLOW + "Đang tải bài hát..." + f, end="\r")
            time.sleep(0.07)
    print()

def music_player():
    song_title = "Ngày Này Năm Ấy"
    artist = "Việt Anh"

    lyrics = [
        ("Dành ra đi để chờ...", Fore.CYAN, 1.7),
        ("Câu chuyện mình không đau...", Fore.BLUE, 3.1),
        ("Em đã xa anh mất rồi người ơi...", Fore.GREEN, 3.0),
        ("Lời hứa gió bay hết rồi người ơi...", Fore.MAGENTA, 3.0),
        ("Ta đã đến bên nhau để day nhau", Fore.YELLOW, 2.8),
        ("Yêu một ai thật chân thành...", Fore.RED, 2.3),
        ("Nhưng sự chân thành dần nguội đến sau", Fore.YELLOW, 2.6),
        ("Thời gian cũng sẽ chưa lành anh thôi...", Fore.CYAN, 2.9),
        ("Người đã buông tay rồi...", Fore.GREEN, 2.0),
        ("Lòng chơi vơi...", Fore.YELLOW, 3.2),
    ]

    clear()
    print(Fore.CYAN + "~~~ vh.slow 🎵\n")
    loading_animation()

    print(Fore.CYAN + f"\n🎵 {song_title}")
    print(Fore.BLUE + f"👤 {artist}\n")

    total = sum(line[2] for line in lyrics)
    current = 0

    for text, color, delay in lyrics:
        typing(text, color)
        # Visualizer loop
        t = 0
        iv = 0.12
        while t < delay:
            visualizer_bar()
            current_time = f"{int(current//60):02d}:{int(current%60):02d}"
            total_time = f"{int(total//60):02d}:{int(total%60):02d}"
            print(
                Fore.CYAN
                + progress(current, total)
                + f"  {current_time}/{total_time}",
                end="\r"
            )
            time.sleep(iv)
            t += iv
            current += iv
        print()
        print()

    print(Fore.GREEN + "\nKết thúc bài hát ♪")
    time.sleep(1)

music_player()
