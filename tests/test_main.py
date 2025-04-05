from unittest.mock import patch

from typer.testing import CliRunner

from ignoreme.main import app

runner = CliRunner()


@patch('ignoreme.api_client.list_templates')
def test_cli_list(mock_list):
    mock_list.return_value = ['python', 'lua', 'zig']
    result = runner.invoke(app, ['list'])

    assert result.exit_code == 0
    assert 'python' in result.output
    assert 'lua' in result.output
    assert 'zig' in result.output


@patch('ignoreme.api_client.get_gitignore')
def test_cli_generate_stdout(mock_get):
    mock_get.return_value = '# Python\n__pycache__/'
    result = runner.invoke(app, ['generate', 'python'])

    assert result.exit_code == 0
    assert '# Python' in result.output


@patch('ignoreme.api_client.get_gitignore')
def test_cli_generate_to_file(mock_get, tmp_path):
    mock_get.return_value = '# Lua\n*.luac'
    output_file = tmp_path / '.gitignore'

    result = runner.invoke(
        app, ['generate', 'lua', '--output', str(output_file)]
    )
    assert result.exit_code == 0
    assert output_file.read_text() == '# Lua\n*.luac'


@patch('ignoreme.api_client.get_gitignore')
def test_cli_generate_invalid_template(mock_get):
    mock_get.side_effect = ValueError('Invalid template')
    result = runner.invoke(app, ['generate', 'invalidtemplate'])

    assert result.exit_code != 0
    assert 'Invalid template' in result.output
