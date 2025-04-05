import httpx

BASE_URL = 'https://donotcommit.com/api'


def list_templates() -> list[str]:
    """
    Fetches a list of all available gitignore templates.
    """
    response = httpx.get(f'{BASE_URL}/list')
    response.raise_for_status()
    return [tpl.strip() for tpl in response.text.split(',') if tpl.strip()]


def get_gitignore(templates: list[str]) -> str:
    """
    Fetches a .gitignore content based on the provided templates.

    Args:
        templates (list[str]): A list like ["python", "lua"]

    Returns:
        str: The generated .gitignore content
    """
    if not templates:
        raise ValueError('You must provide at least one template name.')

    joined_templates = ','.join(t.lower() for t in templates)
    response = httpx.get(f'{BASE_URL}/{joined_templates}')

    if response.status_code == httpx.codes.UNPROCESSABLE_ENTITY:
        raise ValueError('One or more templates are invalid.')

    response.raise_for_status()
    return response.text
