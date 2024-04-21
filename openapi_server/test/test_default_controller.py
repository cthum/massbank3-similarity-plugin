import unittest

from flask import json

from openapi_server.models.similarity_post_request import SimilarityPostRequest  # noqa: E501
from openapi_server.models.similarity_score_list_inner import SimilarityScoreListInner  # noqa: E501
from openapi_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_similarity_post(self):
        """Test case for similarity_post

        Create a new similarity calculation.
        """
        similarity_post_request = openapi_server.SimilarityPostRequest()
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/similarity',
            method='POST',
            headers=headers,
            data=json.dumps(similarity_post_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_version_get(self):
        """Test case for version_get

        Get the version string of the implementation.
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/version',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
