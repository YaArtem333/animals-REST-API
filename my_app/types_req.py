from my_app.application import app
from my_app.database import Types

@app.route("/types", methods=["GET"])
def get_types():
    big_response = {}
    typess = Types.query.all()
    sch = 0
    for i in typess:
        response = {
            "id": i.id,
            "type": i.types
        }
        big_response[sch] = response
        sch+=1
    return big_response



