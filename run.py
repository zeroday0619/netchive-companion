import uvicorn
from fastapi import FastAPI
from apis import router

app = FastAPI(
    name="Netchive companion",
    description="Youtube-dl webserver interface",
    debug=False
)


@app.get("/", tags=["root"])
async def root():
    return {"status": "OK"}


if __name__ == "__main__":
    app.include_router(
        router=router
    )
    uvicorn.run(app=app, host='0.0.0.0', port=18181)
