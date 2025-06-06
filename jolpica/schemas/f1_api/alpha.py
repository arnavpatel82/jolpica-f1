import datetime

from pydantic import BaseModel, Field, HttpUrl


class DetailMetadata(BaseModel):
    timestamp: datetime.datetime


class DetailResponse[T](BaseModel):
    metadata: DetailMetadata
    data: T


class PaginationMetadata(DetailMetadata):
    count: int
    page_size: int
    current_page: int
    total_pages: int
    next_url: HttpUrl | None = None
    previous_url: HttpUrl | None = None


class PaginatedResponse[T](BaseModel):
    metadata: PaginationMetadata
    data: T


class ScheduleCircuit(BaseModel):
    name: str
    reference: str | None = None
    wikipedia: HttpUrl | None = None
    latitude: float | None = None
    longitude: float | None = None
    altitude: float | None = None
    locality: str | None = None
    country: str | None = None
    country_code: str | None = Field(None, max_length=3)


class ScheduleSession(BaseModel):
    type: str = Field(..., description="Session type code (e.g., R, Q1, FP1)")
    type_display: str = Field(..., description="Display name for the session type")
    date: datetime.date | None = None
    time: datetime.time | None = None


class ScheduleRound(BaseModel):
    number: int
    name: str | None = None
    circuit: ScheduleCircuit
    date: datetime.date | None = None
    sessions: list[ScheduleSession]


class ScheduleRoundInfoDetail(BaseModel):
    number: int
    index: int


class ScheduleRoundsInfo(BaseModel):
    next: ScheduleRoundInfoDetail | None = None
    previous: ScheduleRoundInfoDetail | None = None


class ScheduleSummary(BaseModel):
    url: HttpUrl
    year: int
    wikipedia: HttpUrl | None = None


class ScheduleDetail(BaseModel):
    url: HttpUrl
    year: int
    wikipedia: HttpUrl | None = None
    rounds_info: ScheduleRoundsInfo | None = None
    rounds: list[ScheduleRound]


class RetrievedScheduleDetail(DetailResponse[ScheduleDetail]):
    """Schema for season schedule detail responses"""


class ResultTime(BaseModel):
    milliseconds: str


class FastestLap(BaseModel):
    rank: int
    lap_number: int
    time: ResultTime | None = None


class ResultDriver(BaseModel):
    reference: str | None = None
    forename: str
    surname: str
    abbreviation: str | None = None
    nationality: str | None = None
    country_code: str | None = Field(None, max_length=3)
    wikipedia: HttpUrl | None = None


class ResultTeam(BaseModel):
    reference: str | None = None
    name: str
    nationality: str | None = None
    country_code: str | None = Field(None, max_length=3)
    wikipedia: HttpUrl | None = None


class SessionResult(BaseModel):
    position: int | None = None
    position_text: str | None = None
    car_number: str | None = None
    points: float | None = None
    grid_position: int | None = None
    completed_laps: int | None = None
    is_classified: bool | None = None
    classification: str | None = None
    time: ResultTime | None = None
    fastest_lap: FastestLap | None = None
    driver: ResultDriver
    team: ResultTeam


class SessionSummary(BaseModel):
    url: HttpUrl
    type: str = Field(..., description="Session type code (e.g., R, Q1, FP1)")
    type_display: str = Field(..., description="Display name for the session type")
    date: datetime.date | None = None
    time: datetime.time | None = None
    round_number: int
    round_name: str | None = None
    circuit_name: str
    season_year: int


class SessionDetail(SessionSummary):
    circuit: ScheduleCircuit
    results: list[SessionResult]


class RetrievedSessionDetail(DetailResponse[SessionDetail]):
    """Schema for session results detail responses"""
