import pytest
from django.urls import reverse
from .models import *

@pytest.mark.django_db
def test_home_view(client):
    url = reverse('home')  
    response = client.get(url)
    assert response.status_code == 203


@pytest.mark.django_db
def test_homepage_post_valid_form(client):
    url = reverse('home')
    form_data = {'name': 'Sargis', 'surname': 'Mnoyan'}  
    response = client.post(url, data=form_data)
    assert response.status_code == 302  
    assert response.url == '/'


