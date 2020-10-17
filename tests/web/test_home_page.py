import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '../../../src')
from web.app import app


def test_returns_404_with_no_path():
    response = app.test_client().get("/")
    assert response.status_code == 404


def test_returns_200_with_correct_path():
    response = app.test_client().get("/options")
    assert response.status_code == 200







