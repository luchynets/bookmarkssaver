from fastapi import FastAPI
from database import DataBase
from datamodels import Bookmark, Category
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()
db = DataBase()

@app.get("/main", tags=["General"])
def main_page():
    return {
        "message": "Welcome to the Bookmark API",
        "docs": "/docs",
        "version": "1.0.0"
    }

@app.get("/bookmarks", tags=["Bookmarks"])
def get_bookmarks():
    return db.bk_get()

@app.get("/categories", tags=["Bookmarks"])
def get_bookmarks():
    return db.catgrs_get()

@app.get("/bookmarks/{id}", tags=["Bookmarks"])
def get_bookmarks(id: int):
    return db.bk_get_by_id(id)

@app.post("/addbookmark", tags=["Adding info"])
def add_bookmark(bookmark: Bookmark):
    return db.add_bk(bookmark.name, bookmark.url, bookmark.type)

@app.post("/addcategory", tags=["Adding info"])
def add_category(category: Category):
    return db.add_category(category.name)

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def read_index():
    return FileResponse("static/index.html")