from fastapi import APIRouter

router = APIRouter()


@router.get("/investments_test")
def investments_test():
    return "investments router"
