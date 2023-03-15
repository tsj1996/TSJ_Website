# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 17:35:47 2023

@author: stan43
"""
from flask import Flask, request, url_for, redirect, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

#@app.route('/')    
#def index_2():
    #return render_template('index_2.html')
        

#@app.route('/cool_form', methods=['GET', 'POST'])
@app.route('/index_next.html', methods=['GET', 'POST'])
#def cool_form():
def index_next():
    if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('index'))

    # show the form, it wasn't submitted
    #return render_template('cool_form.html')
    return render_template('index_next.html')


@app.route('/index_next_2.html', methods=['GET', 'POST'])
#def cool_form():
def index_next_2():
    if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('index_2'))

    # show the form, it wasn't submitted
    #return render_template('cool_form.html')
    return render_template('index_next_2.html')



if __name__ == "__main__":
    app.run(debug=True)