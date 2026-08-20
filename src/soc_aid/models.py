
from typing import TypedDict, List, Dict, Any


class SOCAidState(TypedDict, total=False):
    alert: Dict[str, Any]
    parsed_alert: Dict[str, Any]
    related_alerts: List[Dict[str, Any]]
    risk_assessment: Dict[str, Any]
    analysis: str
    recommendation: str
    decision: str
    error: str
