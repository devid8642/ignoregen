from unittest.mock import Mock, patch

import pytest

from ignoreme import api_client


@patch('httpx.get')
def test_list_templates(mock_get):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.text = 'python,lua,zig'
    mock_get.return_value = mock_response

    result = api_client.list_templates()
    assert result == ['python', 'lua', 'zig']
    mock_get.assert_called_once_with('https://donotcommit.com/api/list')


@patch('httpx.get')
def test_get_gitignore_success(mock_get):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.text = '# Python\n__pycache__/'
    mock_get.return_value = mock_response

    content = api_client.get_gitignore(['python'])
    assert '# Python' in content
    mock_get.assert_called_once_with('https://donotcommit.com/api/python')


@patch('httpx.get')
def test_get_gitignore_multiple_templates(mock_get):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.text = '# Python\n# Lua'
    mock_get.return_value = mock_response

    content = api_client.get_gitignore(['python', 'lua'])
    assert '# Python' in content
    assert '# Lua' in content
    mock_get.assert_called_once_with('https://donotcommit.com/api/python,lua')


def test_get_gitignore_empty_list():
    with pytest.raises(ValueError, match='at least one template'):
        api_client.get_gitignore([])


@patch('httpx.get')
def test_get_gitignore_invalid_template(mock_get):
    mock_response = Mock()
    mock_response.status_code = 422
    mock_get.return_value = mock_response

    with pytest.raises(ValueError, match='invalid'):
        api_client.get_gitignore(['invalidtemplate'])
