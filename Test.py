import requests
def test_scrape_facebook_page():
    url = "https://www.facebook.com/Publicpage" #example https://www.facebook.com/SamsungTunisie
    response = requests.get(f"http://localhost:8000/?url={url}")
    assert response.status_code == 200
    assert "data" in response.json()

