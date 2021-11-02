from linebot.models.flex_message import FlexSendMessage
from models.record import Record


def buildRecordFlex(record: Record) -> FlexSendMessage:
    flex = FlexSendMessage(
        alt_text=record.comName,
        contents={
            "type": "bubble",
            "body": {
                "type": "box",
                "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "weight": "bold",
                            "size": "xl",
                            "text": record.comName
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "margin": "lg",
                            "spacing": "sm",
                            "contents": [
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "spacing": "sm",
                                    "contents": [
                                      {
                                          "type": "text",
                                          "text": "Place",
                                          "color": "#aaaaaa",
                                          "size": "sm",
                                          "flex": 1
                                      },
                                        {
                                          "type": "text",
                                          "text": record.locName,
                                          "wrap": True,
                                          "color": "#666666",
                                          "size": "sm",
                                          "flex": 5
                                      }
                                    ]
                                },
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "spacing": "sm",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "City",
                                            "color": "#aaaaaa",
                                            "size": "sm",
                                            "flex": 1
                                        },
                                        {
                                            "type": "text",
                                            "text": record.subnational1Name,
                                            "wrap": True,
                                            "color": "#666666",
                                            "size": "sm",
                                            "flex": 5
                                        }
                                    ]
                                },
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "spacing": "sm",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "Date",
                                            "color": "#aaaaaa",
                                            "size": "sm",
                                            "flex": 1
                                        },
                                        {
                                            "type": "text",
                                            "text": record.obsDt,
                                            "wrap": True,
                                            "color": "#666666",
                                            "size": "sm",
                                            "flex": 5
                                        }
                                    ]
                                },
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "spacing": "sm",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "User",
                                            "color": "#aaaaaa",
                                            "size": "sm",
                                            "flex": 1
                                        },
                                        {
                                            "type": "text",
                                            "text": record.userDisplayName,
                                            "wrap": True,
                                            "color": "#666666",
                                            "size": "sm",
                                            "flex": 5
                                        }
                                    ]
                                }
                            ]
                        },
                        {
                            "type": "button",
                            "style": "link",
                            "height": "sm",
                            "action": {
                                "type": "uri",
                                "label": "VIEW",
                                "uri": "https://ebird.org/checklist/{}".format(record.subId)
                            }
                        },
                    ]
            },
        }
    )
    return flex
