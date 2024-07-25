from urllib import parse


def build_jump_map_link(planet_sector, planet_coords, jump=3, **kwargs):
    """Build Jump map render link from Traveller Map API.

    Args:
        planet_sector (str): name of the sector, e.g. "Trojan Reach".
        planet_coords (str): hex coordinates of planet in the sector, e.g. "2223".
        jump (int): jump distance in parsecs (hexes) around the planet to render.
        **kwargs: other API options. https://travellermap.com/doc/api#jump-map-render-hexes-within-n-parsecs.
    """
    query = {
        "sector": planet_sector,
        "hex": planet_coords,
        "jump": jump,
        **kwargs
    }

    url = parse.urlunparse(
        [
            "https",
            "travellermap.com",
            "/api/jumpmap",
            "",
            parse.urlencode(query),
            ""
        ]
    )
    return url


def build_map_link(planet_sector, planet_coords):
    url = parse.urlunparse([
        "https",
        "travellermap.com",
        f"/go/{planet_sector}/{planet_coords}",
        "",
        "",
        "",
    ])
    return url


# Unused function for downloading rendered jump maps.
def download_map(response_content, filename):
    with open(filename, "wb") as file:
        file.write(response_content)
