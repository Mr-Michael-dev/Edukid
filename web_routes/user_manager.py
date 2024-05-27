#!/usr/bin/python3
"""defines routes for managing user rgistration and login"""
from models import storage
from models.user import User
from flask import render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user
from web_routes import web_routes
from get_videos import get_videos


web_routes.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        full_name = request.form['full_name']
        email = request.form['email']
        password = request.form['password']
        new_user = User(username=username, email=email,
                        password=password, full_name=full_name)
        new_user.save()
        return redirect(url_for('login'))
    return render_template('register.html')

web_routes.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username, password=password).first()
        if user:
            login_user(user)
            return redirect(url_for('index'))
        else:
            flash('Invalid credentials')
    return render_template('login.html')

web_routes.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))
