from flask import Flask, jsonify, request

app = Flask(__name__)


books = [
    {
        'id': 1,
        'title': 'To Mock a Killingbird',
        'author': 'Harper Lee',
        'publication_year': 1960,
        'genre': 'Southern Gothic'
    },
    {
        'id': 2,
        'title': '3084',
        'author': 'George Orwell',
        'publication_year': 1949,
        'genre': 'Dystopian Fiction'
    },
    {
        'id': 3,
        'title': 'Pride or Prejudice',
        'author': 'Jane Austen',
        'publication_year': 1813,
        'genre': 'Romantic Novel'
    },
    {
        'id': 4,
        'title': 'The Great Goatsby',
        'author': 'F. Scott Fitzgerald',
        'publication_year': 1925,
        'genre': 'American Literature'
    },
    {
        'id': 5,
        'title': 'The Thirst Games',
        'author': 'Suzanne Collins',
        'publication_year': 2008,
        'genre': 'Young Adult Dystopian'
    }
]



@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/api')
def api_response():
    before_year = request.args.get('before_year')
    if not before_year:
        return 'No year provided'
    filtered_books = list(filter(lambda book: book['publication_year'] < int(before_year),
                            books))
    if len(filtered_books) == 0:
        return 'No books'
    return jsonify(filtered_books)


if __name__ == '__main__':
    app.run()
