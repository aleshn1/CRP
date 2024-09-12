import pytest
from django.test import RequestFactory
from apps.authentication.models import CustomUser
from apps.members.models import Membros
from apps.members.views import members


@pytest.mark.django_db
class TestMembers:

    def test_happy_path_list_members(self):
        # Arrange
        user = CustomUser.objects.create_user(username='testuser', password='testpassword')
        request = RequestFactory().get('/')
        request.user = user

        # Act
        response = members(request)

        # Assert
        assert response.status_code == 200
        assert len(response.context['members_list']) == Membros.objects.count()

    def test_edge_case_empty_search_parameter(self):
        # Arrange
        user = CustomUser.objects.create_user(username='testuser', password='testpassword')
        request = RequestFactory().get('/', {'search': ''})
        request.user = user

        # Act
        response = members(request)

        # Assert
        assert response.status_code == 200
        assert len(response.context['members_list']) == Membros.objects.count()
