
#from app.controllers.validators import URL_validation_handler
#from fastapi.exceptions import RequestValidationError

from app.core.logger import logger
from fastapi.responses import RedirectResponse
from app.api.v1 import redirect, short_url  # import routers
from app.db.database import Base, engine
from fastapi import FastAPI
from scalar_fastapi import Layout, Theme, get_scalar_api_reference
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import allowed_origins, settings as env


# creating FastAPI instance 
app = FastAPI(
    docs_url=None,  # تعطيل Swagger
    redoc_url=None,  # تعطيل ReDoc
)

# init the CORS-MidllWare
app.add_middleware(
    CORSMiddleware, 
    allow_origins=allowed_origins, # 
    allow_credentials=True,
    allow_methods=["*"], # GET, POST,PUT,PATCH,DELETE,OPTIONS ...
    allow_headers=["*"], # 
)




# init db in production environment
if env.ENVIRONMENT == "production":
    Base.metadata.create_all(bind=engine)



# * ===================|Updating-Docs-UI|=================== *#
@app.get("/docs", include_in_schema=False)
async def scalar_docs():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        layout=Layout.CLASSIC,
        theme=Theme.DEEP_SPACE,
        title="API Docs",
    )
# * ======================================================== *#


@app.get("/")
def home():
    return {"status": "ALIVE"}
# import routers
app.include_router(short_url.router)
app.include_router(redirect.router)


logger.success("Hello World !")