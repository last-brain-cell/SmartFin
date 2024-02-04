from fastapi import APIRouter

router = APIRouter()


@router.get("/budgets_test")
def budgets_test():
    return "budgets router"
