from pathlib import Path

def create_dict(path: str)-> dict:
    directory = Path(path).expanduser().resolve()
    
    directory.mkdir(parents=True, exist_ok=True)
    
    return {
        'success' : True,
        'path' : str(directory),
        'exists' : directory.exists(),
        'is_dict' : directory.is_dir()
    }

def list_dict(path:str)-> dict:
    directory = Path(path).expanduser().resolve()
    
    if not directory.exists():
        return {
            'success' : False,
            'message' : 'directory does not exist'
        }
    
    if not directory.is_dir():
        return {
            'success' : False,
            'message' : 'Path given is not directory'
        }
    
    items = []
    
    for item in directory.iterdir():
        items.append({
            'name' : item.name,
            'type' : 'directory' if item.is_dir() else 'file',
        })
    
    return {
        'success' : True,
        'path' : str(directory),
        'items' : items
    }


# we have now given nexus two capability 
#filesystem.create_directory
#filesystem.list_directory