#!/usr/bin/env python3
"""
test_client
"""
import unittest
from parameterized import parameterized
from unittest.mock import PropertyMock, patch
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """TestGithubOrgClient Class"""

    @parameterized.expand(
        [
            ("google", {"login": "google", "id": 1342004}),
            ("abc", {"message": "Not Found", "status": 404}),
        ]
    )
    @patch("client.get_json")
    def test_org(self, org, expected_result, mock_get_json):
        obj = GithubOrgClient(org)
        mock_get_json.return_value = expected_result

        self.assertEqual(obj.org, expected_result)
        mock_get_json.assert_called_once_with
        (obj.ORG_URL.format(org=obj._org_name))

        cached_result = obj.org
        self.assertEqual(cached_result, expected_result)
        mock_get_json.assert_called_once_with
        (obj.ORG_URL.format(org=obj._org_name))

    def test_public_repos_url(self):
        with patch.object(
            GithubOrgClient,
            "org",
            return_value={
                "login": "google",
                "id": 1342004,
                "repos_url": "https://api.github.com/orgs/google/repos",
            },
            new_callable=PropertyMock,
        ) as mock_org:
            obj = GithubOrgClient("google")
            self.assertEqual(
                obj._public_repos_url,
                "https://api.github.com/orgs/google/repos"
            )
            mock_org.assert_called_once()

    @patch(
        "client.get_json",
        return_value=[{"name": "repo1"}, {"name": "repo2"}, {"name": "repo3"}],
    )
    def test_public_repos(self, mock_get_json):
        """
        Unit Test for GithubOrgClient.public_repos
        Args:
            mock_get_json (Mock Object): Mocking get_json in client.py
        """
        with patch.object(
            GithubOrgClient, "_public_repos_url", new_callable=PropertyMock
        ) as mock_repos_url:
            mock_repos_url.return_value = "https://fakeurl.org/repos"

            client = GithubOrgClient("faheorg")

            repos = client.public_repos()

            self.assertEqual(repos, ["repo1", "repo2", "repo3"])
            mock_get_json.assert_called_once_with("https://fakeurl.org/repos")
            mock_repos_url.assert_called_once()

    @parameterized.expand(
        [
            ({"licence": {"key": "my_license"}}, "my_license", True),
            ({"licence": {"key": "other_license"}}, "my_license", False),
        ]
    )
    def test_has_license(self, repo, license_key, expected):
        result = GithubOrgClient.has_license(repo, license_key)

        self.assertEqual(result, expected)


@parameterized_class(
    [
        {
            "org_payload": TEST_PAYLOAD[0][0],
            "repos_payload": TEST_PAYLOAD[0][1],
            "expected_repos": TEST_PAYLOAD[0][2],
            "apache2_repos": TEST_PAYLOAD[0][3],
        }
    ]
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests for GithubOrgClient"""

    @classmethod
    def setUpClass(cls):
        cls.get_patcher = patch("requests.get")

        cls.mock_get = cls.get_patcher.start()

        def side_effect(url):
            if "orgs" in url:
                return MockResponse(cls.org_payload)
            elif "repos" in url:
                return MockResponse(cls.repos_payload)
            return MockResponse(None)

        cls.mock_get.side_effect = side_effect

    @classmethod
    def tearDownClass(cls):
        cls.get_patcher.stop()

    def test_public_repos(self):
        client = GithubOrgClient("google")
        repos = client.public_repos()
        self.assertEqual(repos, self.expected_repos)

    def test_public_repos_with_license(self):
        client = GithubOrgClient("google")
        repos = client.public_repos(license="apache-2.0")
        self.assertEqual(repos, self.apache2_repos)


class MockResponse:
    """Mock response for requests.get().json()"""

    def __init__(self, json_data):
        self.json_data = json_data

    def json(self):
        return self.json_data
