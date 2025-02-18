from fastapi import FastAPI
from app.core.config import engine, Base
from app.api.routes import auth

app = FastAPI(
    title="cirqleX",
    description="""
    CirqleX is a platform designed to support individuals in the tech community, whether you're a coder, developer, designer, or tech enthusiast. It helps users track their progress, connect with like-minded peers, and enhance their skills through structured learning, challenges, and mentorship. With features like real-time collaboration, AI-driven feedback, and gamification, CirqleX encourages continuous growth, collaboration, and consistency. Whether you're working solo or in a team, CirqleX is the place to engage, learn, and thrive in the tech world.
    """,
    version="1.0.0"
)

app.include_router(auth.router)


@app.on_event("startup")
async def startup():
    # Using async context to interact with the engine
    async with engine.begin() as conn:
        # Creating tables synchronously
        await conn.run_sync(Base.metadata.create_all)

@app.on_event("shutdown")
async def shutdown():
    pass  
