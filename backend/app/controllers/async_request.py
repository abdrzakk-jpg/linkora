
#* Define 

from typing import Any
import httpx # for Asynchronous requests

# async requests manager
async def async_get(url, follow_redirects=False, timeout=5, headers={}) -> Any | None:
    async with httpx.AsyncClient(follow_redirects=follow_redirects, timeout=timeout) as aclient:
        try:
            response = await aclient.get(
                url=url,
                headers=headers,
                follow_redirects=follow_redirects,
                timeout=timeout
                )
            response.raise_for_status()
            return response
        except httpx.HTTPStatusError:
            return None
