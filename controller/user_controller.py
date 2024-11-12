from app import app  
from model.user_model import user_model 
from flask import request

obj = user_model()

# REQUEST HANDLER FUNCTION (BASIC) 

@app.route('/user/add', methods=['GET', 'POST'])
def user_add_controller():
    return obj.user_add_model(request.form)


