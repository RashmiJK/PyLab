## Pytest

### Introduction
- Testing framework for python
- Auto-discovery of tests (name your tests as test_<name_of_file>.py, test_<name_of_function>, pytest command)
- Rich assertion introspection
- Support **parameterized** and **fixture-based** testing
    * parameterized - run test with multiple times with different arguments ensuring that broad test coverage with minimal code
    * Fixture - Set up test environment before tests run and tear it down afterward.

### Test run tips
Basic
- ```pytest test_example.py``` - Run a specific test file
- ```pytest test_exampple.py::test_function_name``` - Run a specific test function
- ```pytest test_example.py::TestClassName::test_method_name ``` - Run a specific test method in a class

Run tests matching a pattern (using -k flag)
- ```pytest -k "test_login" ``` - Runs all tests with "test_login" in the name
- ```pytest -k "not slow"``` - Runs all tests except those with "slow" in the name
- ```pytest -k "user and not admin"``` - Boolean expressions work too

Run tests by markers using -m option
- ```pytest -m "slow"``` - Runs tests marked with **@pytest.mark.slow**, **@pytest.mark.skip(reason="This feature is currently broken")**, **@pytest.mark.xfail(reason="Expected, cannot divide by 0")**
- ```pytest -m "not slow"``` - Run tests not marked as slow

Useful additional flags
- ```pytest test_file.py::test_function -v``` - Verbose output
- ```pytest test_file.py::test_function -s``` - Don't capture output (see print statements)
- ```pytest test_file.py::test_function --tb=short``` - Shorter traceback format
- ```pytest test_file.py::test_function -x``` - Stop after first failure

### Key features

1. Assert
   Example ```assert test_output == 1```. Assert if the test_output is not equal to 1.

2. ```with pytest.raises(ValueError)``` - Assert that a specific exception is raised

3. Class based tests - Group related tests in a class
    - Use special method names, **setup_method** and **teardown_method**, for setup and cleanup

4. Fixture based tests

    #### Differences between Class-based Setup/Teardown and Fixtures

    | Aspect                        | Class-based (`setup_method`/`teardown_method`) | Fixtures (`@pytest.fixture`)                |
    |-------------------------------|-----------------------------------------------|---------------------------------------------|
    | **Reusability**               | Limited to the class; harder to reuse         | Can be shared across multiple files/classes |
    | **Scope**                     | Method or class level only                    | Flexible: function, class, module, session  |
    | **Sharing Setup**             | Not easily shared across files                | Easily shared via `conftest.py`             |
    | **Dependency Injection**      | Access via `self.attribute`                   | Passed as parameters to tests               |
    | **Composability**             | Hard to combine multiple setups               | Easy to compose fixtures together           |
    | **Flexibility**               | Less flexible for complex setups              | Highly flexible and modular                 |


5. Marking tests

   Use markers to add metadata to tests. Common markers include:
   - **@pytest.mark.slow** - Marks a test as slow.
   - **@pytest.mark.skip(reason="...")** - Skips a test with a reason.
   - **@pytest.mark.xfail(reason="...")** - Marks a test as expected to fail.
   - **@pytest.mark.skipif(condition, reason="...")** - Skips a test if the condition is true.

6. Parameterized tests

   Use the **@pytest.mark.parametrize** decorator to run a test function with different sets of parameters.

   Example:
   ```python
   @pytest.mark.parametrize("input,expected", [(1, 2), (2, 3), (3, 4)])
   def test_increment(input, expected):
       assert increment(input) == expected
   ```

7. Mocking
    Mocking is a technique used in testing to replace external dependencies or components with controlled, simulated implementations. This allows you to isolate the code under test and avoid relying on external systems, such as APIs, databases, or file systems, which may be slow, unreliable, costly, or have side effects.

    **When to use mocking:**
    - When your code interacts with external services (e.g., APIs, databases, file systems).
    - When you want to simulate specific scenarios, such as errors or edge cases, that are hard to reproduce with real dependencies.
    - When you need to speed up tests by avoiding slow operations.
    - When you want to avoid side effects, such as modifying real data or incurring costs.

    For example, when testing code that fetches data from an external API using the `requests` library, you can mock the API call to return a predefined response instead of making a real network request. Similarly, mocking is useful when testing code that interacts with a database, so you don't need to set up or modify real data during tests.

   Example:
   ```python
    import unittest.mock as mock
    from src import db_service

    # The order of arguments to the test function is the reverse of the decorator order.
    # db_service.get_email_by_id is mocked by mocked_get_email
    # db_service.get_user_by_id is mocked by mocked_get_user
    @mock.patch("src.db_service.get_user_by_id")
    @mock.patch("src.db_service.get_email_by_id")
    def test_get_user_by_id_from_db(mocked_get_email, mocked_get_user):
        mocked_get_user.return_value = "mocked Christopher"
        mocked_get_email.return_value = "mockedc@abc.com"

        user_name = db_service.get_user_by_id(3)
        email = db_service.get_email_by_id(3)
        
        assert user_name == "mocked Christopher"
        assert email == "mockedc@abc.com"
   ```

### Other features
1. Monkey patching using pytest.MonkeyPatch
2. MagicMock() class in unittest.mock
3. unittest.mock.patch() => use context manager with