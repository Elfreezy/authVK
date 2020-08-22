from flask import render_template, redirect, request, url_for
from flask_login import logout_user, current_user, login_user, login_required

from app import app
from app.oauth import VKSingIn
from app.logic import get_vk_user, get_friends


@app.route('/', methods=['POST', 'GET'])
@app.route('/index', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        return VKSingIn().authorize()

    if current_user.is_authenticated:
        return redirect(url_for('profile'))

    return render_template('auth.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    code = request.args.get('code') or ''
    if code:
        response = VKSingIn().get_token(code=code).json()
        user = get_vk_user(response)
        login_user(user, remember=True)
        return redirect(url_for('profile'))

    return redirect(url_for('index'))


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


# Добавить slug??
@app.route('/profile')
@login_required
def profile():
    try:
        friends_id = get_friends(current_user.token)
    except:
        # Если токен устарел
        return redirect(url_for('logout'))

    return render_template('profile.html', friends_id=friends_id)

