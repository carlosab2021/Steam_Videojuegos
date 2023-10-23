from fastapi import FastAPI
from app.PlayTimeGenre import app as PlayTimeGenre
from app.sentiment_analysis import app as SentimentAnalysis
from app.UserForGenre import app as UserForGenre
from app.UsersNotRecommend import app as UsersNotRecommend
from app.UsersRecommend import app as UsersRecommend

app = FastAPI()

# Monta las subaplicaciones FastAPI en sus rutas respectivas
app.mount("/PlayTimeGenre", PlayTimeGenre)
app.mount("/sentiment_analysis", SentimentAnalysis)
app.mount("/UserForGenre", UserForGenre)
app.mount("/UsersNotRecommend", UsersNotRecommend)
app.mount("/UsersRecommend", UsersRecommend)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)

