# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.raspi import Raspi  # noqa: E501
from swagger_server.test import BaseTestCase


class TestSetupController(BaseTestCase):
    """SetupController integration test stubs"""

    def test_install_raspi(self):
        """Test case for install_raspi

        Add a new raspi to the user and trasfer basic files as zip.
        """
        body = Raspi()
        response = self.client.open(
            '/setminami/Simnature/1.0.0/install',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_pet(self):
        """Test case for update_pet

        Update an existing raspi
        """
        body = Raspi()
        response = self.client.open(
            '/setminami/Simnature/1.0.0/install',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
