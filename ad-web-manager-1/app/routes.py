from flask import Blueprint, render_template, request, redirect, url_for, flash
from .ad_utils import add_user, delete_user, batch_add_users, batch_delete_users
from .forms import UserForm, BatchUserForm

app = Blueprint('app', __name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_user', methods=['GET', 'POST'])
def add_user_route():
    form = UserForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        try:
            add_user(username, password)
            flash('User added successfully!', 'success')
        except Exception as e:
            flash(f'Error adding user: {str(e)}', 'danger')
        return redirect(url_for('app.index'))
    return render_template('add_user.html', form=form)

@app.route('/delete_user', methods=['GET', 'POST'])
def delete_user_route():
    form = UserForm()
    if form.validate_on_submit():
        username = form.username.data
        try:
            delete_user(username)
            flash('User deleted successfully!', 'success')
        except Exception as e:
            flash(f'Error deleting user: {str(e)}', 'danger')
        return redirect(url_for('app.index'))
    return render_template('delete_user.html', form=form)

@app.route('/batch_add', methods=['GET', 'POST'])
def batch_add_route():
    form = BatchUserForm()
    if form.validate_on_submit():
        file = form.file.data
        try:
            batch_add_users(file)
            flash('Batch user addition successful!', 'success')
        except Exception as e:
            flash(f'Error in batch addition: {str(e)}', 'danger')
        return redirect(url_for('app.index'))
    return render_template('batch_add.html', form=form)

@app.route('/batch_delete', methods=['GET', 'POST'])
def batch_delete_route():
    form = BatchUserForm()
    if form.validate_on_submit():
        usernames = form.usernames.data.splitlines()
        try:
            batch_delete_users(usernames)
            flash('Batch user deletion successful!', 'success')
        except Exception as e:
            flash(f'Error in batch deletion: {str(e)}', 'danger')
        return redirect(url_for('app.index'))
    return render_template('batch_delete.html', form=form)