from streamlit.testing.v1 import AppTest

def test_love_ui():
    app = AppTest.from_file("app.py")
    app.run()

    assert not app.exception