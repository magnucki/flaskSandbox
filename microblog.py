"""Main microblog module"""
from app import app, db 
from app.models import User, Post

@app.shell_context_processor
def make_shell_context():
    """defines shell context for flask - no need for manual imports"""
    return {'db': db, 'User': User, 'Post': Post}
