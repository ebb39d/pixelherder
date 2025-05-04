from app import app


@app.route("/")
@app.route("/index")
def index():
    return "Pixel Herder: Where Your Creative Story Unfolds"
