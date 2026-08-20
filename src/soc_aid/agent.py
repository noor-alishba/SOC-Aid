
import json
from typing import Dict, Any, List

from langchain_groq import ChatGroq
from langgraph.graph import StateGraph, END

from .models import SOCAidState
from .tools import (
    parse_alert,
    find_related_alerts,
    assess_risk
)


def build_soc_aid_agent(
    llm,
    alerts: List[Dict[str, Any]]
):
    """
    Build and compile the SOC-Aid LangGraph agent.
    """

    # --------------------------------------------------------
    # Node 1: Parse Alert
    # --------------------------------------------------------

    def parse_alert_node(state: SOCAidState) -> SOCAidState:

        try:
            parsed = parse_alert(state["alert"])

            return {
                **state,
                "parsed_alert": parsed,
                "error": ""
            }

        except Exception as e:

            return {
                **state,
                "error": f"Alert parsing failed: {str(e)}"
            }

    # --------------------------------------------------------
    # Node 2: Correlate Alerts
    # --------------------------------------------------------

    def correlation_node(state: SOCAidState) -> SOCAidState:

        if state.get("error"):
            return state

        try:

            related = find_related_alerts(
                state["parsed_alert"],
                alerts
            )

            return {
                **state,
                "related_alerts": related
            }

        except Exception as e:

            return {
                **state,
                "error": f"Alert correlation failed: {str(e)}"
            }

    # --------------------------------------------------------
    # Node 3: Risk Assessment
    # --------------------------------------------------------

    def risk_node(state: SOCAidState) -> SOCAidState:

        if state.get("error"):
            return state

        try:

            risk = assess_risk(
                state["parsed_alert"],
                state["related_alerts"]
            )

            return {
                **state,
                "risk_assessment": risk
            }

        except Exception as e:

            return {
                **state,
                "error": f"Risk assessment failed: {str(e)}"
            }

    # --------------------------------------------------------
    # Node 4: Evidence-Aware LLM Analysis
    # --------------------------------------------------------

    def analysis_node(state: SOCAidState) -> SOCAidState:

        if state.get("error"):
            return state

        try:

            alert = state["parsed_alert"]
            related = state["related_alerts"]
            risk = state["risk_assessment"]

            prompt = f"""
You are SOC-Aid, an explainable AI assistant
for Security Operations Center (SOC) analysts.

Analyze the security alert using ONLY the evidence provided.

CURRENT ALERT:
{json.dumps(alert, indent=2)}

RELATED ALERTS:
{json.dumps(related, indent=2)}

RULE-BASED RISK ASSESSMENT:
{json.dumps(risk, indent=2)}

EVIDENCE RULES:

1. FACT
Only describe information directly present in the evidence as FACT.

2. INFERENCE
If you make a reasonable interpretation that is not directly proven,
clearly label it as INFERENCE.

3. UNKNOWN
If the evidence does not provide enough information, explicitly state:
"This cannot be determined from the available evidence."

4. NEVER claim that:
- the IP belongs to an attacker
- credentials were compromised
- malware spread
- lateral movement occurred
- data exfiltration occurred
- MFA was enabled or bypassed
- privilege escalation occurred

unless the provided evidence explicitly proves it.

5. Recommendations are suggestions for human investigation,
not confirmed facts.

Use exactly these sections:

1. What happened?
2. Why is it suspicious or normal?
3. Evidence
4. Known vs Unknown
5. Recommended Investigation

Keep the response concise and evidence-based.

Remember:
The final decision must remain with a human SOC analyst.
"""

            response = llm.invoke(prompt)

            return {
                **state,
                "analysis": response.content
            }

        except Exception as e:

            return {
                **state,
                "error": f"LLM analysis failed: {str(e)}"
            }

    # --------------------------------------------------------
    # Node 5: Recommendation
    # --------------------------------------------------------

    def recommendation_node(state: SOCAidState) -> SOCAidState:

        if state.get("error"):
            return state

        try:

            level = state["risk_assessment"]["risk_level"]

            recommendations = {

                "LOW":
                    "Monitor the activity and close the alert "
                    "if no additional suspicious evidence is found.",

                "MEDIUM":
                    "Review related activity and verify whether "
                    "the activity was expected.",

                "HIGH":
                    "Prioritize human investigation and review "
                    "the affected account, endpoint, and related events.",

                "CRITICAL":
                    "Escalate immediately for human investigation "
                    "and review the affected account or endpoint."
            }

            recommendation = recommendations.get(
                level,
                "Perform human SOC analyst investigation."
            )

            return {
                **state,
                "recommendation": recommendation,
                "decision": "Human SOC analyst review required."
            }

        except Exception as e:

            return {
                **state,
                "error": f"Recommendation generation failed: {str(e)}"
            }

    # --------------------------------------------------------
    # Conditional Routing
    # --------------------------------------------------------

    def route_after_parse(state: SOCAidState):

        if state.get("error"):
            return "end"

        return "continue"

    def route_after_correlation(state: SOCAidState):

        if state.get("error"):
            return "end"

        return "continue"

    def route_after_risk(state: SOCAidState):

        if state.get("error"):
            return "end"

        return "continue"

    def route_after_analysis(state: SOCAidState):

        if state.get("error"):
            return "end"

        return "continue"

    # --------------------------------------------------------
    # Build LangGraph
    # --------------------------------------------------------

    workflow = StateGraph(SOCAidState)

    workflow.add_node(
        "parse_alert",
        parse_alert_node
    )

    workflow.add_node(
        "correlate_alerts",
        correlation_node
    )

    workflow.add_node(
        "assess_risk",
        risk_node
    )

    workflow.add_node(
        "analyze",
        analysis_node
    )

    workflow.add_node(
        "recommend",
        recommendation_node
    )

    workflow.set_entry_point("parse_alert")

    workflow.add_conditional_edges(
        "parse_alert",
        route_after_parse,
        {
            "continue": "correlate_alerts",
            "end": END
        }
    )

    workflow.add_conditional_edges(
        "correlate_alerts",
        route_after_correlation,
        {
            "continue": "assess_risk",
            "end": END
        }
    )

    workflow.add_conditional_edges(
        "assess_risk",
        route_after_risk,
        {
            "continue": "analyze",
            "end": END
        }
    )

    workflow.add_conditional_edges(
        "analyze",
        route_after_analysis,
        {
            "continue": "recommend",
            "end": END
        }
    )

    workflow.add_edge(
        "recommend",
        END
    )

    return workflow.compile()


def run_soc_aid(
    agent,
    alert: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Run SOC-Aid on a security alert.
    """

    return agent.invoke({
        "alert": alert
    })
