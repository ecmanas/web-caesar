from flask import Flask, request
from caesar import rotate_string
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
     <form method='POST'>
                <label for="rotate_by">Rotate by: </label>
                <input id="rotate_by" type="text" name="rot" value="0"  />
                <textarea name="text">{0}</textarea>
                <input type="submit" value="Submit querry">
            </form>
    </body>
</html>

"""


@app.route("/")
def index():
    return form.format('')

@app.route("/", methods=['POST'])
def encrypt():
    rot_1st = cgi.escape(request.form["rot"])
    text = cgi.escape(request.form["text"])
    rot = int(rot_1st)

    content = rotate_string(text, rot)
    
    return form.format(content)

app.run()
