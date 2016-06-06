from . import data

import packaging.requirements

import pytest

@pytest.mark.parametrize("marker", [x for x in data.markers])
def test_packaging(marker):
    req = "foo==1.1;" + marker + "=='2.1'"
    parsed = packaging.requirements.Requirement(req)
    parsed.marker.evaluate()
