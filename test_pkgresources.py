from . import data

import pkg_resources

import pytest

@pytest.mark.parametrize("marker", [x for x in data.markers])
def test_pkg_resources(marker):
    req = "foo==1.1;" + marker + "=='2.1'"
    req, mark = req.split(";")
    pkg_resources.Requirement.parse(req)
    pkg_resources.evaluate_marker(mark)


@pytest.mark.parametrize("marker", [x for x in data.markers])
def test_pkg_resources_no_parser(marker):
    if not hasattr(pkg_resources, "MarkerEvaluation"):
        pytest.skip("no markerlib variant")
    
    parser = pkg_resources.parser
    evaluate_marker = pkg_resources.evaluate_marker

    del pkg_resources.parser
    pkg_resources.evaluate_marker = pkg_resources.MarkerEvaluation._markerlib_evaluate

    try:
        req = "foo==1.1;" + marker + "=='2.1'"
        req, mark = req.split(";")
        pkg_resources.Requirement.parse(req)
        pkg_resources.evaluate_marker(mark)
    finally:
        pkg_resources.parser = parser 
        pkg_resources.evaluate_marker = evaluate_marker
