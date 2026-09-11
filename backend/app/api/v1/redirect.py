
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

@router.get("/re/{id}", status_code=307)
async def redirecting(id: str, db: Session = Depends(get_db)):
    try:
        id_query = db.query(models.Url).filter(models.Url.id == id).first()
        if id_query is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='URL does not exists'
            )
        return RedirectResponse(str(id_query.long_url))

    except HTTPException : raise
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=e
        )