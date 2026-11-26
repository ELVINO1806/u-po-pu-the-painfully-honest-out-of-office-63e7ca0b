
import os

TEXT = "I am away this week recharging, by which I mean staring at the ceiling while my inbox grows braver without me. Back Monday, kinder."

def main():
    # The gate counts characters, so the file is written with no
    # trailing newline and no extra whitespace of any kind.
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as handle:
        handle.write(TEXT)

if __name__ == "__main__":
    main()
