from fastapi import FastAPI
from app.api.routes import auth

app = FastAPI(
    title="cirqleX",
    description="This is cirqleX official documentation",
    version="1.0.0"
)
app.include_router(auth.router)

# @app.get('/')
# def index():
#     return {'message': 'I am working'}

# models.Base.metadata.create_all(database.engine)
