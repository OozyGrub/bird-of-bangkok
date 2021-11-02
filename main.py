import os
from typing import Coroutine, List

from dotenv import load_dotenv
from ebird.api import get_nearby_notable
from fastapi import FastAPI, Header, HTTPException, Request
from linebot.api import LineBotApi
from linebot.exceptions import InvalidSignatureError
from linebot.models import (FlexSendMessage, MessageEvent, TextMessage,
                            TextSendMessage)
from linebot.webhook import WebhookHandler
from linebotx import LineBotApiAsync, WebhookHandlerAsync

from models.record import Record, is_report_previous_hour, is_report_yesterday
from views.record import buildRecordFlex

load_dotenv()

line_bot_api = LineBotApi(os.environ.get('CHANNEL_ACCESS_TOKEN'))
handler = WebhookHandler(os.environ.get('CHANNEL_SECRET'))

app = FastAPI()

VERSION = '1.0.0'


@app.get("/")
def version() -> str:
    return VERSION


@app.post('/webhook')
async def webhook(request: Request, x_line_signature: str = Header(None)):
    body = await request.body()
    try:
        handler.handle(body.decode("utf-8"), x_line_signature)
    except InvalidSignatureError:
        raise HTTPException(
            status_code=400, detail="chatbot handle body error.")
    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event: MessageEvent):
    return line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text='Bird of Bangkok {}'.format(VERSION))
    )


def _uniq_records(records: List[Record]) -> List[Record]:
    return list({record['obsId']: record for record in records}.values())


def _plain_to_class(record: Record) -> Record:
    return Record.parse_obj(record)


def _get_records() -> List[Record]:
    api_key = os.environ.get("API_KEY")
    lat = os.environ.get("LAT")
    lng = os.environ.get("LNG")
    records: List[Record] = get_nearby_notable(
        api_key, lat, lng, dist=50, detail='full')
    records = _uniq_records(records)
    return list(map(_plain_to_class, records))


def _get_yesterday_records() -> List[Record]:
    records = _get_records()
    return list(filter(is_report_yesterday, records))


def _get_previous_hrs_records() -> List[Record]:
    records = _get_records()
    return list(filter(is_report_previous_hour, records))


@app.post('/broadcast')
def broadcast():
    records = _get_previous_hrs_records()
    for record in records:
        line_bot_api.broadcast(buildRecordFlex(record))
    return 'success'
