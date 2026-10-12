import unicodedata

def normalize_key(value: str) -> str:
    """Frozen normalization: Unicode NFKC followed by whitespace removal."""
    return "".join(char for char in unicodedata.normalize("NFKC", value) if not char.isspace())
