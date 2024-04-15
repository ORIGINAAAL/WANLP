from fastapi import FastAPI, HTTPException
from predection import predect_new_category
from pydantic import BaseModel

app = FastAPI()

class Message(BaseModel):
    message: str

@app.post('/categorize')
def predect_category(data: Message):
    user_message = [data.message]  

    bot_response = predect_new_category(user_message)

    return {'category': bot_response}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
