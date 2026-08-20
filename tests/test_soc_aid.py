
import sys
from pathlib import Path

# ------------------------------------------------------------
# Add src directory to Python path
# ------------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_PATH = PROJECT_ROOT / "src"

if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))


# ------------------------------------------------------------
# Imports
# ------------------------------------------------------------

from soc_aid.tools import (
    parse_alert,
    find_related_alerts,
    assess_risk
)


# ------------------------------------------------------------
# Test Data
# ------------------------------------------------------------

ALERTS = [
    {
        "alert_id": "A001",
        "timestamp": "2026-08-18 01:42:10",
        "user": "admin",
        "source_ip": "185.220.101.45",
        "event_type": "failed_login",
        "message": "Multiple failed login attempts detected",
        "severity": "medium"
    },
    {
        "alert_id": "A002",
        "timestamp": "2026-08-18 01:45:32",
        "user": "admin",
        "source_ip": "185.220.101.45",
        "event_type": "successful_login",
        "message": "Successful login after multiple failed attempts",
        "severity": "high"
    },
    {
        "alert_id": "A003",
        "timestamp": "2026-08-18 02:10:05",
        "user": "employee01",
        "source_ip": "192.168.1.25",
        "event_type": "normal_login",
        "message": "Normal employee login",
        "severity": "low"
    },
    {
        "alert_id": "A004",
        "timestamp": "2026-08-18 02:15:44",
        "user": "employee02",
        "source_ip": "10.0.0.15",
        "event_type": "malware_detected",
        "message": "Malicious file detected on endpoint",
        "severity": "critical"
    }
]


# ------------------------------------------------------------
# Test 1 — Alert Parsing
# ------------------------------------------------------------

def test_alert_parsing():

    parsed = parse_alert(ALERTS[1])

    assert parsed["alert_id"] == "A002"
    assert parsed["user"] == "admin"
    assert parsed["severity"] == "high"


# ------------------------------------------------------------
# Test 2 — Invalid Alert
# ------------------------------------------------------------

def test_invalid_alert():

    invalid_alert = {
        "alert_id": "INVALID",
        "event_type": "unknown_event"
    }

    try:
        parse_alert(invalid_alert)
        assert False, "Invalid alert should raise ValueError"

    except ValueError as error:

        assert "missing required fields" in str(error).lower()


# ------------------------------------------------------------
# Test 3 — Alert Correlation
# ------------------------------------------------------------

def test_alert_correlation():

    parsed = parse_alert(ALERTS[1])

    related = find_related_alerts(
        parsed,
        ALERTS
    )

    assert len(related) == 1
    assert related[0]["alert_id"] == "A001"


# ------------------------------------------------------------
# Test 4 — Suspicious Login Risk
# ------------------------------------------------------------

def test_suspicious_login_risk():

    parsed = parse_alert(ALERTS[1])

    related = find_related_alerts(
        parsed,
        ALERTS
    )

    risk = assess_risk(
        parsed,
        related
    )

    assert risk["risk_level"] == "CRITICAL"
    assert risk["risk_score"] == 90


# ------------------------------------------------------------
# Test 5 — Normal Login Risk
# ------------------------------------------------------------

def test_normal_login_risk():

    parsed = parse_alert(ALERTS[2])

    related = find_related_alerts(
        parsed,
        ALERTS
    )

    risk = assess_risk(
        parsed,
        related
    )

    assert risk["risk_level"] == "LOW"
    assert risk["risk_score"] == 10


# ------------------------------------------------------------
# Test 6 — Critical Malware Risk
# ------------------------------------------------------------

def test_critical_malware_risk():

    parsed = parse_alert(ALERTS[3])

    related = find_related_alerts(
        parsed,
        ALERTS
    )

    risk = assess_risk(
        parsed,
        related
    )

    assert risk["risk_level"] == "CRITICAL"
    assert risk["risk_score"] == 90


# ------------------------------------------------------------
# Test 7 — Required Risk Fields
# ------------------------------------------------------------

def test_risk_output_structure():

    parsed = parse_alert(ALERTS[1])

    related = find_related_alerts(
        parsed,
        ALERTS
    )

    risk = assess_risk(
        parsed,
        related
    )

    assert "risk_score" in risk
    assert "risk_level" in risk
    assert "reasons" in risk
    assert "risk_factors" in risk


print("✓ Automated test file created successfully")
