from fastapi import APIRouter, HTTPException

from ..utils.parse import get_avg_data

router = APIRouter(prefix="/states", tags=["states"])
state_avg_price = get_avg_data()


@router.get("/")
def read_all_states():
    return { "Description": "Average electricity prices of each Australian states", **state_avg_price }


@router.get("/{state_id}")
def read_state(state_id: str):
    state_id = state_id.upper()
    states = sorted(state_avg_price.keys())
    if state_id not in states:
        raise HTTPException(status_code=400, detail=f"Invalid state, must only pick from: {', '.join(states)}")
    return {
        "state": state_id,
        "average_price": state_avg_price[state_id]
    }
