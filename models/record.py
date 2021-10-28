from typing import Optional
from pydantic import BaseModel


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
