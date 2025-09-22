import matplotlib
matplotlib.use("Agg")

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from solvers.ballistics import simulate_ballistics

app = FastAPI()


# Allow React frontend to call API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://devindubbelde.com"],  # or your domain for tighter security
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/hello")
def say_hello():
    return {"message": "Hello from Python!2"}

@app.get("/ballistics")
def get_ballistics(v0: float = 10, angle: float = 45, h0: float = 0):
    img_base64, totalDistance = simulate_ballistics(v0, angle, h0)
    return {
        "image": img_base64,
        "totalDistance": totalDistance
    }