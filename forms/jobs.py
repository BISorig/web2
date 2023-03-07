from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms import BooleanField, SubmitField
from wtforms.validators import DataRequired


class JobsForm(FlaskForm):
    team_leader = StringField('ID руководителя', validators=[DataRequired()])
    title = StringField("Название работы", validators=[DataRequired()])
    job = TextAreaField('Описание работы', validators=[DataRequired()])
    work_size = StringField('Объём работы в часах')
    collaborators = StringField('Список ID участников')
    start_date = StringField('Дата начала')
    end_date = StringField('Дата окончания')
    is_finished = BooleanField('Работа завершена')
    submit = SubmitField('Применить')