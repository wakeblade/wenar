"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from flask import request,jsonify
from demo import app

@app.route("/get_my_ip", methods=["GET"])
def get_my_ip():
    return jsonify({'ip': request.remote_addr}), 200

@app.before_request
def before_request():
    request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
    ip = request.remote_addr
    url = request.referrer
    print(ip)
    print(url)

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )
