
from app.core.logger import logger
from app.utils.utils import src
from fastapi import status
from fastapi import HTTPException
from fastapi import Depends
from fastapi.responses import RedirectResponse
from fastapi import APIRouter
from app import models
from app.db.src import get_db
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/v1"
)
file = src(__file__)

@router.get("/re/{id}", status_code=status.HTTP_307_TEMPORARY_REDIRECT)
async def redirecting(id: str, db: Session = Depends(get_db)):
    """ Redirect The to original URL """
    
    try:
        id_query = db.query(models.Url).filter(models.Url.id == id).first()
        
        # check the id validation
        if id_query is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='URL-ID does not exists'
            )
        logger.info(f"<{file}>:: Redirect destnation: [{id_query.id}]--to->[{id_query.long_url}]")
        return RedirectResponse(str(id_query.long_url))

    except HTTPException : raise # ignore HTTPExceptions
    
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=e
        )