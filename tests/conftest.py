import pytest

@pytest.fixture(scope='session')
def app():
    from app import create_app
    app = create_app()
    yield app

@pytest.fixture(scope='session')
def client(app):
    return app.test_client()