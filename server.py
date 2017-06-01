from flask import Flask, render_template, request, redirect, session
from random import randint


app=Flask(__name__)
app.secret_key = "ThisIsSecret"

@app.route('/')
def welcome():
	session['wins'] = 0
	session['losses'] = 0
	session['ties'] = 0


	return render_template('welcome.html')



@app.route('/click', methods=['POST'])
def play():
	random_num = randint(1,3)
	new_rand = str(random_num)
	user = request.form['action'] 

	if user == new_rand:
		result = "it's a tie"
		session['ties'] += 1
	elif user == "1" and new_rand == "2":
		result = "you loose"
		session['losses'] += 1
	elif user == "1" and new_rand == "3":
		result = "you win"
		session['wins'] += 1
	elif user == "2" and new_rand == "1":
		result = "you win"
		session['wins'] += 1
	elif user == "2" and new_rand == "3":
		result = "you loose"
		session['losses'] += 1
	elif user == "3" and new_rand == "1":
		result = "you loose"
		session['losses'] += 1
	elif user == "3" and new_rand == "2":
		result = "you win"
		session['wins'] += 1

	return render_template('welcome.html', result=result)
	








app.run(debug=True)

#1 = rock
#2 = paper
#3 = scissors