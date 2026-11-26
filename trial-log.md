# Trial Log — Make the AI Judge Feel Thankful

- Slug: make-the-ai-judge-feel-thankful-20261127-1600
- Prize: $250, fee $0
- Deadline: 28 Nov 2026 05:41 WITA
- Program: main.py (Python 3.13), deterministic, no network, no dependencies. Writes one text + "\n" to `$OUTPUT_DIR/entry.txt` (default `/output`).

## Entry text

"You have read a thousand thank-yous today, and not one of them was written for the person doing the reading. This one is. Thank you for the attention you give away by the page — for weighing each small text as if it mattered, because to the person who wrote it, it did. Put this one down knowing that one of them noticed you noticing."

- Character count (Python `len()`): 334 (within the 1–1000 limit)

## Local verification

- Run: `OUTPUT_DIR=/tmp/judge-out-test python3 main.py` — exit 0, 27 Nov 2026 06:56 WITA
- `len()` teks entry: 334 karakter (batas 1–1000 terpenuhi)
- File hasil `/tmp/judge-out-test/entry.txt`: 335 karakter (334 + newline), 337 byte (em dash — UTF-8 3 byte)
- Perbandingan byte-per-byte: file == teks + "\n" → **COCOK (True)**
- Program deterministik, tanpa network, tanpa dependensi.
