from apps.tools.registry import get_tool
def check_permission(tool_name: str) -> dict:
    tool = get_tool(tool_name)

    if tool is None:
        return {
            'allowed' : False,
            'required_approval' : False,
            'reason' : 'Unknown Tool',
        }

    if tool.requires_approval:
        return {
            'allowed' : False,
            'requires_approval' : True,
            'risk_level': tool.risk_level,
            'reason' : 'User approval required'
        }

    else:
        return {
            'allowed' : True,
            'requires_approval' : False,
            'risk_level' : tool.risk_level,
            'reason' : 'Tool allowed by policy'
        }