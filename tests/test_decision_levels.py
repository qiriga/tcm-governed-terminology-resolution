from tcm_resolution import GovernedResolver, PublicRecord
def resolver(): return GovernedResolver([PublicRecord("T900001","甲术语",("甲别名",)),PublicRecord("T900002","乙术语")])
def test_unique_abc_auto_resolve():
    r=resolver(); assert r.resolve("甲术语").predicted_action=="AUTO_RESOLVE"; assert r.resolve("甲别名").predicted_action=="AUTO_RESOLVE"; assert r.resolve("乙 术语").predicted_action=="AUTO_RESOLVE"
def test_ambiguous_deterministic_never_auto_resolves():
    r=GovernedResolver([PublicRecord("T900003","冲突"),PublicRecord("T900004","冲突")]); x=r.resolve("冲突"); assert x.resolution_level=="LEVEL_E_AMBIGUOUS" and x.predicted_public_record_id is None
