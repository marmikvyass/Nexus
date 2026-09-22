from apps.tools.base import Tools
from apps.tools.filesystem import (create_dict, list_dict)

TOOLS = {
    'filesystem.create_dict' : Tools(
        name='filesystem.create_dict',
        description='Create a directory on computer',
        function=create_dict,
        risk_level='low',
        requires_approval=False
    ),

    'filesystem.list_dict' : Tools(
        name='filesystem.list_dict',
        description='List all the files and directories at the given path',
        function=list_dict,
        risk_level='low',
        requires_approval=False
    )
}

def get_tool(name:str)-> Tools | None:
    return TOOLS.get(name)

def get_all_tools() -> list[Tools]:
    return list(TOOLS.values())