from apps.tools.registry import get_tool
from apps.permission.policy import check_permission

def execute_tool(tool_name: str, arguments:dict) -> dict:

    permission = check_permission(tool_name)

    if not permission['allowed']:
        return {
            'success' : False,
            'tool' : tool_name,
            'permission' : permission
        }

    tool = get_tool(tool_name)

    try:
        result = tool.function(**arguments)

        return {
            'success' : True,
            'tool' : tool_name,
            'permission' : permission,
            'result' : result
        }

    except Exception as error:
        return {
            'success' : False,
            'tool' : tool_name,
            'permission' : permission,
            'error' : str(error)
        }