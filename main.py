from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
	<head>
		<style>
			form {
				background-color: #eee;
				padding: 20px;
				margin: 0 auto;
				width: 540px;
				font: 16px sans-serif;
				border-radius: 10px;
			}
			textarea {
				margin: 10px 0;
				width: 540px;
				height: 120px;
			}
		</style>
	</head>
	<body>
		<!-- create your form here -->
		<form method='POST'>
			
			<!-- rotation input -->
			<label>Rotate by:
				<input name="rot" type="text" />
			</label>

			<!-- text to encrypt input -->
			<textarea name="text"></textarea>

			<input type="submit" value="submit" />

	</body>
</html>

"""

@app.route('/')
def index():
	return form

@app.route('/', methods=['POST'])
def encrypt():
	rot = request.form['rot']
	rot = int(rot)
	text = request.form['text']

	rotated_text = rotate_string(text, rot)

	return '<h1>' + str(rotated_text) + '</h1>'

# Getting error that int is not iterable. Issue with converting form input for rot into something
# that can be used in the rotated_text function.


'''
To process the form, define a new function encrypt in main.py. 
Add an @app.route decorator to configure the function to receive requests at the root path "/", 
and with methods=['POST']. ---DONE---

When the form is submitted, the request will contain the parameters rot and text.
In order to access these, we need Flask's request object. To import it,
modify the topmost import statement to include this object. ---DONE---

Within encrypt, store the values of these request parameters in local variables,
converting data types as necessary. ---DONE---

Then, encrypt the value of the text parameter using rotate_string. Return the encrypted 
string wrapped in <h1> tags, to be rendered in the browser. ---DONE---

Before embarking on our final task, start up the application and test that everything
you've done so far works. This is also a good time to commit your changes to your local
Git repo.





'''
app.run()














