import program_2

def test_prov(capfd):
    program_2.proverbs_22_29()
    out, err = capfd.readouterr()
    assert "Proverbs 22:29" in out