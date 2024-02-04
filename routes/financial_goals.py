from fastapi import APIRouter

router = APIRouter()


@router.get("/financial_goals_test")
def financial_goals_test():
    return "financial_goals router"
