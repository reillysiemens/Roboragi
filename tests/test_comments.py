from typing import List

import pytest

from roboragi.comment import parse, Request, Tag


@pytest.mark.parametrize('comment,requests', [
    pytest.param(
        '{anime}',
        [Request(tag=Tag.ANIME, body='anime')]
    ),
    pytest.param(
        '{{anime}}',
        [Request(tag=Tag.ANIME, body='anime', expanded=True)]
    ),
    pytest.param(
        '<manga>',
        [Request(tag=Tag.MANGA, body='manga')]
    ),
    pytest.param(
        '<<manga>>',
        [Request(tag=Tag.MANGA, body='manga', expanded=True)]
    ),
    pytest.param(
        ']light novel[',
        [Request(tag=Tag.LIGHT_NOVEL, body='light novel')]
    ),
    pytest.param(
        ']]light novel[[',
        [Request(tag=Tag.LIGHT_NOVEL, body='light novel', expanded=True)]
    ),
    pytest.param(
        '|visual novel|',
        [Request(tag=Tag.VISUAL_NOVEL, body='visual novel')]
    ),
    pytest.param(
        '||visual novel||',
        [Request(tag=Tag.VISUAL_NOVEL, body='visual novel', expanded=True)]
    ),
])
def test_comment_parsing(comment: str, requests: List[Request]) -> None:
    assert list(parse(comment)) == requests
