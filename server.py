import json
import managers
from flask import Flask, request, make_response

app = Flask(__name__)


@app.route("/chars/<string:char_encoding>", methods=["GET"])
def get_character(char_encoding: str):
    """Returns the encoded utf-8 symbol
    char_encoding: A number representing a symbol in utf-8 encoding system
    """
    if request.method == "GET":
        db = managers.DBmanager()
        try:
            character = db.symbol_query(char_encoding)
        except KeyError:
            response = make_response("")
            response.status = 404
            return response
        character = json.dumps(character)
        response = make_response(character)
        response.content_type = "application/json"
        return response


@app.route("/codes/<string:char>", methods=["GET"])
def get_encoding(char: str):
    """Returns the encoding of a utf-8 symbol
    char: A utf-8 encoded symbol
    """
    if request.method == "GET":
        db = managers.DBmanager()
        try:
            encoding = db.encoding_query(char)
        except KeyError:
            response = make_response("")
            response.status = 404
            return response
        encoding = json.dumps(encoding)
        response = make_response(encoding)
        response.content_type = "application/json"
        return response


if __name__ == "__main__":
    app.run()
