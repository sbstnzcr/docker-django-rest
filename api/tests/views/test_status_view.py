from rest_framework.reverse import reverse


class TestStatusView:
    def test_status_view(self, api_client):
        url = reverse("api:status")
        response = api_client.get(url)
        assert response.status_code == 200
