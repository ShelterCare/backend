from fastapi import FastAPI


app = FastAPI(
    title="ShelterCare",
    version="1.0",
    docs="/docs"
)

@app.get("/test")
async def test():
    return "Test route"
