import pytest

module_app = pytest.importorskip("homework_05.app")


@pytest.fixture
def client():
    try:
        app = module_app.app
    except AttributeError:
        raise pytest.fail("skip testing homework_05 due to lack of Flask `app` in the `app.py`")

    app.config['TESTING'] = True

    with app.test_client() as client:
        # with app.app_context():
        #     app.init_db()
        yield client


def test_visit_index(client):
    rv = client.get("/")
    assert rv.status_code == 200


def test_visit_about(client):
    rv = client.get("/about/")
    assert rv.status_code == 200


def test_nav_present(client):
    rv = client.get("/")
    assert b'<nav class="navbar' in rv.data
    assert b'</nav>' in rv.data


def test_meta_viewport_present(client):
    rv = client.get("/")
    assert b'<meta name="viewport"' in rv.data
