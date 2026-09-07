
#* Define Schema of Expected Inputs

from pydantic import BaseModel, HttpUrl


# url schema (for req&res)
class URL(BaseModel):
    url: HttpUrl
    valid: bool = False

# expected url-scheme input
class URLRequest(BaseModel):
    url: HttpUrl
