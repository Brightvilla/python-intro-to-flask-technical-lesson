"""Tests for Flask app routes."""

import pytest
from server.app import app


@pytest.fixture
def client():
    """Create a test client for the Flask app."""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


class TestIndexRoute:
    """Tests for the '/' route."""

    def test_index_route_exists(self, client):
        """GET / should return 200 status."""
        response = client.get("/")
        assert response.status_code == 200

    def test_index_route_content(self, client):
        """GET / should return the expected welcome message."""
        response = client.get("/")
        assert b"<h1>Welcome to my page!</h1>" in response.data


class TestUserRoute:
    """Tests for the '/<username>' route."""

    def test_user_route_exists(self, client):
        """GET /<username> should return 200 status."""
        response = client.get("/testuser")
        assert response.status_code == 200

    def test_user_route_content(self, client):
        """GET /<username> should return a profile page with the username."""
        response = client.get("/testuser")
        assert b"<h1>Profile for testuser</h1>" in response.data

    def test_user_route_different_username(self, client):
        """GET /<username> should work with any username."""
        response = client.get("/Brightvilla")
        assert b"<h1>Profile for Brightvilla</h1>" in response.data

    def test_user_route_returns_content_type_html(self, client):
        """GET /<username> should return HTML content."""
        response = client.get("/testuser")
        assert response.content_type == "text/html; charset=utf-8"
