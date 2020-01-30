from slpkg.md5sum import md5


def test_md5_superuser():
    result = md5('slpkg/superuser.py')
    assert result == "e6cebdf37fbc1b8e9d3c5e3e53b300c1"


def test_md5_security():
    result = md5('slpkg/security.py')
    assert result == "3f10bf99b21f66af879dc0882bcd92b3"
