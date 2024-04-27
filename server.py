from fastapi import FastAPI, HTTPException
from predection import predect_new_category
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

class Message(BaseModel):
    message: str

@app.post('/categorize')
def predict_category(data: Message):
    user_message = data.message
    # this is the only changed part it's just to ensure that the input is a list of strings (even if it's just one string)
    #make sure to update this part or the code won't work
    article = [user_message]
    category = predect_new_category(article)
    return {'category': category}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
