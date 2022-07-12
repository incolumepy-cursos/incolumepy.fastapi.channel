import imp
import json
from dataclasses import dataclass, field

from fastapi import FastAPI, HTTPException, Response, status
import logging
from inspect import stack


logging.basicConfig(level=logging.DEBUG)


app = FastAPI()


@dataclass
class Channel:
    id: str
    name: str
    tags: list[str] = field(default_factory=list)
    description: str = ''


channels: dict[str, Channel] = {}

with open('channels.json', encoding='utf8') as file:
    channels_raw = json.load(file)
    for channel_raw in channels_raw:
        channel = Channel(**channel_raw)
        channels[channel.id] = channel


@app.get('/')
def root() -> Response:
    return Response('The server is running.')


@app.get('/channels/{channel_id}', response_model=Channel)
def channel_read(channel_id: str) -> Channel:
    if channel_id not in channels:
        logging.error(f'{channel_id=}{status.HTTP_404_NOT_FOUND=}')
        raise HTTPException(status_code=404, detail='Channel not found')
    return channels[channel_id]


@app.get('/channels')
def channel_all():
    return channels
