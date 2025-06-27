from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from .routers import states

app = FastAPI()
app.include_router(states.router)


@app.get("/")
def root():
    return RedirectResponse(url="/states")
