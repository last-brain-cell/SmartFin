from fastapi import APIRouter

router = APIRouter()


@router.get("/transactions_test")
def transactions_test():
    return "transactions router"
