
from typing import Dict, Any


def generate_triage_report(
    agent,
    alert: Dict[str, Any]
) -> None:
    """
    Run SOC-Aid and display a professional analyst-style report.
    """

    result = agent.invoke({
        "alert": alert
    })

    print("\n" + "=" * 70)
    print("                     SOC-Aid TRIAGE REPORT")
    print("=" * 70)

    # --------------------------------------------------------
    # Error Handling
    # --------------------------------------------------------

    if result.get("error"):

        print("\nSTATUS          : ERROR")
        print("MESSAGE         :", result["error"])
        print("\nHuman analyst review is required.")
        print("=" * 70)

        return

    # --------------------------------------------------------
    # Alert Information
    # --------------------------------------------------------

    parsed = result["parsed_alert"]
    risk = result["risk_assessment"]

    print("\n[ALERT INFORMATION]")

    print(f"Alert ID        : {parsed['alert_id']}")
    print(f"Timestamp       : {parsed['timestamp']}")
    print(f"User            : {parsed['user']}")
    print(f"Source IP       : {parsed['source_ip']}")
    print(f"Event Type      : {parsed['event_type']}")
    print(f"Severity        : {parsed['severity'].upper()}")

    # --------------------------------------------------------
    # Risk Assessment
    # --------------------------------------------------------

    print("\n[RISK ASSESSMENT]")

    print(
        f"Risk Level      : {risk['risk_level']}"
    )

    print(
        f"Risk Score      : {risk['risk_score']}/100"
    )

    # --------------------------------------------------------
    # Reasons
    # --------------------------------------------------------

    print("\n[REASONS]")

    if risk["reasons"]:

        for reason in risk["reasons"]:
            print(f"- {reason}")

    else:

        print(
            "- No additional rule-based risk factors detected."
        )

    # --------------------------------------------------------
    # Related Alerts
    # --------------------------------------------------------

    print("\n[RELATED ALERTS]")

    if result["related_alerts"]:

        for related in result["related_alerts"]:

            print(
                f"- {related['alert_id']} | "
                f"{related['event_type']} | "
                f"{related['source_ip']}"
            )

    else:

        print("- No related alerts found.")

    # --------------------------------------------------------
    # AI Analysis
    # --------------------------------------------------------

    print("\n[AI ANALYSIS]")
    print(result["analysis"])

    # --------------------------------------------------------
    # Recommendation
    # --------------------------------------------------------

    print("\n[RECOMMENDED ACTION]")
    print(result["recommendation"])

    # --------------------------------------------------------
    # Human Decision
    # --------------------------------------------------------

    print("\n[DECISION]")
    print("Human SOC analyst review required.")

    print("\n" + "=" * 70)
    print("                 SOC-Aid analysis complete")
    print("=" * 70)
