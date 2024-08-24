from fastapi import FastAPI, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from service.servise import work_with_vpn
app = FastAPI()

# Настройка CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Разрешить запросы с любого домена. Укажите конкретные домены, если необходимо.
    allow_credentials=True,
    allow_methods=["*"],  # Разрешить все методы (GET, POST и т.д.)
    allow_headers=["*"],  # Разрешить все заголовки
)

@app.get("/")
async def home():
    pass


@app.get("/backend/{name_country}/{user_name}/")
def get_vpn_config(name_country:str,user_name:str):
    return work_with_vpn.get_comfig(name_country,user_name)


