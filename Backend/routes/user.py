


@login_manager.user_loader
def load_user(user_id):
    """
    """
    user = DB.find_user(user_id=user_id)
    if user is None:
        return None

@app.route('/register', methods=['POST'], strict_slashes=False)
def register_user() -> str:
    """Creat new user
    """

    name = request.form['first name']
    email = request.form['email']
    password = request.form['password']
    role = request.form['role']
    try:
        user = AUTH.register_user(email, password, name, role)
    except Exception as e:
        return flash(f'user already exist', category='danger')
    login_user(user)        
    if user:
        if user.role == 'Admin':
            return render_template('admin-dashboard.html')
        
        if user.role == 'Costumer':
            return render_template('index.html')
    else:
        flash(f'user already exist', category='danger')
        

@app.route('/user', methods=['GET'], strict_slashes = False)
def get_users() -> str:
    """Return all users
    """

    return jsonify(DB.get_users()), 200