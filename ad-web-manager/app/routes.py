from flask import Blueprint, render_template, request, redirect, url_for
from app.ad_utils import add_users_to_ad, delete_users_from_ad

bp = Blueprint('routes', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/users', methods=['GET', 'POST'])
def users():
    if request.method == 'POST':
        action = request.form.get('action')
        users_list = request.form.get('users').splitlines()
        
        if action == 'add':
            add_users_to_ad(users_list)
        elif action == 'delete':
            delete_users_from_ad(users_list)
        
        return redirect(url_for('routes.users'))
    
    return render_template('users.html')