import requests
from scrapping_service import scrape_facebook_page
def test_scrape_facebook_page():
    '''
    The test checks if the scrape_facebook_page() function is working as expected
    '''
    # Test inputs
    url = "https://www.facebook.com/Publicpage" #example: https://www.facebook.com/SamsungTunisie

    # Call the function to be tested
    result = scrape_facebook_page(url)

    # Check the result
    assert "data" in result, "Expected 'data' key not found in the result"
    assert type(result["data"]) == list, "Expected data to be a list, but got {}".format(type(result["data"]))


if __name__ == '__main__':
    test_scrape_facebook_page()