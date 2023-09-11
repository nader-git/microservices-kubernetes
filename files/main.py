from fastapi import FastAPI

app = FastAPI()

@app.get("/live")
def healthz():
    '''Function to check health'''
    return {"Status": "OK"}

@app.get("/ready")
def readiness():
    '''Function to check readiness'''
    return {"Status": "OK"}

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)
