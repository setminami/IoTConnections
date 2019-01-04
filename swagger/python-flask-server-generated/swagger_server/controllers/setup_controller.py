import connexion
import six

from swagger_server.models.raspi import Raspi  # noqa: E501
from swagger_server import util


def install_raspi(body):  # noqa: E501
    """Add a new raspi to the user and trasfer basic files as zip.

     # noqa: E501

    :param body: raspi object that needs to be added to the store
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Raspi.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_pet(body):  # noqa: E501
    """Update an existing raspi

     # noqa: E501

    :param body: Pet object that needs to be added to the store
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Raspi.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
