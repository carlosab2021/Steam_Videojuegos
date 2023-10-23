from fastapi import FastAPI
from app.mi_app import app as mi_app

main_app = FastAPI()

# se monta las aplicaciones
main_app.mount("/PlayTimeGenre", PlayTimeGenre)
main_app.mount("/sentiment_analysis", sentiment_analysis)
main_app.mount("/UserForGenre", UserForGenre)
main_app.mount("/UsersNotRecommend", UsersNotRecommend)
main_app.mount("/UsersRecommend", UsersRecommend)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(main_app, host="0.0.0.0", port=1000)

