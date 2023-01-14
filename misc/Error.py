
from tools.iPrint import *

class Error:
    error_list = {
        10000: {
            "typer": "error",
            "model": "models",
            "title": "Invalid or Unregisted model(s).", 
            "solve": ""
        },
        20001: {
            "typer": "error",
            "model": "Dellib",
            "title": "Deleting error!", 
            "solve": "Please check pip\'s environment"
        },
    }
    def printError(code: int):
        err = Error.error_list[code]
        model = err["model"]
        title = err["title"]
        solve = err["solve"]
        typer = err["typer"]
        iPrintLog(title,modelName=model,typer=typer)
        if solve: iPrintLog(solve,modelName=model,typer="info")
