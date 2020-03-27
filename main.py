from module import create_app, db


if __name__ == "__main__":
    create_app().run(debug=True, port=4000, use_reloader=True)
