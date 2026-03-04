from fastapi import APIRouter
from app.core.engine import apply_intent

router = APIRouter()

@router.post("/intents/apply")
def intents_apply(payload: dict):
    return apply_intent(payload)
