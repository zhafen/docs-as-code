from dataclasses import dataclass


@dataclass
class Analyst:
    id: str


@dataclass
class Requester:
    net_id: str


@dataclass
class RequestConcept:
    description: str


@dataclass
class Request:
    id: str
    requester_id: str
    time_spent: float = 0.0


@dataclass
class Report:
    id: str