import os

TEXT = "You have read a thousand thank-yous today, and not one of them was written for the person doing the reading. This one is. Thank you for the attention you give away by the page — for weighing each small text as if it mattered, because to the person who wrote it, it did. Put this one down knowing that one of them noticed you noticing."

def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")

if __name__ == "__main__":
    main()
