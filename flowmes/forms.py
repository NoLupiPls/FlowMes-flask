from flask_wtf import FlaskForm
from wtforms.fields.html5 import DateField
from wtforms import StringField, PasswordField, SubmitField, RadioField, BooleanField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_wtf.file import FileField, FileAllowed
from flowmes.models import User


class RegistrationForm(FlaskForm):
    f_name = StringField('Имя', validators=[DataRequired(), Length(min=2, max=20)], render_kw={"placeholder": "Имя"})
    l_name = StringField('Фамидия', validators=[DataRequired(), Length(min=2, max=20)], render_kw={"placeholder": "Фамилия"})
    email = StringField('Почта', validators=[DataRequired(), Email()], render_kw={"placeholder": "Почта"})
    gender = RadioField('Пол', choices=[('мужчина', 'Мужчина'), ('девушка', 'Девушка')])
    dob = DateField('Дата рождения', format='%Y-%m-%d', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()], render_kw={"placeholder": "Пароль"})
    confirm_password = PasswordField('Повторите пароль', validators=[DataRequired(), EqualTo('password')], render_kw={"placeholder": "Повторите пароль"})
    submit = SubmitField('Зарегистрироваться')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Эта почта уже используется. Пожалуйста, выберите другую.')


class LoginForm(FlaskForm):
    email = StringField('Почта', validators=[DataRequired(), Email()], render_kw={"placeholder": "Почта"})
    password = PasswordField('Пароль', validators=[DataRequired()], render_kw={"placeholder": "Пароль"})
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


class PostForm(FlaskForm):
    post = TextAreaField('Say something', validators=[
        DataRequired(), Length(min=1, max=140)], render_kw={"placeholder": "Что Вы хотите написать?"})
    post_image = FileField('Обновить аватар', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Опубликовать')


class EditPostForm(FlaskForm):
    post = TextAreaField('Say something', validators=[
        DataRequired(), Length(min=1, max=140)], render_kw={"placeholder": "Что Вы хотите написать?"})
    post_image = FileField('Обновить аватар', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Опубликовать')


class EditProfilePhotoForm(FlaskForm):
    cover_image = FileField('Добавить ковер фото', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    profile_image = FileField('Добавить аватар', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    submit = SubmitField('Опубликовать')


class EditStoryForm(FlaskForm):
    story_image = FileField('Создать сторис', validators=[DataRequired(), FileAllowed(['jpg', 'png', 'jpeg'])])
    submit = SubmitField('Опубликовать')


class EditProfileForm(FlaskForm):
    f_name = StringField('Имя', validators=[DataRequired()])
    l_name = StringField('Фамилия', validators=[DataRequired()])
    about_me = TextAreaField('Описание', validators=[Length(min=0, max=140)])
    submit = SubmitField('Сохранить')


class EditProfileDetailsForm(FlaskForm):
    school = StringField('Школа', validators=[DataRequired()])
    hometown = StringField('Родом из города', validators=[DataRequired()])
    location = StringField('Проживаете в', validators=[DataRequired()])
    relationship = RadioField('Gender', choices=[('одинок', 'Одинок'), ('женат', 'Женат'), ('в отношениях', 'В отношениях')])
    submit = SubmitField('Готово')


class EmptyForm(FlaskForm):
    submit = SubmitField('Готово')


class CommentForm(FlaskForm):
    comment = TextAreaField('comment', validators=[
        DataRequired(), Length(min=1, max=140)], render_kw={"placeholder": "Напишите комментарий"})
    submit = SubmitField('Опубликовать')


class LikeForm(FlaskForm):
    like = TextAreaField('comment', validators=[
        DataRequired(), Length(min=1, max=140)], render_kw={"placeholder": "Напишите комментарий"})
    submit = SubmitField('Опубликовать')


class MessageForm(FlaskForm):
    message = TextAreaField('Message', validators=[DataRequired(), Length(min=0, max=140)], render_kw={"placeholder": "Введите сообщение"})
    image = FileField('Добавить фото', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    submit = SubmitField('Опубликовать')


class RecipientList(FlaskForm):
    recipient = SelectField('Выберите получателя', validators=[DataRequired()])
    submit = SubmitField('Готово')


class ResetPasswordRequestForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')


class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Request Password Reset')
