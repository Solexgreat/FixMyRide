


@app.route('/service', methods=['GET'], strict_slashes=False)
def get_service() -> str:
    """Return all service
    """

    return jsonify(DB.get_service()), 200
