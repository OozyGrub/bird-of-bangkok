from datetime import datetime
from pydantic import BaseModel

from utils.time import as_bkk_tz, is_between_yesterday


class Record(BaseModel):
    speciesCode: str
    comName: str
    sciName: str
    locId: str
    locName: str
    obsDt: str
    howMany: int
    lat: float
    lng: float
    obsValid: bool
    obsReviewed: bool
    locationPrivate: bool
    subId: str
    subnational1Code: str
    subnational1Name: str
    countryCode: str
    countryName: str
    userDisplayName: str
    obsId: str
    checklistId: str
    presenceNoted: bool
    hasComments: bool
    firstName: str
    lastName: str
    hasRichMedia: bool


def parse_obs_dt(record: Record):
    try:
        return as_bkk_tz(datetime.strptime(record.obsDt, "%Y-%m-%d %H:%M"))
    except:
        return as_bkk_tz(datetime.strptime(record.obsDt, "%Y-%m-%d"))


def is_report_yesterday(record):
    return is_between_yesterday(parse_obs_dt(record))
