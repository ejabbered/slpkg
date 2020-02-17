from slpkg.md5sum import md5


def test_md5_superuser():
    result = md5('slpkg/superuser.py')
    assert result == "c6a3576c247bda199c75b43540bfc3d7"


def test_md5_security():
    result = md5('slpkg/security.py')
    assert result == "eb8dbea4dec6d72353d30475670389f0"
