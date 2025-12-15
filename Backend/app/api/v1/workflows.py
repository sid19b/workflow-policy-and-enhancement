from fastapi import APIRouter

router=APIRouter()

@router.get("/workflows")
async def workflows():
    return {"workflow":"using"}