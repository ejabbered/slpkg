from slpkg.md5sum import md5


def test_md5():
    result = md5('slpkg/superuser.py')
    assert result == "e6cebdf37fbc1b8e9d3c5e3e53b300c1"
