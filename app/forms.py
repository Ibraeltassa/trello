from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegisterForm(FlaskForm):
    username = StringField("Usuário", validators=[DataRequired(), Length(min=3, max=50)])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Senha", validators=[DataRequired()])
    confirm_password = PasswordField("Confirmar Senha", validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField("Cadastrar")

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Senha", validators=[DataRequired()])
    submit = SubmitField("Login")

class TaskForm(FlaskForm):
    title = StringField("Título", validators=[DataRequired()])
    description = TextAreaField("Descrição")
    status = SelectField("Status", choices=[("pendente", "Pendente"), ("em andamento", "Em andamento"), ("concluída", "Concluída")])
    submit = SubmitField("Salvar")
