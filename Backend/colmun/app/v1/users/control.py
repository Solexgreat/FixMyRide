



 def get_users(self) -> dict:
        """Return dict of users
        """
        users = self._session.query(User).all()
        return [u.__dict__ for u in users]

