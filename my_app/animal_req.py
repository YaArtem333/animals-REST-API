from flask import request
from my_app.application import app
from my_app.database import db, Animal, Account, Types

def get_parameters():
    request_data = request.get_json()
    if request_data["email"] == "" or request_data["password"] == "":
        return ("", 400)
    else:
        acc_email = Account.query.filter_by(email=request_data['email']).first()
        acc = Account.query.filter_by(email=request_data['email'], password=request_data['password']).first()
        if not acc_email:
            return ("", 404)
        elif not acc:
            return ("", 401)


@app.route("/animals", methods=["POST"])
def create_animal():
    if get_parameters():
        return get_parameters()
    request_data = request.get_json()
    acc = Account.query.filter_by(email=request_data['email'], password=request_data['password']).first()
    if request_data["name"] == "" or request_data["weight"] == "" or request_data["weight"] == 0 \
            or request_data["gender"] == "" or request_data["gender"] == 0 \
            or request_data["animal_type"] == "":
        return ("", 400)
    else:
        anml = Animal.query.filter_by(name=request_data['name']).first()
        if anml:
            return ("", 409)
        else:
            new_animal = Animal(
                name=request_data["name"],
                weight=request_data["weight"],
                gender=request_data["gender"],
                animal_type=request_data["animal_type"],
                chipperId=acc.id
            )
            tps = Types.query.filter_by(types=request_data['animal_type']).first()
            if not tps:
                new_type = Types(
                    types=request_data['animal_type']
                )
                db.session.add(new_type)
            db.session.add(new_animal)
            db.session.commit()
            response = {
                "id": new_animal.id,
                "name": new_animal.name,
                "weight": new_animal.weight,
                "gender": new_animal.gender,
                "animal_type": new_animal.animal_type,
                "chipperId": new_animal.chipperId
            }
            return (response, 201)

@app.route("/animals/<int:animalId>", methods=["DELETE"])
def delete_animal(animalId):
    if get_parameters():
        return get_parameters()
    if animalId == 0:
        return ("", 400)
    elif not Animal.query.filter_by(id=animalId).first():
        return ("", 403)
    else:
        selected_animal = Animal.query.filter_by(id=animalId).first()
        tp = selected_animal.animal_type
        db.session.delete(selected_animal)
        db.session.commit()
        if not Animal.query.filter_by(animal_type=tp).first():
            db.session.delete(Types.query.filter_by(types=tp).first())
            db.session.commit()
        return ("", 200)

@app.route("/animals/<int:animalId>", methods=["GET"])
def get_animal(animalId):
    if get_parameters():
        return get_parameters()
    if animalId == 0:
        return ("", 400)
    elif not Animal.query.filter_by(id=animalId).first():
        return ("", 404)
    elif Animal.query.filter_by(id=animalId).first():
        selected_anml = Animal.query.filter_by(id=animalId).first()
        response = {
            "id": selected_anml.id,
            "name": selected_anml.name,
            "weight": selected_anml.weight,
            "gender": selected_anml.gender,
            "animal_type": selected_anml.animal_type,
            "chipperId": selected_anml.chipperId
        }
        return (response, 200)
    else:
        return ("", 401)

@app.route("/animals/search", methods=["GET"])
def get_animal_parameters():
    if get_parameters():
        return get_parameters()
    name = request.args.get('name')
    anml = Animal.query.filter_by(name=name).first()
    if not anml:
        return ("", 401)
    else:
        response = {
            "id": anml.id,
            "name": anml.name,
            "weight": anml.weight,
            "gender": anml.gender,
            "animal_type": anml.animal_type,
            "chipperId": anml.chipperId
        }
        return (response, 200)

@app.route("/animals/<int:animalId>", methods=["PUT"])
def update_animal_info(animalId):
    if get_parameters():
        return get_parameters()
    request_data = request.get_json()
    if animalId <= 0 or request_data["name"] == "" \
            or request_data["weight"] == "" or request_data["weight"] == 0 \
            or request_data["gender"] == "" or request_data["gender"] == 0 \
            or request_data["animal_type"] == "":
        return ("", 400)
    elif not Animal.query.filter_by(id=animalId).first():
        return ("", 403)
    else:
        selected_anml = Animal.query.filter_by(id=animalId).first()
        if Animal.query.filter_by(name=request_data["name"]).first() and \
                Animal.query.filter_by(name=request_data["name"]).first().id != animalId:
            return ("", 409)
        else:
            acc = Account.query.filter_by(email=request_data['email'], password=request_data['password']).first()
            selected_anml.name = request_data["name"]
            selected_anml.weight = request_data["weight"]
            selected_anml.gender = request_data["gender"]
            selected_anml.animal_type = request_data["animal_type"]
            chipperId = acc.id
            db.session.commit()

            response = {
                "id": selected_anml.id,
                "name": selected_anml.name,
                "weight": selected_anml.weight,
                "gender": selected_anml.gender,
                "animal_type": selected_anml.animal_type,
                "chipperId": selected_anml.chipperId
            }
            return (response, 200)


