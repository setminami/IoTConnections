import connexion
import six

from swagger_server.models.schedule import Schedule  # noqa: E501
from swagger_server import util


def get_schedule(utc_date, username):  # noqa: E501
    """Get the Schedules that all your raspi held

     # noqa: E501

    :param utc_date: ISO8601 by UTC
    :type utc_date: str
    :param username: The user name for login
    :type username: str

    :rtype: List[Schedule]
    """
    return 'do some magic!'
