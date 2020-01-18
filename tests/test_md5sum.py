from slpkg.md5sum import md5
from slpkg.sizes import units
from slpkg.utils import Utils


def test_md5_superuser():
    result = md5('slpkg/superuser.py')
    assert result == "e6cebdf37fbc1b8e9d3c5e3e53b300c1"


def test_md5_security():
    result = md5('slpkg/security.py')
    assert result == "d395d2fcf1c7b1a91ef6ce3dc8eb047b"


def test_units():
    assert ["Kb", "Kb"], ["100", "100"] == units(['100', ['100']])


def test_dimensional_list():
    lists = [[1, 2, 3, 4, 5]]
    utils = Utils()
    assert [1, 2, 3, 4, 5] == utils.dimensional_list(lists)


def test_remove_dbs():
    lists = [1, 2, 3, 3, 4, 5, 2, 1]
    utils = Utils()
    assert [1, 2, 3, 4, 5] == utils.remove_dbs(lists)