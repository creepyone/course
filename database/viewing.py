import flask as flask

app = flask.Flask("__main__")


@app.route("/", methods=["GET"])
def main_page():
    return flask.render_template()

if __name__ == "__main__":
    app.run()
