"""
AI-Enabled Cybersecurity Framework for Smart Grid Threat Modeling
FastAPI Backend - Production Ready
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import random
from typing import Dict, Optional, Any
import os
from datetime import datetime

# Initialize FastAPI app
app = FastAPI(
    title="Smart Grid Agentic Framework",
    description="AI-Enabled Cybersecurity Framework",
    version="1.0.0"
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =========================================
# CHUNK 1 - SMART GRID SIMULATOR
# =========================================

class SmartGridSimulator:
    """Simulates smart grid environment events"""
    
    def __init__(self):
        self.components = ["DER", "Transformer", "Substation", "Load_Balancer"]
    
    def generate_normal_event(self) -> Dict[str, Any]:
        """Generate normal operational event"""
        return {
            "component": random.choice(self.components),
            "voltage": round(random.uniform(220, 240), 2),
            "frequency": round(random.uniform(49.8, 50.2), 2),
            "latency": round(random.uniform(20, 80), 2),
            "timestamp": datetime.now().isoformat()
        }
    
    def generate_voltage_attack(self) -> Dict[str, Any]:
        """Generate voltage attack event"""
        return {
            "component": random.choice(self.components),
            "voltage": round(random.uniform(255, 280), 2),
            "frequency": round(random.uniform(48.5, 49.0), 2),
            "latency": round(random.uniform(200, 400), 2),
            "timestamp": datetime.now().isoformat()
        }
    
    def simulate_event(self) -> Dict[str, Any]:
        """
        Generate event with 70% normal, 30% attack distribution
        """
        if random.random() < 0.7:
            event = self.generate_normal_event()
            event["event_type"] = "normal"
        else:
            event = self.generate_voltage_attack()
            event["event_type"] = "attack"
        
        return event


# =========================================
# CHUNK 2 - PERCEPTUAL AGENTS
# =========================================

class DataFusionAgent:
    """Fuses raw event data into structured system state"""
    
    def process(self, raw_event: Dict[str, Any]) -> Dict[str, Any]:
        """
        Input: Raw event
        Output: Structured system state
        """
        fused_state = {
            "component": raw_event.get("component"),
            "voltage": raw_event.get("voltage"),
            "frequency": raw_event.get("frequency"),
            "latency": raw_event.get("latency"),
            "timestamp": raw_event.get("timestamp"),
            "processing_stage": "data_fusion_complete"
        }
        return fused_state


class BehavioralEnvelopeAgent:
    """Analyzes behavioral deviations from baseline"""
    
    VOLTAGE_BASELINE = 230
    LATENCY_BASELINE = 50
    FREQUENCY_BASELINE = 50
    
    def analyze(self, fused_state: Dict[str, Any]) -> Dict[str, Any]:
        """
        Input: Fused state
        Output: Deviation metrics
        """
        voltage = fused_state.get("voltage", self.VOLTAGE_BASELINE)
        latency = fused_state.get("latency", self.LATENCY_BASELINE)
        frequency = fused_state.get("frequency", self.FREQUENCY_BASELINE)
        
        voltage_deviation = round(voltage - self.VOLTAGE_BASELINE, 2)
        latency_deviation = round(latency - self.LATENCY_BASELINE, 2)
        frequency_deviation = round(frequency - self.FREQUENCY_BASELINE, 2)
        
        metrics = {
            "voltage_deviation": voltage_deviation,
            "latency_deviation": latency_deviation,
            "frequency_deviation": frequency_deviation,
            "voltage_status": "normal" if abs(voltage_deviation) <= 15 else "abnormal",
            "latency_status": "normal" if abs(latency_deviation) <= 120 else "abnormal",
            "processing_stage": "behavioral_analysis_complete"
        }
        
        return metrics


class AnomalyDetectionAgent:
    """Detects anomalies based on behavioral analysis"""
    
    VOLTAGE_THRESHOLD = 15
    LATENCY_THRESHOLD = 120
    
    def detect(self, metrics: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """
        Rules:
        - If |voltage_deviation| > 15 → Voltage Anomaly
        - If |latency_deviation| > 120 → Network Anomaly
        
        Output: Anomaly details or None
        """
        voltage_dev = abs(metrics.get("voltage_deviation", 0))
        latency_dev = abs(metrics.get("latency_deviation", 0))
        
        anomalies = []
        
        if voltage_dev > self.VOLTAGE_THRESHOLD:
            anomalies.append({
                "type": "Voltage Anomaly",
                "severity": "High" if voltage_dev > 25 else "Medium",
                "deviation": metrics.get("voltage_deviation")
            })
        
        if latency_dev > self.LATENCY_THRESHOLD:
            anomalies.append({
                "type": "Network Anomaly",
                "severity": "High" if latency_dev > 200 else "Medium",
                "deviation": metrics.get("latency_deviation")
            })
        
        if anomalies:
            return {
                "anomaly_detected": True,
                "anomalies": anomalies,
                "total_anomalies": len(anomalies),
                "processing_stage": "anomaly_detection_complete"
            }
        
        return None


# =========================================
# HIGHER LAYERS (ARCHITECTURAL PLACEHOLDERS)
# =========================================

class ArchitecturalAnalyzerAgent:
    """Placeholder for architectural analysis"""
    def analyze(self, data: Dict) -> Dict:
        return {"status": "placeholder", "layer": "threat_modeling"}


class ThreatContextWeaverAgent:
    """Placeholder for threat context weaving"""
    def weave(self, data: Dict) -> Dict:
        return {"status": "placeholder", "layer": "threat_modeling"}


class CascadePredictorAgent:
    """Placeholder for cascade prediction"""
    def predict(self, data: Dict) -> Dict:
        return {"status": "placeholder", "layer": "cascade"}


class GoalInferencerAgent:
    """Placeholder for goal inference"""
    def infer(self, data: Dict) -> Dict:
        return {"status": "placeholder", "layer": "cascade"}


class CognitiveOrchestratorAgent:
    """Placeholder for cognitive orchestration"""
    def orchestrate(self, data: Dict) -> Dict:
        return {"status": "placeholder", "layer": "strategic"}


class MitigationGeneratorAgent:
    """Placeholder for mitigation generation"""
    def generate(self, data: Dict) -> Dict:
        return {"status": "placeholder", "layer": "strategic"}


class ResourceSchedulerAgent:
    """Placeholder for resource scheduling"""
    def schedule(self, data: Dict) -> Dict:
        return {"status": "placeholder", "layer": "strategic"}


# =========================================
# INITIALIZE COMPONENTS
# =========================================

simulator = SmartGridSimulator()
data_fusion_agent = DataFusionAgent()
behavioral_agent = BehavioralEnvelopeAgent()
anomaly_agent = AnomalyDetectionAgent()


# =========================================
# API ENDPOINTS
# =========================================

@app.get("/")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "Smart Grid Agentic Framework Running",
        "version": "1.0.0",
        "chunks_active": ["0", "1", "2"],
        "timestamp": datetime.now().isoformat()
    }


@app.get("/simulate")
async def simulate_grid_event():
    """
    Main simulation endpoint
    
    Flow:
    Raw Event → Data Fusion → Behavioral Analysis → Anomaly Detection
    
    Returns:
    - Normal operation response or
    - Anomaly alert with metrics
    """
    try:
        # Step 1: Generate raw event
        raw_event = simulator.simulate_event()
        
        # Step 2: Data Fusion
        fused_state = data_fusion_agent.process(raw_event)
        
        # Step 3: Behavioral Analysis
        behavioral_metrics = behavioral_agent.analyze(fused_state)
        
        # Step 4: Anomaly Detection
        anomaly_result = anomaly_agent.detect(behavioral_metrics)
        
        # Prepare response
        if anomaly_result is None:
            # Normal Operation
            return {
                "status": "Normal Operation",
                "event": {
                    "component": raw_event["component"],
                    "voltage": raw_event["voltage"],
                    "frequency": raw_event["frequency"],
                    "latency": raw_event["latency"],
                    "timestamp": raw_event["timestamp"]
                },
                "metrics": {
                    "voltage_deviation": behavioral_metrics["voltage_deviation"],
                    "latency_deviation": behavioral_metrics["latency_deviation"],
                    "frequency_deviation": behavioral_metrics["frequency_deviation"]
                }
            }
        else:
            # Anomaly Detected
            return {
                "status": "Anomaly Detected",
                "event": {
                    "component": raw_event["component"],
                    "voltage": raw_event["voltage"],
                    "frequency": raw_event["frequency"],
                    "latency": raw_event["latency"],
                    "timestamp": raw_event["timestamp"]
                },
                "alert": {
                    "anomaly_detected": True,
                    "anomalies": anomaly_result["anomalies"],
                    "total_anomalies": anomaly_result["total_anomalies"]
                },
                "metrics": {
                    "voltage_deviation": behavioral_metrics["voltage_deviation"],
                    "latency_deviation": behavioral_metrics["latency_deviation"],
                    "frequency_deviation": behavioral_metrics["frequency_deviation"],
                    "voltage_status": behavioral_metrics["voltage_status"],
                    "latency_status": behavioral_metrics["latency_status"]
                }
            }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Simulation error: {str(e)}")


@app.get("/system-info")
async def system_info():
    """System architecture information"""
    return {
        "framework": "AI-Enabled Cybersecurity Framework for Smart Grid",
        "architecture": {
            "active_layers": [
                "Cloud Foundation (Chunk 0)",
                "Smart Grid Simulator (Chunk 1)",
                "Perceptual Detection Layer (Chunk 2)"
            ],
            "defined_layers": [
                "Threat Modeling Layer",
                "Cascade Prediction Layer",
                "Strategic Orchestration Layer"
            ]
        },
        "agents": {
            "active": [
                "SmartGridSimulator",
                "DataFusionAgent",
                "BehavioralEnvelopeAgent",
                "AnomalyDetectionAgent"
            ],
            "placeholder": [
                "ArchitecturalAnalyzerAgent",
                "ThreatContextWeaverAgent",
                "CascadePredictorAgent",
                "GoalInferencerAgent",
                "CognitiveOrchestratorAgent",
                "MitigationGeneratorAgent",
                "ResourceSchedulerAgent"
            ]
        }
    }


# =========================================
# APPLICATION ENTRY POINT
# =========================================

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
