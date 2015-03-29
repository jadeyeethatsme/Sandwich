from flask import Flask, render_template, url_for, request, render_template 
from wtforms.fields import TextField, BooleanField, SelectMultipleField, SubmitField
from wtforms.validators import Required 

from flask import Flask, render_template_string
from wtforms import SelectMultipleField, Form, SelectField, validators
from wtforms import widgets

app = Flask(__name__)
#app.config.from_object(__name__)

snack_data = [('Snickers','Snickers'), ('Chips','Chips'), ('Kit Kat','Kit Kat')]
bread_data = [('None','None'), ('White bread','White bread'), ('Whole wheat','Whole wheat')]
filling_data = [('Brown sticky stuff','Brown sticky stuff'), ('Strawberry jelly','Strawberry jelly')]

class SandwichForm(Form):
	snack = SelectMultipleField(
		choices=snack_data,
		option_widget = widgets.CheckboxInput(),
		widget=widgets.ListWidget(prefix_label=False)
		)
	bread = SelectField(
		'Pick Things!',
		choices=bread_data,
		#option_widget = widgets.CheckboxInput(),
		#widget=widgets.ListWidget(prefix_label=False)
		)
	filling = SelectMultipleField(
		choices=filling_data,
		option_widget = widgets.CheckboxInput(),
		widget=widgets.ListWidget(prefix_label=False)	
		)

class BaseForm(Form):
	submit_button = SubmitField('Submit')

@app.route('/')
def home():
	form = SandwichForm()
	return render_template('index.html', form=form)


@app.route('/confirm', methods=['post'])
def confirm():
	for item in request.form:
		print item

	print request.form
	return render_template('confirm.html')


@app.route('/hello')
def hello():
	return 'Hello World'

@app.route('/user/<username>')
#def show_user_profile(username):
def profile(username):
	#show the user profile for that user
	return'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
	#show the post with the given id, the id is an integer
	return 'Post %d' % post_id

@app.route('/projects/')
def projects():
	return 'The project page'

@app.route('/about/')
def about():
	return 'The about page'

if __name__ == '__main__':
	app.run(debug=True)
