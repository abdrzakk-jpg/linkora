
#* Define Schema of Expected Inputs

from pydantic import BaseModel, HttpUrl


# url schema (for req&res)
class URL(BaseModel):
    """Default URL Schema"""
    
    url: HttpUrl
    valid: bool = False

# expected url-scheme input
class URLRequest(BaseModel):
    """Request Structure (url only)"""
    url: HttpUrl
