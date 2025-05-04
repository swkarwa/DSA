import pytest


@pytest.fixture
def sample_data():
    return {"name": "Alice", "age": 30}


@pytest.fixture(scope="session")
def session_scope_fixture():
    print("\nSession scope")
    yield # pass controller to caller function and then excute rest of statements
    print("Session scope ended")


@pytest.fixture(scope="module")
def module_scope_fixture(session_scope_fixture):
    print("Module scope")
    yield
    print("Module scope ended")

@pytest.fixture(scope="class")
def test_class_fixture(module_scope_fixture):
    print("Class scope")
    yield
    print("Class scope ended")

@pytest.fixture(scope="function")
def test_function_fixture(test_class_fixture):
    print("\nFunction scope")
    yield
    print("function scope ended")





