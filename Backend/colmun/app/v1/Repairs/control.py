


def get_all_repairs(self) -> dict:
        """Return dict of services
        """
        repairs = self._session.query(Repair).all()
        return [r.__dict__ for r in repairs]