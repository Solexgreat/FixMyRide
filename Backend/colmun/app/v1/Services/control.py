


 def get_service(self) -> dict:
        """Return dict of services
        """
        services = self._session.query(Service).all()
        return [s.__dict__ for s in services]
