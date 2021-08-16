from my_br_package.lib import try_me

def test_try_me():
    a = try_me()
    assert len(a) > 0
