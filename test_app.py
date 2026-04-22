from Activity_6 import TemperatureConverterApp


def test_fahrenheit_to_celsius():
    app = TemperatureConverterApp(None)

    assert round(app.fahrenheit_to_celsius(32), 2) == 11.00
    assert round(app.fahrenheit_to_celsius(212), 2) == 100.00
    assert round(app.fahrenheit_to_celsius(68), 2) == 20.00