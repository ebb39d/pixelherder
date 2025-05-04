from app import app


@app.route("/")
@app.route("/inspiration")
def inspiration_feed():
    return "Pixel Herder: Where Your Creative Story Unfolds"
