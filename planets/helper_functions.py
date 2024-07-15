import requests


def build_jump_map_link(planet_sector, planet_coords, jump=3, **kwargs):
    """Build Jump map render link from Traveller Map API.

    Args:
        planet_sector (str): name of the sector, e.g. "Trojan Reach".
        planet_coords (str): hex coordinates of planet in the sector, e.g. "2223".
        jump (int): jump distance in parsecs (hexes) around the planet to render.
        **kwargs: other API options. https://travellermap.com/doc/api#jump-map-render-hexes-within-n-parsecs.
    """
    url = "https://travellermap.com/api/jumpmap"
    payload = {
        "sector": planet_sector,
        "hex": planet_coords,
        "jump": jump,
        **kwargs
    }

    # r = requests.get(url, params=payload)
    # r.raise_for_status()

    # return r.url

    req = requests.Request("GET", url).prepare()
    req.prepare_url(url, params=payload)
    return req.url


# Unused function for downloading rendered jump maps.
def download_map(response_content, filename):
    with open(filename, "wb") as file:
        file.write(response_content)
