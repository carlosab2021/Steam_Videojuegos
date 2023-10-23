from fastapi import FastAPI
from starlette.middleware.wsgi import WSGIMiddleware
from app.PlayTimeGenre import app as PlayTimeGenre
from app.sentiment_analysis import app as sentiment_analysis
from app.UserForGenre import app as UserForGenre
from app.UsersNotRecommend import app as UsersNotRecommend
from app.UsersRecommend import app as UsersRecommend

main_app = FastAPI()

# Monta la aplicación Flask
main_app.mount("/PlayTimeGenre", WSGIMiddleware(PlayTimeGenre))
main_app.mount("/sentiment_analysis", WSGIMiddleware (sentiment_analysis))
main_app.mount("/UserForGenre", WSGIMiddleware (UserForGenre))
main_app.mount("/UsersNotRecommend", WSGIMiddleware (UsersNotRecommend))
main_app.mount("/UsersRecommend", WSGIMiddleware (UsersRecommend))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(main_app, host="0.0.0.0", port=10000)


