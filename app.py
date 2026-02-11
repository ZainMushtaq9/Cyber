from fastapi import FastAPI
from pydantic import BaseModel
import random
import networkx as nx
from groq import Groq
import os

app = FastAPI()

# -----------------------------
# Groq LLaMA Setup
# -----------------------------

groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))


# -----------------------------
# Smart Grid Simulator
# -----------------------------

class SmartGridSimulator:

    def generate_normal_event(self):
        return {
            "component": "DER",
            "voltage": random.randint(220, 240),
            "frequency": round(random.uniform(49.8, 50.2), 2),
            "latency": random.randint(20, 80)
        }

    def generate_voltage_attack(self):
        return {
            "component": "DER",
            "voltage": random.randint(255, 280),
            "frequency": round(random.uniform(48.5, 49.0), 2),
            "latency": random.randint(200, 400)
        }


simulator = SmartGridSimulator()


# -----------------------------
# Agents - Chunk 1 & 2
# -----------------------------

class DataFusionAgent:
    def process(self, raw_event):
        return {
            "DER": {
                "voltage": raw_event["voltage"],
                "frequency": raw_event["frequency"]
            },
            "Network": {
                "latency": raw_event["latency"]
            }
        }


class BehavioralEnvelopeAgent:
    def __init__(self):
        self.nominal_voltage = 230
        self.nominal_latency = 50

    def process(self, fused_state):
        voltage = fused_state["DER"]["voltage"]
        latency = fused_state["Network"]["latency"]

        return {
            "voltage_deviation": voltage - self.nominal_voltage,
            "latency_deviation": latency - self.nominal_latency
        }


class AnomalyDetectionAgent:
    def process(self, metrics):

        if abs(metrics["voltage_deviation"]) > 15:
            return {
                "type": "Voltage Anomaly",
                "severity": "High"
            }

        if abs(metrics["latency_deviation"]) > 120:
            return {
                "type": "Network Latency Anomaly",
                "severity": "Medium"
            }

        return None


data_fusion = DataFusionAgent()
behavioral = BehavioralEnvelopeAgent()
anomaly = AnomalyDetectionAgent()


# -----------------------------
# Threat Modeling
# -----------------------------

def model_threat(alert):
    if alert["type"] == "Voltage Anomaly":
        return {
            "attack_type": "Data Injection",
            "confidence": 0.82
        }

    if alert["type"] == "Network Latency Anomaly":
        return {
            "attack_type": "Denial of Service",
            "confidence": 0.75
        }

    return {
        "attack_type": "Unknown",
        "confidence": 0.5
    }


# -----------------------------
# Cascade Prediction
# -----------------------------

def predict_cascade():
    G = nx.DiGraph()
    G.add_edge("DER", "Substation")
    G.add_edge("Substation", "Grid")

    return {
        "propagation_path": list(G.edges),
        "cascade_risk": "High"
    }


# -----------------------------
# Decision Engine
# -----------------------------

def make_decision(threat_model, cascade_data):

    threat_score = threat_model["confidence"]

    if cascade_data["cascade_risk"] == "High":
        threat_score += 0.1

    if threat_score >= 0.8:
        mitigation = "Isolate DER"
    elif threat_score >= 0.6:
        mitigation = "Monitor and Throttle"
    else:
        mitigation = "Log Only"

    return {
        "threat_score": round(threat_score, 2),
        "mitigation": mitigation
    }


# -----------------------------
# Groq Explanation
# -----------------------------

def generate_explanation(data):

    prompt = f"""
    You are a cybersecurity analyst for smart grid systems.

    Threat Type: {data['attack_type']}
    Confidence: {data['confidence']}
    Cascade Risk: {data['cascade_risk']}
    Mitigation Action: {data['mitigation']}

    Provide a technical explanation of the situation.
    """

    response = groq_client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
        max_tokens=250
    )

    return response.choices[0].message.content


# -----------------------------
# API Endpoint
# -----------------------------

@app.get("/simulate")
def simulate():

    # Step 1: Generate Event
    if random.random() < 0.3:
        event = simulator.generate_voltage_attack()
    else:
        event = simulator.generate_normal_event()

    # Step 2: Perceptual Layer
    fused = data_fusion.process(event)
    metrics = behavioral.process(fused)
    alert = anomaly.process(metrics)

    if not alert:
        return {
            "event": event,
            "status": "Normal Operation"
        }

    # Step 3: Threat Modeling
    threat_model = model_threat(alert)

    # Step 4: Cascade Prediction
    cascade = predict_cascade()

    # Step 5: Decision
    decision = make_decision(threat_model, cascade)

    # Step 6: LLM Explanation
    explanation = generate_explanation({
        "attack_type": threat_model["attack_type"],
        "confidence": threat_model["confidence"],
        "cascade_risk": cascade["cascade_risk"],
        "mitigation": decision["mitigation"]
    })

    return {
        "event": event,
        "alert": alert,
        "threat_model": threat_model,
        "cascade": cascade,
        "decision": decision,
        "llm_explanation": explanation
        }
