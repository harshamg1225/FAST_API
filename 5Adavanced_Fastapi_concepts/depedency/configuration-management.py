from fastapi import FastAPI, Depends


app = FastAPI()


class Settings:
    def __init__(self):

        self.api_key = "My-secret"
        self.debug = True


def get_settings():
    return Settings()


@app.get("/config")
def get_config(setting: Settings = Depends(get_settings)):

    return {"configuration": setting.api_key}
