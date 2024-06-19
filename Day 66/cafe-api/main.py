from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
import requests
import random

API_KEY = "TopSecretAPIKey"

app = Flask(__name__)

##Connect to Database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cafes.db"
db = SQLAlchemy()
db.init_app(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        # #Method 1.
        # dictionary = {}
        # # Loop through each column in the data record
        # for column in self.__table__.columns:
        #     #Create a new dictionary entry;
        #     # where the key is the name of the column
        #     # and the value is the value of the column
        #     dictionary[column.name] = getattr(self, column.name)
        # return dictionary

        # Method 2. Altenatively use Dictionary Comprehension to do the same thing.
        return {
            column.name: getattr(self, column.name) for column in self.__table__.columns
        }


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


## HTTP GET - Read Record
@app.route("/random")
def get_random_cafe():
    result = db.session.execute(db.select(Cafe))
    cafes = result.scalars().all()
    random_cafe = random.choice(cafes)
    # print(random_cafe.name)
    return jsonify(cafe=random_cafe.to_dict())


@app.route("/all")
def get_all_cafes():
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()
    # cafes = []
    # for cafe in all_cafes:
    #     cafes.append(cafe.to_dict())
    # return jsonify(cafes=cafes)
    return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])


@app.route("/search")
def search_cafe():
    desired_location = request.args.get("loc")
    cafes = (
        db.session.execute(db.select(Cafe).where(Cafe.location == desired_location))
        .scalars()
        .all()
    )
    if len(cafes) != 0:
        return jsonify(cafes=[cafe.to_dict() for cafe in cafes])
    else:
        return (
            jsonify(
                error={"Not Found": "Sorry, we don't have a cafe at this location."}
            ),
            404,
        )


## HTTP POST - Create Record
@app.route("/add", methods=["GET", "POST"])
def add_new_cafe():
    if request.method == "POST":
        try:
            new_cafe = Cafe(
                name=request.form.get("name"),
                map_url=request.form.get("map_url"),
                img_url=request.form.get("img_url"),
                location=request.form.get("location"),
                seats=request.form.get("seats"),
                has_toilet=bool(request.form.get("has_toilet")),
                has_wifi=bool(request.form.get("has_wifi")),
                has_sockets=bool(request.form.get("has_sockets")),
                can_take_calls=bool(request.form.get("can_take_calls")),
                coffee_price=request.form.get("coffee_price"),
            )
        except KeyError:
            return jsonify(error={"Bad Request": "Some or all fields were incorrect or missing."})
        else:
            db.session.add(new_cafe)
            db.session.commit()
            return jsonify(response={"Success": "Successfully added the new cafe. "})
    


## HTTP PUT/PATCH - Update Record
@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def update_coffee_price(cafe_id):
    new_price = request.args.get("new_price")
    cafe_to_update = db.get_or_404(Cafe, cafe_id)
    if cafe_to_update:
        cafe_to_update.coffee_price = new_price
        db.session.commit()
        return jsonify(response={"success": "Successfully updated the price."}), 200
    elif not cafe_to_update:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404
    

## HTTP DELETE - Delete Record
@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def remove_closed_cafe(cafe_id):
    api_key = request.args.get("api_key")
    if api_key == API_KEY:
        cafe_to_delete = db.get_or_404(Cafe, cafe_id)
        if cafe_to_delete:
            db.session.delete(cafe_to_delete)
            db.session.commit()
            return jsonify(response={"success": "Successfully deleted the cafe from database."}), 200
        else:
            return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404
    else:
        return jsonify(response={"error": "Sorry, that's not allowed. Make sure you have the correct api_key."}), 403

   

if __name__ == "__main__":
    app.run(debug=True)
