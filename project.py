import requests
from random import randint

"""a program that will return a random artwork image
    using Art Institute of Chicago API"""


def main():
    artworks = search_art()
    api_link, title, artist, date, info = pick_art(artworks)
    img_link = get_image_url(api_link)
    return img_link, title, artist, date, info


def search_art():
    """searches for a random art
        and returns its contents"""
    artworks = requests.get("https://api.artic.edu/api/v1/artworks/search?query[term][is_public_domain]=true&page=" + str(
        randint(1, 100))).json()    # random page 1-100
    return artworks


def pick_art(artworks):
    api_link = (artworks['data'][randint(0, artworks['pagination']['limit']-1)]
                ['api_link'] + '?fields=id,title,image_id,artist_display,date_display,api_link')
    api_link = requests.get(api_link).json()
    title, artist, date, info = api_link['data']['title'], api_link['data']['artist_display'], api_link[
        'data']['date_display'], api_link['data']['api_link'].replace('api.', '').replace('/api/v1', '')
    return api_link, title, artist, date, info


def get_image_url(api_link):
    """construct IIIF image url
        by taking image id from link"""
    image_url = api_link['config']['iiif_url'] + '/' + \
        api_link['data']['image_id'] + '/full/843,/0/default.jpg'
    return image_url


if __name__ == "__main__":
    main()
