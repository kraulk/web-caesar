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
		<!-- create your form here -->
		<form method='POST'>
			
			<!-- rotation input -->
			<label>Rotate by:
				<input name="rot" type="text" value="{rotate}"/>
			</label>

			<!-- text to encrypt input -->
			<textarea name="text">{text}</textarea>

			<input type="submit" value="submit" />

	</body>
</html>

"""

@app.route('/')
def index():
	return form.format(rotate='', text='')

@app.route('/', methods=['POST'])
def encrypt():
	rot = request.form['rot']
	rot = int(rot)
	text = request.form['text']

	rotated_text = rotate_string(text, rot)
	# Return the form with Caesar rotated text
	# in textarea. Keep rotation amount in input.

	return form.format(rotate=rot, text=rotated_text)

app.run()














