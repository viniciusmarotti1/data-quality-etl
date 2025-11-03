from app.hello_world import hw

def test_hello_world():
    output = hw()
    exceptetd = "Hello, World!"
    assert output == exceptetd