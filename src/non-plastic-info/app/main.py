from fastapi import FastAPI

non_plastic_info_api = FastAPI()


@non_plastic_info_api.get("/")
async def root():
    return {"message": "Hello World"}


@non_plastic_info_api.get("/items")
async def read_items():
    return [{"item_id1": "foo"}, {"item_id2": "foo2"}]


@non_plastic_info_api.get("/items/{item_id}")
async def read_item_by_id(item_id):
    return {"item_id": item_id}

