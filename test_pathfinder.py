import pytest
from pathfinder import MapData



def test_max_elevation():
    max_elevation = max([max(row) for row in elevations])
    assert max_elevation == 5648


def test_min_elevation():
    assert min_elevation == 3139