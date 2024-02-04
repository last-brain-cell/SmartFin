from fastapi import APIRouter

router = APIRouter()


@router.get("/profiles_test")
def profiles_test():
    return "profiles router"
