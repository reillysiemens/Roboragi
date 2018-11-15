from typing import List

import pytest

from roboragi.comments import parse, Request, Tag


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


@pytest.mark.parametrize('comment,requests', [
    pytest.param(
        '{anime0} {anime1}',
        [
            Request(tag=Tag.ANIME, body='anime0'),
            Request(tag=Tag.ANIME, body='anime1')
        ]
    ),
    pytest.param(
        '{{anime0}} {{anime1}}',
        [
            Request(tag=Tag.ANIME, body='anime0', expanded=True),
            Request(tag=Tag.ANIME, body='anime1', expanded=True)
        ]
    ),
    pytest.param(
        '<manga0> <manga1>',
        [
            Request(tag=Tag.MANGA, body='manga0'),
            Request(tag=Tag.MANGA, body='manga1')
        ]
    ),
    pytest.param(
        '<<manga0>> <<manga1>>',
        [
            Request(tag=Tag.MANGA, body='manga0'),
            Request(tag=Tag.MANGA, body='manga1')
        ]
    ),
    pytest.param(
        ']light novel0[ ]light novel1[',
        [
            Request(tag=Tag.MANGA, body='light novel0'),
            Request(tag=Tag.MANGA, body='light novel1')
        ]
    ),
    pytest.param(
        ']]light novel0[[ ]]light novel1[[',
        [
            Request(tag=Tag.MANGA, body='light novel0', expanded=True),
            Request(tag=Tag.MANGA, body='light novel1', expanded=True)
        ]
    ),
    pytest.param(
        '|visual novel0| |visual novel1|',
        [
            Request(tag=Tag.MANGA, body='visual novel0'),
            Request(tag=Tag.MANGA, body='visual novel1')
        ]
    ),
    pytest.param(
        '||visual novel0|| ||visual novel1||',
        [
            Request(tag=Tag.MANGA, body='visual novel0', expanded=True),
            Request(tag=Tag.MANGA, body='visual novel1', expanded=True)
        ]
    ),
])
def test_multiple_comment_parsing(
    comment: str,
    requests: List[Request]
) -> None:
    assert list(parse(comment)) == requests
