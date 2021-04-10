import json

from rest_framework.test import APITestCase
from rest_framework import status
from api.models import PullRequest
from api.serializer import BranchSerializer,CommitSerializer,CommitDetailSerializer,PRListSerializer,PullRequestSerializer


class GetBranchesTestCase(APITestCase):
    def test_get_branches(self):
        response = self.client.get('/api/branches/')
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_get_branches_bad_url(self):
        response = self.client.get('/api/branche/')
        self.assertEqual(response.status_code,status.HTTP_404_NOT_FOUND)

    def test_get_pr_backups(self):
        response = self.client.get('/api/backup/')
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_get_prs(self):
        response = self.client.get('/api/prs/')
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_create_pr(self):
        data = {
            "base":"some_master",
            "title":"test",
            "body":"somebody",
            "commit":"somecommit",
            "merge":False,
            "compare":"some_master"
        }
        response = self.client.post('/api/prs/',data)
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_create_pr_bad_user(self):
        data = {
            "base":"some_masterer",
            "title":"test",
            "body":"somebody",
            "commit":"somecommit",
            "merge":False,
            "compare":"some_masterer"
        }
        response = self.client.post('/api/prs/',data)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
    
    def test_create_pr_missing_data(self):
        data = {
            
            "merge":False,
            "compare":"some_masterer"
        }
        response = self.client.post('/api/prs/',data)
        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)

    def test_merge_pr(self):
        data = {
            "number":1,
            "commit":"algun commit"
        }
        response = self.client.post('/api/prs/1/merge_pr/',data)
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_merge_pr_missing_data(self):
        data = {
            
        }
        response = self.client.post('/api/prs/1/merge_pr/',data)
        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)

    def test_close_pr(self):
        data = {
            "number":1,
        }
        response = self.client.post('/api/prs/1/close_pr/',data)
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_close_pr_missing_data(self):
        data = {
            
        }
        response = self.client.post('/api/prs/1/close_pr/',data)
        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)