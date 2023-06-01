from flask import request
from my_app.application import app
from my_app.database import db, Account, Animal

@app.route("/registration", methods=["POST"])
def create_account():
    request_data = request.get_json()
    if request_data["firstName"] == "" or request_data["lastName"] == ""\
            or request_data["email"] == "" or request_data["password"] == "":
        return ("", 400)
    elif "@" not in request_data["email"] or request_data["email"][-1] == "@":
        return ("", 400)
    elif Account.query.filter_by(firstName=request_data["firstName"], lastName=request_data["lastName"]).first():
        return ("", 403)
    elif Account.query.filter_by(email=request_data["email"]).first():
        return ("", 409)
    else:
        new_acc = Account(
            firstName=request_data["firstName"],
            lastName=request_data["lastName"],
            email=request_data["email"],
            password=request_data["password"]
        )
        db.session.add(new_acc)
        db.session.commit()
        response = {
            "id": new_acc.id,
            "firstName": new_acc.firstName,
            "lastName": new_acc.lastName,
            "email": new_acc.email
        }
        return (response, 201)

@app.route("/accounts/<int:accountId>", methods=["GET"])
def get_user(accountId):
    if accountId == 0:
        return ("", 400)
    elif not Account.query.filter_by(id=accountId).first():
        return ("", 404)
    elif Account.query.filter_by(id=accountId).first():
        selected_acc = Account.query.filter_by(id=accountId).first()
        response = {
            "id": selected_acc.id,
            "firstName": selected_acc.firstName,
            "lastName": selected_acc.lastName,
            "email": selected_acc.email
        }
        return (response, 200)
    else:
        return ("", 401)

@app.route("/accounts/search", methods=["GET"])
def get_user_parameters():
    name = request.args.get('firstName')
    surname = request.args.get('lastName')
    acc = Account.query.filter_by(firstName=name, lastName=surname).first()

    if not acc:
        return ("", 401)
    else:
        response = {
            "id": acc.id,
            "firstName": acc.firstName,
            "lastName": acc.lastName,
            "email": acc.email
        }
        return (response, 200)

@app.route("/accounts/<int:accountId>", methods=["PUT"])
def update_info(accountId):
    request_data = request.get_json()

    if accountId <= 0 or request_data["firstName"] == "" or request_data["lastName"] == ""\
            or request_data["email"] == "" or request_data["password"] == "":
        return ("", 400)
    elif not Account.query.filter_by(id=accountId).first():
        return ("", 403)
    else:
        selected_acc = Account.query.filter_by(id=accountId).first()
        if accountId == selected_acc.id and request_data["password"] != selected_acc.password:
            return ("", 401)
        elif Account.query.filter_by(email=request_data["email"]).first() and \
                Account.query.filter_by(email=request_data["email"]).first().id != accountId:
            return ("", 409)
        else:
            selected_acc.firstName = request_data["firstName"]
            selected_acc.lastName = request_data["lastName"]
            selected_acc.email = request_data["email"]
            selected_acc.password = request_data["password"]
            db.session.commit()

            response = {
                "id": selected_acc.id,
                "firstName": selected_acc.firstName,
                "lastName": selected_acc.lastName,
                "email": selected_acc.email
            }
            return (response, 200)

@app.route("/accounts/<int:accountId>", methods=["DELETE"])
def delete_account(accountId):
    animal_chipper = Animal.query.filter_by(chipperId=accountId).first()

    if accountId == 0 or animal_chipper:
        return ("", 400)
    elif not Account.query.filter_by(id=accountId).first():
        return ("", 403)
    else:
        selected_acc = Account.query.filter_by(id=accountId).first()
        db.session.delete(selected_acc)
        db.session.commit()
        return ("", 200)


