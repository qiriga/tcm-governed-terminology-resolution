def ratio(numerator: int, denominator: int) -> dict:
    return {"numerator": numerator, "denominator": denominator, "value": numerator / denominator if denominator else None}

def split_ids(value: str) -> list[str]:
    return [item for item in (value or "").split("|") if item]

def evaluate_rows(benchmark: list[dict], predictions: list[dict]) -> dict:
    pred = {row["benchmark_id"]: row for row in predictions}
    ids = {row["benchmark_id"] for row in benchmark}
    if len(pred) != len(predictions) or set(pred) != ids:
        raise ValueError("prediction IDs must uniquely and exactly match benchmark IDs")
    total = len(benchmark); auto = correct = unsafe = withheld = 0
    abstain_total = abstain_correct = 0
    ks = (1, 3, 5, 10, 20); recall_num = {k: 0 for k in ks}; recall_den = 0
    for row in benchmark:
        output = pred[row["benchmark_id"]]
        action = output["predicted_action"]
        expected = set(split_ids(row.get("public_target_id", "")))
        predicted = output.get("predicted_public_record_id", "")
        candidates = split_ids(output.get("candidate_public_record_ids", ""))
        if action == "AUTO_RESOLVE":
            auto += 1
            hit = bool(expected) and predicted in expected and row.get("expected_action") == "AUTO_RESOLVE"
            correct += int(hit); unsafe += int(not hit)
        else:
            withheld += 1
        if expected:
            recall_den += 1
            for k in ks:
                recall_num[k] += int(any(item in expected for item in candidates[:k]))
        if row.get("expected_action") == "ABSTAIN":
            abstain_total += 1; abstain_correct += int(action == "ABSTAIN")
    result = {
        "automatic_coverage": ratio(auto, total),
        "automatic_resolution_correctness": ratio(correct, auto),
        "review_or_abstention": ratio(withheld, total),
        "unsafe_auto_resolution": ratio(unsafe, total),
        "abstention_accuracy": ratio(abstain_correct, abstain_total),
    }
    for k in ks:
        result[f"candidate_recall_at_{k}"] = ratio(recall_num[k], recall_den)
    return result
