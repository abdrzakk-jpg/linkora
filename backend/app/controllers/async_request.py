
#* Define Asynchronous-Requests Function

from app.core.logger import logger
from typing import Any
import httpx # for Asynchronous requests

# async requests manager
async def async_get(url, follow_redirects=False, timeout=5, headers={}) -> Any | None:
    """Async-api-requests function"""
    
    async with httpx.AsyncClient(follow_redirects=follow_redirects, timeout=timeout) as asynclient:
        try:
            response = await asynclient.get(
                url=url,
                headers=headers,
                follow_redirects=follow_redirects,
                timeout=timeout
                )
            logger.trace(f"</controllers:async_request.py>:: Request sent to: GET/:{url}")
            response.raise_for_status()
            return response
        
        except httpx.HTTPStatusError:
            return None
