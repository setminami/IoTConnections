# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.schedule import Schedule  # noqa: E501
from swagger_server.test import BaseTestCase


class TestOperateController(BaseTestCase):
    """OperateController integration test stubs"""

    def test_get_schedule(self):
        """Test case for get_schedule

        Get the Schedules that all your raspi held
        """
        query_string = [('utc_date', 'utc_date_example'),
                        ('username', 'username_example')]
        response = self.client.open(
            '/setminami/Simnature/1.0.0/operate/schedules',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
