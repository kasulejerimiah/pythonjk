#http://127.0.0.1:8000/docs
#uvicorn item-get:app --reload
from fastapi import FastAPI, Path

#Path is added so you can put a description of sort
app = FastAPI()

inventory = {
    1: {
        "name":"Milk",
        "price":3000,
        "brand":"kidawalime"
    }
}
#THIS WORKED SO AM COMMENTING IT OUT
@app.get("/get-item/{item_id}")
def get_item(item_id: int = Path(None, description="The ID of the item you want to view", gt=0, lt=3)):
    return inventory[item_id]
#QUERY PARAMETOR
#when calling query: you start with a "?" ie:?name=Milk
#forexample: http://127.0.0.1:8000/get-by-name?name=Milk
@app.get("/get-by-name")
def get_item(name:str):
    for item_id in inventory:
        if inventory[item_id]["name"] == name:
            return inventory[item_id]
        return {"data":"Not found"}

@app.get("/get-by-brand")
def get_item(brand:str):
    for item_id in inventory:
        if inventory[item_id]["brand"] == brand:
            return inventory[item_id]
        return {"data":"Not found"}



#@app.get("/get-item/{item_id}/{name}")
#def get_item(item_id: int, name: str):
#    return inventory[item_id]