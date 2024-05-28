#!/usr/bin/python3
"""defines routes for managing user rgistration and login"""
from models.user import User
from models import storage
from flask import render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user
from web_routes import web_routes
from sqlalchemy.exc import IntegrityError
from ..app import app


@web_routes.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        full_name = request.form['full_name']
        email = request.form['email']
        password = request.form['password']
        user = User.with_password(email=email, password=password,
                                  full_name=full_name, username=username)

        try:
            user.save()
        except IntegrityError as e:
            app.logger.exception(e)
            storage.rollback()
            flash("This username is already in use")
            return redirect(url_for("signup"))

        flash("Thanks for registering, you can save and watch later")
        return redirect(url_for('web_routes.login'))
    return render_template('register.html')


@web_routes.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.get_by_password(username=username, password=password)
        if user:
            flash('You have succesfully logged in!')
            login_user(user)
            return redirect(url_for('web_routes.index'))
        flash('Invalid credentials')
        return redirect(url_for('web_routes.login'))
    return render_template('login.html')


@web_routes.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You are logged out')
    return redirect(url_for('web_routes.index'))
