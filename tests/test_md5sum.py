from slpkg.md5sum import md5


def test_md5_superuser():
    result = md5('slpkg/superuser.py')
    assert result == "e6cebdf37fbc1b8e9d3c5e3e53b300c1"


def test_md5_security():
    result = md5('slpkg/security.py')
    assert result == "d395d2fcf1c7b1a91ef6ce3dc8eb047b"