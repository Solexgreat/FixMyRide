from flask_mail import Message
from flask import Flask, jsonify, request, abort, redirect, render_template, flash
# from flask_login import login_user, logout_user, login_required, current_user, LoginManager
from Backend.column.app.v1.core.auth import AUTH
from Backend.column.app.v1.core.security import SECURITY
from .. import mail
from . import auth_bp




@auth_bp.route('/reset_password', methods=['POST'], strict_slashes=False)
def get_reset_password_token() -> str:
	"""POST /reset_password
		:Return
		-status 403 if email is invalid
	"""
	data=request.get_json()
	email = data['email']
	reset_token = SECURITY.get_reset_password_token(email)
	if reset_token:
		msg = Message('Password Reset Request', recipients=[email])
		msg.body = f"To reset your password, use the following token: {reset_token}"
		mail.send(msg)
		return jsonify({"message": "Reset token sent to your email"}), 200
	else:
		return jsonify({"message": "Invalid email or account not found"}), 403

@auth_bp.route('/login', methods=['POST'])
def login():
	"""
			login user via user details
	"""
	data = request.get_json()
	try:
		user = AUTH.verify_login(**data)
		return jsonify({'msg': "Login successful",'token': f'{user.session_id}' }), 201
	except Exception as e:
		return jsonify({'msg': e})

@auth_bp.route('/reset_password', methods=['PUT'], strict_slashes=False)
def update_password() -> str:
	"""PUT /reset_password
			:Return
			-status 403 if token is invalid
	"""
	data= request.get_json()
	email = data['email']
	new_password = data['new_password']
	reset_token = data['reset_token']

	token_email = SECURITY.validate_reset_token(email, reset_token)

	if token_email is None or token_email != email:
		return jsonify({"message": "Invalid or expired reset token"}), 403

	try:
		AUTH.update_password(reset_token, new_password)
	except Exception:
		abort(403)

	return jsonify({"email": email, "message": "Password updated"}), 200

@auth_bp.route('/api/check_login_status', methods=['GET'])
def check_login_status():
	# Check if session_id cookie is present
	session_id = request.cookies.get('session_id')
	if session_id:
			# Verify session_id with AUTH class
			if AUTH.get_current_user(session_id):
					return True
			else:
					return False
	else:
			return False
