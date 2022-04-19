def test_index_route(app, client):
    """
    GIVEN a flask application configured for testing
    WHEN the '/' is requested (GET)
    THEN check that the response is valid
    """
    with app.test_client as test_client:
        res = test_client.get('/')
        assert res.status_code == 200

def test_about_route(app, client):
    """
    GIVEN a flask application configured for testing
    WHEN the '/about' route is requested (GET)
    THEN check that the response is valid
    """
    with app.test_client as test_client:
        res = test_client.get('/about')
        assert res.status_code == 200

def test_estimate_route(app, client):
    """
    GIVEN a flask application configured for testing
    WHEN the '/estimate' route is requested (GET)
    THEN check that the user is redirected to the homepage
    """
    with app.test_client() as test_client:
        res = test_client.get('/estimate')
        assert res.status_code == 302