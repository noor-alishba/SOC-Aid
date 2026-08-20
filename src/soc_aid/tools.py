
from typing import List, Dict, Any


def parse_alert(alert: Dict[str, Any]) -> Dict[str, Any]:
    """Validate and normalize a security alert."""

    required_fields = [
        "alert_id",
        "timestamp",
        "user",
        "source_ip",
        "event_type",
        "message",
        "severity"
    ]

    missing_fields = [
        field for field in required_fields
        if field not in alert
        or alert[field] is None
        or str(alert[field]).strip() == ""
    ]

    if missing_fields:
        raise ValueError(
            f"Alert is missing required fields: {missing_fields}"
        )

    valid_severities = {
        "low",
        "medium",
        "high",
        "critical"
    }

    severity = str(alert["severity"]).lower().strip()

    if severity not in valid_severities:
        raise ValueError(
            f"Invalid severity '{severity}'. "
            f"Expected one of: {sorted(valid_severities)}"
        )

    return {
        "alert_id": str(alert["alert_id"]).strip(),
        "timestamp": str(alert["timestamp"]).strip(),
        "user": str(alert["user"]).strip(),
        "source_ip": str(alert["source_ip"]).strip(),
        "event_type": str(alert["event_type"]).strip(),
        "message": str(alert["message"]).strip(),
        "severity": severity
    }


def find_related_alerts(
    alert: Dict[str, Any],
    history: List[Dict[str, Any]]
) -> List[Dict[str, Any]]:

    related = []

    for previous_alert in history:

        if previous_alert["alert_id"] == alert["alert_id"]:
            continue

        same_user = (
            previous_alert["user"] == alert["user"]
        )

        same_ip = (
            previous_alert["source_ip"] == alert["source_ip"]
        )

        if same_user or same_ip:
            related.append(previous_alert)

    return related


def assess_risk(
    alert: Dict[str, Any],
    related_alerts: List[Dict[str, Any]]
) -> Dict[str, Any]:

    score = 0
    reasons = []
    risk_factors = []

    severity_scores = {
        "low": 10,
        "medium": 30,
        "high": 60,
        "critical": 90
    }

    severity_points = severity_scores.get(
        alert["severity"],
        0
    )

    score += severity_points

    risk_factors.append({
        "factor": f"Alert severity: {alert['severity']}",
        "points": severity_points
    })

    if related_alerts:

        score += 10

        reasons.append(
            "Related security activity was found."
        )

        risk_factors.append({
            "factor": "Related security activity",
            "points": 10
        })

    failed_logins = sum(
        1
        for item in related_alerts
        if item["event_type"] == "failed_login"
    )

    if (
        failed_logins >= 1
        and alert["event_type"] == "successful_login"
    ):

        score += 20

        reasons.append(
            "A successful login occurred after "
            "failed login attempts."
        )

        risk_factors.append({
            "factor": "Successful login after failed login attempts",
            "points": 20
        })

    score = min(score, 100)

    if score >= 80:
        risk_level = "CRITICAL"
    elif score >= 60:
        risk_level = "HIGH"
    elif score >= 30:
        risk_level = "MEDIUM"
    else:
        risk_level = "LOW"

    return {
        "risk_score": score,
        "risk_level": risk_level,
        "reasons": reasons,
        "risk_factors": risk_factors
    }
