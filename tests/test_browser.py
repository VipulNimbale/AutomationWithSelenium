def test_open_google(driver):
    driver.get("https://google.com")
    assert "Google" in driver.title