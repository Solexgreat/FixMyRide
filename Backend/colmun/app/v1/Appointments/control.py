

def get_all_appointment(self) -> dict:
        """Return dict of services
        """
        appointment = self._session.query(Appointment).all()
        return [a.__dict__ for a in appointment]