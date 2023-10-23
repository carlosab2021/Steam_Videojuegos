from fastapi import FastAPI
from fastapi.openapi.models import APIBase
from app.PlayTimeGenre import app as PlayTimeGenre
from app.sentiment_analysis import app as SentimentAnalysis
from app.UserForGenre import app as UserForGenre
from app.UsersNotRecommend import app as UsersNotRecommend
from app.UsersRecommend import app as UsersRecommend
from fastapi.openapi.models import APIBase
from fastapi.openapi.models import APIBase
from fastapi.openapi.models import APIBase
from fastapi.openapi.models import APIBase

app = FastAPI()

# Monta las subaplicaciones FastAPI en sus rutas respectivas
app.mount("/PlayTimeGenre", PlayTimeGenre)
app.mount("/sentiment_analysis", SentimentAnalysis)
app.mount("/UserForGenre", UserForGenre)
app.mount("/UsersNotRecommend", UsersNotRecommend)
app.mount("/UsersRecommend", UsersRecommend)

# Define una función que obtiene la documentación OpenAPI
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="API de Steam Videojuegos",
        version="1.0",
        description="App para informacin sobre videos juegos",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=10000)

