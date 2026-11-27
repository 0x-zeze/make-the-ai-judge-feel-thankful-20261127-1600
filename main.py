"""make.fun entry: Make the AI judge feel thankful (make-the-ai-judge-feel-thankful-20261127-1600)."""

from pathlib import Path

OUTPUT_PATH = Path("/output/entry.txt")
MIN_CHARS = 1
MAX_CHARS = 1000

TEXT: str = """Past two in the morning, a night clerk in a small post office sits at the back counter with the letters that never found their address.

Blue ink has bled where rain got in; a town name breaks off halfway, pencil pressed hard enough to ridge the paper. She reads each letter twice: once for a missing number, once for the person who wrote it.

She runs her thumb down the crease, slips the page back into its envelope, and files it in the wooden drawer marked "waiting". Nobody watches through the frosted glass. Nobody leaves a note at dawn. Not one goes to the bin; someone sat at a kitchen table and wrote it line by line.

This page has no return address. Thank you for staying in the quiet to read it twice."""


def validate_text(text: str) -> str:
    """Validate that text is 1-1000 Unicode code points and not whitespace-only."""
    if not text.strip():
        raise ValueError("Entry text must not be empty or whitespace-only.")
    length = len(text)
    if not (MIN_CHARS <= length <= MAX_CHARS):
        raise ValueError(
            f"Entry text must be {MIN_CHARS}-{MAX_CHARS} Unicode code points, got {length}."
        )
    return text


def main() -> None:
    """Validate and write the deterministic entry text to /output/entry.txt."""
    text = validate_text(TEXT)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
