from . import data

from distlib.markers import interpret as markers_interpret


import pytest

@pytest.mark.parametrize("marker", [x for x in data.markers])
def test_distlib(marker):
    markers_interpret(marker + "=='2.1'")
