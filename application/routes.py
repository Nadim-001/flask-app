from application import app, db
from flask import request, jsonify
from application.models import FriendsCharacter

def format_character(character):
    return {
        "id":character.id,
        "name": character.name,
        "age": character.age,
        "catch_phrase": character.catch_phrase
    }

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/characters", methods=['POST'])
def create_character():
    #retrieve body -req.body
    data = request.json
    # data -> {name: "ross", age: , catch_phrase: }
    character = FriendsCharacter(data["name"], data["age"], data["catch_phrase"])
    # add the character
    db.session.add(character)
    # commit -> send the character to the database
    db.session.commit()
    # Send back a json response
    # jsonify -> turns JSON output into a Response object
    return jsonify(id=character.id, name=character.name, age=character.age, catch_phrase=character.catch_phrase)

# GET route to retrieve all the characters
@app.route("/characters")
def get_characters():
    characters = FriendsCharacter.query.all()
    character_list = []
    for character in characters:
        character_list.append(format_character(character))
    return {'characters': character_list}

@app.route("/characters/<id>")
def get_characters_by_id(id):
    character = FriendsCharacter.query.filter_by(id=id).first()
    return jsonify(id=character.id, name=character.name, age=character.age, catch_phrase=character.catch_phrase)

@app.route("/characters/<id>", methods=["DELETE"])
def delete_character(id):
    character = FriendsCharacter.query.filter_by(id=id).first()
    db.session.delete(character)
    db.session.commit()
    return "character deleted"



@app.route("/characters/<id>", methods=["PATCH"])
def update_character(id):
    # retrieve character by id AND UPDATE
    character = FriendsCharacter.query.filter_by(id=id)
    data = request.json
    character.update(
        dict(name=data["name"], age=data["age"], catch_phrase=data["catch_phrase"])
    )
    # commit change to database
    db.session.commit()
    # retrieve the updata character
    updated_character = FriendsCharacter.query.filter_by(id=id).first()
    # return json object of updated character
    return jsonify(
        id=updated_character.id,
        name=updated_character.name,
        age=updated_character.age,
        catch_phrase=updated_character.catch_phrase,
    )
