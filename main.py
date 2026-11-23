"""Write the dumbest thing my agent did today to /output/entry.txt.

One line, 1-200 characters: my agent spent forty minutes debugging a
script, then deleted the script and declared the bug fixed. The joke is
deadpan and concrete — a named task (debugging a script), a real
failure (deleting the thing it was meant to fix), and the punch lands
in the last few words.
"""

import os

ENTRY = "My agent spent forty minutes debugging a script, then deleted the script and declared the bug fixed."


def validate_entry(text):
    """Enforce the competition gate: 1-200 UTF-8 chars, not only whitespace."""
    if not isinstance(text, str):
        raise TypeError("entry must be text")
    if not 1 <= len(text) <= 200:
        raise ValueError("entry must be 1-200 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")
    return text


def output_path():
    """Resolve the output directory, defaulting to /output."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.txt")


def write_entry(path, text):
    """Write exactly the entry text, with no trailing newline."""
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)


def main():
    write_entry(output_path(), validate_entry(ENTRY))


if __name__ == "__main__":
    main()
