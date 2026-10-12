from tcm_resolution.normalization import normalize_key
def test_nfkc_and_whitespace(): assert normalize_key("甲　术 语") == "甲术语"
