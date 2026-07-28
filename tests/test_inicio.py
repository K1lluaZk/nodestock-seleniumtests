def test_abrir_nodestock(driver):

    driver.get("http://localhost:3000")

    assert "Node" in driver.title