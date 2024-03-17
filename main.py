from fastapi import FastAPI, Query
from requests_oauthlib import OAuth2Session
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi import  HTTPException

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/github/callback")
async def github_callback(ci: str = Query(default=None), cs: str = Query(default=None), ruri: str = Query(default=None), code: str = Query(default=None)):
    if not ci:
        raise HTTPException(status_code=400, detail={"status": "400", "msg": "Missing client_id","key_missing":"ci"}) 
    if not cs:
        raise HTTPException(status_code=400, detail={"status": "400", "msg": "Missing client_secret","key_missing":"cs"})
    if not ruri:
        raise HTTPException(status_code=400, detail={"status": "400", "msg": "Missing redirect_uri","key_missing":"ruri"})
    if not code:
        raise HTTPException(status_code=400, detail={"status": "400", "msg": "Missing code","key_missing":"code"})
    github = OAuth2Session(client_id=ci,  redirect_uri=ruri)
    try:
        token = github.fetch_token(
            token_url="https://github.com/login/oauth/access_token",
            client_secret=cs,
            code=code
        )
        return JSONResponse({"details":{{"status": "200", "msg": "Success","access_token": token["access_token"]}}})
    except Exception as e:
        raise HTTPException(status_code=401, detail={"status": "401", "msg": "Error","error": str(e)})
    
