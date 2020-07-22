from flask import Flask,render_template,redirect,url_for
from . import main
from flask_login import login_required,current_user
from .forms import PitchForm,CommentForm
from .. import db
from ..models import Pitches,User,Comments

@main.route('/')
def index():
    '''
    my index page
    '''
    title = 'Pitch It UP'
    return render_template('index.html',title = title)

@main.route('/pitch/', methods = ['GET','POST'])
@login_required
def new_pitch():

    form = PitchForm()

    if form.validate_on_submit():
        category = form.category.data
        pitch= form.pitch.data
        

        # Updated pitchinstance
        new_pitch = Pitches(category= category,pitch= pitch,user=current_user)

        db.session.add(new_pitch)
        db.session.commit()

        title='New Pitch'


        return redirect(url_for('main.index'))

    return render_template('pitch.html',pitch_entry= form)

@main.route('/categories/<cate>',methods = ['GET','POST'])
def category(cate):
    '''
    function to return the pitches by category
    '''


    form = CommentForm()
    
    
    pitches = Pitches.query.filter_by(category=cate).all()
    print(category)
    title = f'{cate}'
    return render_template('categories.html',title = title, pitches = pitches,comment_form = form)


@main.route('/all_comment/<int:pitches_id>', methods = ['GET', 'POST'])
@login_required
def all_comment(pitches_id):
    pitch = Pitches.query.filter_by(id=pitches_id).first()
    comments = Comments.query.filter_by(pitches_id=pitches_id).all()

    form = CommentForm()
    if form.validate_on_submit():
        comment = form.comment.data

        new_comment = Comments(comment=comment,user=current_user,pitch=pitch)


        db.session.add(new_comment)
        db.session.commit()

       

        return redirect(url_for('categories.html',cate =pitch.category))


    
    return render_template('new_comment.html',comments= comments)
  