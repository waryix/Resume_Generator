# app/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, FileField
from wtforms.validators import DataRequired, Email, Length, EqualTo
from wtforms import TextAreaField

class SignupForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[
        DataRequired(), EqualTo('password', message='Passwords must match.')
    ])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class ResumeForm(FlaskForm):
    full_name = StringField('Full Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = StringField('Phone', validators=[DataRequired()])
    address = TextAreaField('Address', validators=[DataRequired()], render_kw={"rows": 3, "placeholder": "Enter your full address"})
    education = TextAreaField('Education', validators=[DataRequired()], render_kw={"rows": 4, "placeholder": "Enter your educational background, degrees, certifications, etc."})
    skills = TextAreaField('Technical Skills', validators=[DataRequired()], render_kw={"rows": 4, "placeholder": "List your technical skills, programming languages, tools, etc."})
    interpersonal_skills = TextAreaField('Interpersonal Skills', validators=[DataRequired()], render_kw={"rows": 3, "placeholder": "List your soft skills, communication, leadership, teamwork, etc."})
    experience = TextAreaField('Experience', validators=[DataRequired()], render_kw={"rows": 6, "placeholder": "Describe your work experience, projects, achievements, etc."})
    certificates = TextAreaField('Certificates (Optional)', validators=[], render_kw={"rows": 3, "placeholder": "List any relevant certifications, courses, or training programs"})
    github = StringField('GitHub (Optional)', validators=[], render_kw={"placeholder": "https://github.com/yourusername"})
    linkedin = StringField('LinkedIn (Optional)', validators=[], render_kw={"placeholder": "https://linkedin.com/in/yourprofile"})
    profile_image = FileField('Profile Image (Optional)', validators=[])

    layout = SelectField('Resume Layout', choices=[
        ('classic', 'Classic Professional'),
        ('modern', 'Modern Clean'),
        ('creative', 'Creative Design'),
        ('minimalist', 'Minimalist'),
        ('executive', 'Executive Style'),
        ('developer', 'Developer Focused'),
        ('designer', 'Designer Portfolio'),
        ('academic', 'Academic Style')
    ])

    submit = SubmitField('Save Resume')