from flask_app import app
from flask import redirect, render_template,request
from flask_app.models.author_model import Author
from flask_app.models.book_model import Book


@app.route('/')
def index():
    return redirect('/authors')
#renders default authors page
@app.route('/authors')
def authors():
    return render_template('authors.html',all_authors=Author.get_all())

#creates a new author
@app.route('/create/author',methods=['POST'])
def create_author():
    data = {
        "name": request.form['name']
    }
    author_id = Author.save(data)
    return redirect('/authors')

@app.route('/author/<int:id>')
def show_author(id):
    data = {
        "id": id
    }
    return render_template('show_author.html',author=Author.get_by_id(data),unfavorited_books=Book.unfavorited_books(data))

@app.route('/join/book',methods=['POST'])
def join_book():
    data = {
        'author_id': request.form['author_id'],
        'book_id': request.form['book_id']
    }
    Author.add_favorite(data)
    return redirect(f"/author/{request.form['author_id']}")

@app.errorhandler(404)
def page_not_found(e): #as far as I can tell this parameter literally exists just to stop a positional argument error.
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404