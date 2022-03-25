import pathlib
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from api.routers import task, done
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

# pathlib.Pathを使って、staticディレクトリの絶対パスを取得
PATH_STATIC = str(pathlib.Path(__file__).resolve().parent / "static")

app = FastAPI()
app.include_router(task.router)
app.include_router(done.router)

#app.mount(
#    "/static",
#    StaticFiles(directory=Path(__file__).parent.parent.absolute() / "static"),
#    name="static",
#)
#app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount('/static', StaticFiles(directory=PATH_STATIC), name='static')
#templates = Jinja2Templates(directory='templates')
templates = Jinja2Templates(directory=str(Path(BASE_DIR, 'templates')))

#def https_url_for(request: Request, name: str, **path_params: Any) -> str:
#    http_url = request.url_for(name, **path_params)
#    # Replace 'http' with 'https'
#    return http_url.replace("http", "https", 1)
#
#templates.env.globals["https_url_for"] = https_url_for

@app.get('/', response_class=HTMLResponse)
async def read_index(request: Request):
    return templates.TemplateResponse('index.html',
                            context={'request': request,
                                     'title': 'イカスミエギンガーZ Activity',
                                     'description': '鹿児島県の長島近辺で週末フィッシングを満喫中',
                                     'subtitle1': '週末エギンガー &amp; パドラー',
                                     'subtitle2': '釣行ダイアリー',
                                     'h1': 'エギング・ジギング　長島海中探検 カヤックで釣りしながら浮かんでます',
                                     'author': '@CyberMameCAN'
                                    })
@app.get("/hello")
async def hello():
    return {"message": "hello world!!"}