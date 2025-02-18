import pytest
from unittest.mock import patch
from nescom.hello import say_hello

@pytest.fixture
def mock_completion():
    with patch('litellm.completion') as mock:
        mock.return_value.choices = [
            type('Choice', (), {'message': type('Message', (), {'content': 'Muhammad Ali Jinnah\\n'})})()
        ]
        yield mock

def test_say_hello(mock_completion):
    result = say_hello()
    assert isinstance(result, str)
    assert result == "Muhammad Ali Jinnah"
    mock_completion.assert_called_once_with(
        model="gemini/gemini-1.5-flash",
        messages=[{"role": "user", "content": "Who is the founder of Pakistan?"}]
    ) 