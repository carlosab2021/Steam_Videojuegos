from fastapi import FastAPI
from app.PlayTimeGenre import app as PlayTimeGenre
from app.sentiment_analysis import app as sentiment_analysis
from app.UserForGenre import app as UserForGenre
from app.UsersNotRecommend import app as UsersNotRecommend
from app.UsersRecommend import app as UsersRecommend

main_app = FastAPI()

# se monta las aplicaciones
main_app.mount("/PlayTimeGenre", PlayTimeGenre)
main_app.mount("/sentiment_analysis", sentiment_analysis)
main_app.mount("/UserForGenre", UserForGenre)
main_app.mount("/UsersNotRecommend", UsersNotRecommend)
main_app.mount("/UsersRecommend", UsersRecommend)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(main_app, host="0.0.0.0", port=10000)

