
#* Define URL's operations
from typing import Any
from app.schemas import URL, URLRequest
from app.controllers.async_request import async_get
from random import choices
from string import ascii_letters, digits
from urllib.parse import urljoin 

# headers for validation-requests
headers = {
    "User-Agent": (
        "Mozilla/5.0 (X11; Linux x86_64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/140.0.0.0 Safari/537.36"
    )
}
async def valid_url(url: URLRequest) -> URL:
    """Url Accessablity Validation"""
    
    try:
        res: Any  = await async_get(url=url.url.unicode_string(), headers=headers, timeout=10, follow_redirects=False)
        if res.status_code < 400 : return URL(url=url.url, valid=True) # if status_code in range 2xx - 3xx
        
        return URL(url=url.url, valid=False) # return url & make as invalid
    
    except : return URL(url=url.url, valid=False)



async def check_redirection(url: URL) -> bool:
    """checks The Functionality of generated redirect-url"""
    
    res: Any = await async_get(url=url.url.unicode_string(), headers=headers, timeout=10, follow_redirects=False)
    
    if res is not None:    
        return (300 >= res.status_code < 400) # return if the status_code in range [3xx, 4xx[
    
    
    return False
    
def create_redirect_url(base: str, id:str) -> URL:
    """merge `base` with `url-id`"""
    
    string_url = urljoin(base, f"/v1/re/{id}")
    http_url_obj = URL(url=string_url)
    return http_url_obj



def gen_url_id():
    """generate `url-id`"""
    
    return "".join(choices(ascii_letters+digits, k=10))