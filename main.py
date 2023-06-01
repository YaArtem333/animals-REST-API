from my_app.database import create_table
from my_app import app

create_table()

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)

