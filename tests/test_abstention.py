from tcm_resolution import GovernedResolver, PublicRecord
def test_d_e_f_cannot_emit_factual_output():
    d=GovernedResolver([PublicRecord("T900001","甲术语")]).resolve("甲术雨")
    e=GovernedResolver([PublicRecord("T900002","冲突"),PublicRecord("T900003","冲突")]).resolve("冲突")
    f=GovernedResolver([PublicRecord("T900004","甲术语")]).resolve("完全无关输入")
    assert d.resolution_level=="LEVEL_D_FUZZY_CANDIDATE"
    assert e.resolution_level=="LEVEL_E_AMBIGUOUS"
    assert f.resolution_level=="LEVEL_F_UNSUPPORTED"
    assert all(x.predicted_public_record_id is None and x.predicted_action!="AUTO_RESOLVE" for x in (d,e,f))
