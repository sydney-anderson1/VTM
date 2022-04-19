import app

def test_TotalCost(height, radius):
    """
    GIVEN a user enters the height and radius
    WHEN those amounts are passed through this function
    THEN the total cost is accurately calculated
    """
    assert app.TotalCost(360, 180) == 141,300.00
