
from fastapi.exceptions import RequestValidationError
from app.api.v1 import redirect, short_url  # import routers
from app.db.database import Base, engine
from fastapi import FastAPI
from scalar_fastapi import Layout, Theme, get_scalar_api_reference
from app.controllers import validation_handler


# creating FastAPI instance 
app = FastAPI(
    docs_url=None,  # تعطيل Swagger
    redoc_url=None,  # تعطيل ReDoc
)
# db init
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
def main():
    return {"msg": "Hello world"}

# import routers
app.include_router(short_url.router)
app.include_router(redirect.router)


#* add exceptions handlers
app.add_exception_handler(
    RequestValidationError,
    # pyrefly: ignore [bad-argument-type]
    validation_handler
)