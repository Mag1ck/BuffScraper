from selenium.webdriver.common.by import By


def filtrowanie(name):
    """
    function filter web to get only these items we need.
    :param name:
    :return: for every "if" returns list of elements which include defined text for first item it's ak-47 2nd awp etc.
    """
    if name.find_elements(By.PARTIAL_LINK_TEXT, "AK-47"):
        return name.find_elements(By.PARTIAL_LINK_TEXT, "AK-47")
    if name.find_elements(By.PARTIAL_LINK_TEXT, "AWP"):
        return name.find_elements(By.PARTIAL_LINK_TEXT, "AWP")
    if name.find_elements(By.PARTIAL_LINK_TEXT, "M4A4"):
        return name.find_elements(By.PARTIAL_LINK_TEXT, "M4A4")
    if name.find_elements(By.PARTIAL_LINK_TEXT, "M4A1-S"):
        return name.find_elements(By.PARTIAL_LINK_TEXT, "M4A1-S")
    if name.find_elements(By.PARTIAL_LINK_TEXT, "FAMAS"):
        return name.find_elements(By.PARTIAL_LINK_TEXT, "FAMAS")
    if name.find_elements(By.PARTIAL_LINK_TEXT, "Galil AR"):
        return name.find_elements(By.PARTIAL_LINK_TEXT, "Galil AR")
    if name.find_elements(By.PARTIAL_LINK_TEXT, "USPS"):
        return name.find_elements(By.PARTIAL_LINK_TEXT, "USP-S")
    if name.find_elements(By.PARTIAL_LINK_TEXT, "Desert Eagle"):
        return name.find_elements(By.PARTIAL_LINK_TEXT, "Desert Eagle")
