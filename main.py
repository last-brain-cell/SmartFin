from fastapi import FastAPI, Response, Request
from starlette import status
from starlette.responses import RedirectResponse
from database import SessionLocal
from routes import users, profiles, budgets, transactions, investments, financial_goals

app = FastAPI()


@app.get("/")
async def home():
    return RedirectResponse(url="/docs", status_code=status.HTTP_302_FOUND)


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response


app.include_router(users.router, prefix="/api/v1", tags=["users"])
app.include_router(profiles.router, prefix="/api/v1", tags=["profiles"])
app.include_router(budgets.router, prefix="/api/v1", tags=["budgets"])
app.include_router(transactions.router, prefix="/api/v1", tags=["transactions"])
app.include_router(investments.router, prefix="/api/v1", tags=["investments"])
app.include_router(financial_goals.router, prefix="/api/v1", tags=["financial_goals"])
