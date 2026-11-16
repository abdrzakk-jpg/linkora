
from pathlib import Path

def src(f:str):
    "funcntion helps to locate logging-messages source(where log msg came from)"    
    x = Path(f)
    return f"{x.parent.name}: {x.name}"

