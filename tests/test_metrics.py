from tcm_resolution.metrics import evaluate_rows
def test_metric_denominators():
    b=[{"benchmark_id":"1","public_target_id":"T900001","expected_action":"AUTO_RESOLVE"},{"benchmark_id":"2","public_target_id":"","expected_action":"ABSTAIN"}]
    p=[{"benchmark_id":"1","predicted_action":"AUTO_RESOLVE","predicted_public_record_id":"T900001","candidate_public_record_ids":"T900001"},{"benchmark_id":"2","predicted_action":"ABSTAIN","predicted_public_record_id":"","candidate_public_record_ids":""}]
    m=evaluate_rows(b,p); assert m["automatic_coverage"]["denominator"]==2; assert m["automatic_resolution_correctness"]=={"numerator":1,"denominator":1,"value":1.0}; assert m["review_or_abstention"]["numerator"]==1
