from flask import Blueprint, render_template, request, redirect, url_for
from . import db
from .models import Request
import os
import requests

API_KEY = os.getenv("TMDB_API_KEY")
TMDB_BASE_URL = "https://api.themoviedb.org/3"

main = Blueprint('main', __name__)

@main.route('/')
def index():
    queue = Request.query.all()
    return render_template('index.html', queue=queue)

@main.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        query = request.form.get('query')
        if query:
            search_url = f"{TMDB_BASE_URL}/search/multi?api_key={API_KEY}&query={query}"
            response = requests.get(search_url).json()
            return render_template('search.html', results=response.get('results', []))
    return render_template('search.html', results=[])

@main.route('/add', methods=['POST'])
def add():
    title = request.form.get('title')
    tmdb_id = request.form.get('tmdb_id')
    media_type = request.form.get('media_type')

    if title and tmdb_id and media_type:
        new_request = Request(title=title, type=media_type, tmdb_id=tmdb_id)
        db.session.add(new_request)
        db.session.commit()
    return redirect(url_for('main.index'))
