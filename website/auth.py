from flask import Blueprint, render_template, request
from website.algo import Horowitz_Sahni


auth = Blueprint('auth', __name__)




@auth.route('/', methods = ['GET', 'POST'])
def login():
    return render_template('welcome.html')


@auth.route('/input-numbers', methods = ['GET', 'POST'])
def input_numbers():
    print(request.form)
    size = int(request.form.get('sizeOfArray'))
    target = int(request.form.get('target'))
    
    return render_template('input_numbers.html', number = size, target = target)




@auth.route('/res', methods = ['GET', 'POST'])
def res():
    numbers = request.form
    target = int(request.form.get('catch'))
    arr = []
    for value in numbers.values():
        arr.append(int(value))
    arr = arr[:len(arr)-1]
    return render_template('res.html', ans = Horowitz_Sahni(arr, target))