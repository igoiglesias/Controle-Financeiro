from app import app
from flask import render_template, flash, redirect, request, url_for
from flask_login import login_user, logout_user, login_required, current_user

from app.models.forms import LoginForm
from app.models.tables import Expense, User


@app.route('/login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated: return redirect(url_for('home'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        print(user.password, form.password.data)
        if user and User.verify_password(user.password, form.password.data):
            login_user(user)
            if request.args.get('next'):
                return redirect(request.args.get('next'))
            return redirect(url_for('home'))
        else:
            print("Tente novamente")
            flash("Credenciais inválidas")

    return render_template('login.html', form=form)

@app.route('/')
@app.route('/home')
@login_required
def home():
    expenses = Expense.query.all()
    incomes = Expense.query.all()
    return render_template('home.html', expenses=expenses, incomes=incomes)

@app.route('/perfil')
@login_required
def perfil():
    return render_template('perfil.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect('login')

@app.route('/register')
def register():
    from app import db
    user = User('Igor Iglesias', 'contato@igoriglesias.com', '1234')
    db.session.add(user)
    db.session.commit()
    flash(f'Usuário {user.name} inserido com sucesso!')
    return redirect(url_for('login'))