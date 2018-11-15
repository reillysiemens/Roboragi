from typing import List

import pytest

from roboragi.comments import parse, Request, Tag


@pytest.mark.parametrize('comment,requests', [
    pytest.param(
        '{anime}',
        [Request(tag=Tag.ANIME, body='anime')],
        id='anime'
    ),
    pytest.param(
        '{{anime}}',
        [Request(tag=Tag.ANIME, body='anime', expanded=True)],
        id='expanded anime'
    ),
    pytest.param(
        '<manga>',
        [Request(tag=Tag.MANGA, body='manga')],
        id='manga'
    ),
    pytest.param(
        '<<manga>>',
        [Request(tag=Tag.MANGA, body='manga', expanded=True)],
        id='expanded manga'
    ),
    pytest.param(
        ']light novel[',
        [Request(tag=Tag.LIGHT_NOVEL, body='light novel')],
        id='light novel'
    ),
    pytest.param(
        ']]light novel[[',
        [Request(tag=Tag.LIGHT_NOVEL, body='light novel', expanded=True)],
        id='expanded light novel'
    ),
    pytest.param(
        '|visual novel|',
        [Request(tag=Tag.VISUAL_NOVEL, body='visual novel')],
        id='visual novel'
    ),
    pytest.param(
        '||visual novel||',
        [Request(tag=Tag.VISUAL_NOVEL, body='visual novel', expanded=True)],
        id='expanded visual novel'
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
        ],
        id='anime'
    ),
    pytest.param(
        '{{anime0}} {{anime1}}',
        [
            Request(tag=Tag.ANIME, body='anime0', expanded=True),
            Request(tag=Tag.ANIME, body='anime1', expanded=True)
        ],
        id='expanded anime'
    ),
    pytest.param(
        '<manga0> <manga1>',
        [
            Request(tag=Tag.MANGA, body='manga0'),
            Request(tag=Tag.MANGA, body='manga1')
        ],
        id='manga'
    ),
    pytest.param(
        '<<manga0>> <<manga1>>',
        [
            Request(tag=Tag.MANGA, body='manga0'),
            Request(tag=Tag.MANGA, body='manga1')
        ],
        id='expanded manga'
    ),
    pytest.param(
        ']light novel0[ ]light novel1[',
        [
            Request(tag=Tag.MANGA, body='light novel0'),
            Request(tag=Tag.MANGA, body='light novel1')
        ],
        id='light novel'
    ),
    pytest.param(
        ']]light novel0[[ ]]light novel1[[',
        [
            Request(tag=Tag.MANGA, body='light novel0', expanded=True),
            Request(tag=Tag.MANGA, body='light novel1', expanded=True)
        ],
        id='expanded light novel'
    ),
    pytest.param(
        '|visual novel0| |visual novel1|',
        [
            Request(tag=Tag.MANGA, body='visual novel0'),
            Request(tag=Tag.MANGA, body='visual novel1')
        ],
        id='visual novel'
    ),
    pytest.param(
        '||visual novel0|| ||visual novel1||',
        [
            Request(tag=Tag.MANGA, body='visual novel0', expanded=True),
            Request(tag=Tag.MANGA, body='visual novel1', expanded=True)
        ],
        id='expanded visual novel'
    ),
])
def test_multiple_comment_parsing(
    comment: str,
    requests: List[Request]
) -> None:
    assert list(parse(comment)) == requests
