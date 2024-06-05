#!/usr/bin/python3
"""defines routes for managing user rgistration and login"""
from models.user import User
from models import storage
from flask import render_template, redirect
from flask import url_for, request, flash, current_app
from flask_login import login_user, logout_user, login_required
import bcrypt
from web_routes import web_routes
from sqlalchemy.exc import IntegrityError


@web_routes.route('/register', methods=['GET', 'POST'])
def register():
    """register a new user"""
    if request.method == 'POST':
        username = request.form['username']
        full_name = request.form['full_name']
        password = request.form['password']
        user = User.with_password(password=password,
                                  full_name=full_name, username=username)

        try:
            user.save()
        except IntegrityError as e:
            current_app.logger.exception(e)
            storage.rollback()
            flash("This username is already in use")
            return redirect(url_for("web_routes.register"))

        flash("Thanks for registering, please login")
        return redirect(url_for('web_routes.login'))
    return render_template('register.html')


@web_routes.route('/login', methods=['GET', 'POST'])
def login():
    """login a user"""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        users = [user for user in storage.all(User).values()]
        for user in users:
            if user.username == username and bcrypt.checkpw(
                    password.encode("utf-8"), user.password.encode("utf-8")):

                flash('You have succesfully logged in!')
                login_user(user)
                return redirect(url_for('web_routes.user_profile'))
        flash('Invalid credentials')
        return redirect(url_for('web_routes.login'))
    return render_template('login.html')


@web_routes.route('/logout')
@login_required
def logout():
    """logout a user"""
    logout_user()
    flash('You are logged out')
    return redirect(url_for('web_routes.index'))
