

from app.utils.utils import src
from fastapi import APIRouter, Depends, HTTPException, status, Request
from app.utils.url_ops import valid_url, gen_url_id, create_redirect_url
from app import models
from app.models import Url
from app.db.src import get_db
from app.schemas import  Response, URL
from sqlalchemy.orm.session import Session
from app.core.logger import logger


router = APIRouter(
    prefix="/v1"
)
file = src(__file__)

@router.post("/sh", status_code=status.HTTP_201_CREATED, response_model=Response)
async def url_short( req: Request, db: Session = Depends(get_db), url: URL = Depends(valid_url)):
    # Create New Redirect-URL
    try:
        
        base_url = req.base_url._url # base url 
        query_search = db.query(Url).filter(Url.long_url == url.url.unicode_string()).first()
        
        # if the url is already registered
        if query_search is not None:
            logger.info(f"<{file}>:: URL Already Registred as: [{query_search.id}] --to-> [{url.url.unicode_string()}]")
            return Response(
                url = create_redirect_url(base_url, str(query_search.id)).url.unicode_string(),
                valid=bool(query_search.valid)
            )
            
        #* create new URL-obj
        url_model = models.Url(
            long_url = url.url.unicode_string(),
            valid = url.valid,
            id = gen_url_id()
        )
        
        #* add URL-obj to db
        db.add(url_model)
        db.commit()
        db.refresh(url_model)
        
        #* collect url parts & final check
        new_url = create_redirect_url(base_url, str(url_model.id))
        
        logger.success(f"<{file}>:: New URL Registred with ID: [{url_model.id}]--to->[{url.url.unicode_string()}]")
        
        
        return Response(
            url = new_url.url,
            valid=url.valid
        )
    except HTTPException : raise
    
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=e
        )