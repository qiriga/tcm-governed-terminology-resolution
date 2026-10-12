from tcm_resolution import GovernedResolver, PublicRecord
def test_repeatability():
    r=GovernedResolver([PublicRecord("T900001","甲术语")]); assert r.resolve("甲术语") == r.resolve("甲术语")
