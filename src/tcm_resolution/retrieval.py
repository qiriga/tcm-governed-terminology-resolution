from .normalization import normalize_key

def levenshtein(a: str, b: str) -> int:
    if len(a) < len(b):
        a, b = b, a
    row = list(range(len(b) + 1))
    for i, x in enumerate(a, 1):
        new = [i]
        for j, y in enumerate(b, 1):
            new.append(min(new[-1] + 1, row[j] + 1, row[j - 1] + (x != y)))
        row = new
    return row[-1]

def lcs_length(a: str, b: str) -> int:
    row = [0] * (len(b) + 1)
    for x in a:
        new = [0]
        for j, y in enumerate(b, 1):
            new.append(row[j - 1] + 1 if x == y else max(row[j], new[-1]))
        row = new
    return row[-1]

def similarity(a: str, b: str) -> float:
    if not a and not b:
        return 1.0
    lev = 1 - levenshtein(a, b) / max(len(a), len(b))
    dice = 2 * lcs_length(a, b) / (len(a) + len(b))
    return 0.7 * lev + 0.3 * dice

def rank_candidates(query: str, names_by_id: dict[str, list[str]], limit: int = 20):
    query_norm = normalize_key(query)
    scored = [(max(similarity(query_norm, value) for value in values), rid) for rid, values in names_by_id.items()]
    scored.sort(key=lambda item: (-item[0], item[1]))
    return scored[:limit]
