import pytest
from project import pick_art,get_image_url,search_art


def test_search_art():
    assert search_art() != search_art() # finds random page
    with pytest.raises(TypeError):
        search_art('foo')


def test_pick_art():
    JAYSON = search_art()
    assert pick_art(JAYSON) != pick_art(JAYSON) # finds random artwork
    with pytest.raises(KeyError):
        JAYSON['foo']


def test_get_image_url():
    JAYSON = search_art()
    JAYSON, title, artist, date, info = pick_art(JAYSON)
    print(JAYSON)
    assert get_image_url(JAYSON) == JAYSON['config']['iiif_url'] + '/' + JAYSON['data']['image_id'] + '/full/843,/0/default.jpg'

