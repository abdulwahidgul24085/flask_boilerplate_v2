from flask import url_for


class TestPage(object):
    def test_home_page(self, client):
        """ Home page should respond with a success 200. """
        response = client.get(url_for('page.home'))
        assert response.status_code == 200

    def test_terms_page(self, client):
        """ Terms page should respond with a success 200. """
        response = client.get(url_for('page.terms'))
        assert response.status_code == 200

    def test_privacy_page(self, client):
        """ Privacy page should respond with a success 200. """
        response = client.get(url_for('page.privacy'))
        assert response.status_code == 200

    def test_about_page(self, client):
        """ About page should respond with a success 200. """
        response = client.get(url_for('page.about'))
        assert response.status_code == 200

    def test_contact_page(self, client):
        """ Contact page should respond with a success 200. """
        response = client.get(url_for('page.contact'))
        assert response.status_code == 200
