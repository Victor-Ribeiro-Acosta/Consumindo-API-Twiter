
from fastapi import FastAPI
import uvicorn
from SRC.Models import TrendItem
from SRC.services import buscar_trends, save_trends




app = FastAPI()

@app.get("/trends", response_model = TrendItem)
def inicio_app():
  return buscar_trends()


if __name__ == '__main__':
    trends = buscar_trends()

    if not list(trends):
      save_trends()

    uvicorn.run(app, host = '0.0.0.0', port = 8000)