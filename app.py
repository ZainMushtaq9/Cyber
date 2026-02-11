"""
AI-Enabled Smart Grid Cybersecurity Framework
Backend Application - Chunks 0, 1, 2
"""

from flask import Flask, jsonify, request
from flask_cors import CORS
import random
import logging
from datetime import datetime
import json
import os

app = Flask(__name__)
CORS(app)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# ========================================================
# GLOBAL STATE & CONFIGURATION
# ========================================================

# Thresholds for anomaly detection
VOLTAGE_THRESHOLD = 15.0  # Voltage deviation threshold in volts
LATENCY_THRESHOLD = 50.0  # Network latency threshold in ms

# Baseline values
BASELINE_VOLTAGE = 230.0  # Volts
BASELINE_LATENCY = 20.0   # Milliseconds

# Event history storage
event_history = []
metrics = {
    "total_events": 0,
    "total_anomalies": 0,
    "detection_rate": 0.0
}

# ========================================================
# CHUNK 1: SMART GRID EVENT SIMULATION
# ========================================================

class SmartGridSimulator:
    """Simulates smart grid events with normal and attack scenarios"""
    
    COMPONENTS = [
        "Transformer_T1",
        "Transformer_T2", 
        "Substation_S1",
        "Substation_S2",
        "Generator_G1",
        "Generator_G2",
        "Distribution_Line_D1",
        "Distribution_Line_D2"
    ]
    
    @staticmethod
    def generate_event():
        """Generate a random grid event (70% normal, 30% attack)"""
        is_attack = random.random() < 0.3
        
        component = random.choice(SmartGridSimulator.COMPONENTS)
        
        if is_attack:
            # Attack scenario - abnormal values
            voltage = BASELINE_VOLTAGE + random.uniform(-30, 30)
            frequency = random.uniform(48.5, 51.5)
            network_latency = random.uniform(10, 150)
            event_type = "attack"
        else:
            # Normal scenario - values within normal range
            voltage = BASELINE_VOLTAGE + random.uniform(-5, 5)
            frequency = random.uniform(49.8, 50.2)
            network_latency = random.uniform(10, 35)
            event_type = "normal"
        
        event = {
            "timestamp": datetime.utcnow().isoformat(),
            "component": component,
            "voltage": round(voltage, 2),
            "frequency": round(frequency, 2),
            "network_latency": round(network_latency, 2),
            "event_type": event_type
        }
        
        logger.info(f"Generated {event_type} event for {component}")
        return event


# ========================================================
# CHUNK 2: PERCEPTUAL DETECTION LAYER
# ========================================================

class DataFusionAgent:
    """Agent 1: Structures raw event data into system state"""
    
    @staticmethod
    def process(raw_event):
        """Fuse and structure incoming event data"""
        system_state = {
            "timestamp": raw_event["timestamp"],
            "component": raw_event["component"],
            "voltage": raw_event["voltage"],
            "frequency": raw_event["frequency"],
            "network_latency": raw_event["network_latency"],
            "baseline_voltage": BASELINE_VOLTAGE,
            "baseline_latency": BASELINE_LATENCY
        }
        
        logger.info(f"Data Fusion: Processed event from {raw_event['component']}")
        return system_state


class BehavioralEnvelopeAgent:
    """Agent 2: Calculates deviations from normal behavioral envelope"""
    
    @staticmethod
    def analyze(system_state):
        """Calculate deviations from baseline values"""
        voltage_deviation = abs(system_state["voltage"] - system_state["baseline_voltage"])
        latency_deviation = abs(system_state["network_latency"] - system_state["baseline_latency"])
        
        behavioral_metrics = {
            "voltage_deviation": round(voltage_deviation, 2),
            "latency_deviation": round(latency_deviation, 2),
            "frequency": system_state["frequency"]
        }
        
        logger.info(f"Behavioral Envelope: V_dev={voltage_deviation:.2f}V, L_dev={latency_deviation:.2f}ms")
        return behavioral_metrics


class AnomalyDetectionAgent:
    """Agent 3: Applies deterministic rules to detect anomalies"""
    
    @staticmethod
    def detect(behavioral_metrics):
        """Apply threshold-based anomaly detection"""
        voltage_anomaly = behavioral_metrics["voltage_deviation"] > VOLTAGE_THRESHOLD
        latency_anomaly = behavioral_metrics["latency_deviation"] > LATENCY_THRESHOLD
        
        is_anomaly = voltage_anomaly or latency_anomaly
        
        # Determine severity
        if is_anomaly:
            if voltage_anomaly and latency_anomaly:
                severity = "CRITICAL"
                alert_type = "Voltage & Latency Anomaly"
            elif voltage_anomaly:
                severity = "HIGH"
                alert_type = "Voltage Anomaly"
            else:
                severity = "MEDIUM"
                alert_type = "Latency Anomaly"
        else:
            severity = "NORMAL"
            alert_type = "No Anomaly"
        
        detection_result = {
            "is_anomaly": is_anomaly,
            "severity": severity,
            "alert_type": alert_type,
            "voltage_anomaly": voltage_anomaly,
            "latency_anomaly": latency_anomaly
        }
        
        logger.info(f"Anomaly Detection: {alert_type} - Severity: {severity}")
        return detection_result


class PerceptualLayer:
    """Orchestrates the perceptual detection layer processing"""
    
    @staticmethod
    def process_event(raw_event):
        """Process event through the complete perceptual layer"""
        
        # Step 1: Data Fusion
        system_state = DataFusionAgent.process(raw_event)
        
        # Step 2: Behavioral Analysis
        behavioral_metrics = BehavioralEnvelopeAgent.analyze(system_state)
        
        # Step 3: Anomaly Detection
        detection_result = AnomalyDetectionAgent.detect(behavioral_metrics)
        
        # Combine results
        processed_result = {
            "event": raw_event,
            "behavioral_metrics": behavioral_metrics,
            "detection": detection_result
        }
        
        return processed_result


# ========================================================
# LOGGING SYSTEM
# ========================================================

class EventLogger:
    """Structured logging system for grid events"""
    
    LOG_FILE = "event_logs.jsonl"
    
    @staticmethod
    def log_event(event_data):
        """Log event to JSONL file"""
        log_entry = {
            "timestamp": event_data["event"]["timestamp"],
            "component": event_data["event"]["component"],
            "voltage": event_data["event"]["voltage"],
            "frequency": event_data["event"]["frequency"],
            "network_latency": event_data["event"]["network_latency"],
            "voltage_deviation": event_data["behavioral_metrics"]["voltage_deviation"],
            "latency_deviation": event_data["behavioral_metrics"]["latency_deviation"],
            "is_anomaly": event_data["detection"]["is_anomaly"],
            "severity": event_data["detection"]["severity"],
            "alert_type": event_data["detection"]["alert_type"]
        }
        
        # Append to JSONL file
        with open(EventLogger.LOG_FILE, 'a') as f:
            f.write(json.dumps(log_entry) + '\n')
        
        logger.info(f"Event logged: {log_entry['alert_type']}")
    
    @staticmethod
    def get_logs(limit=None):
        """Retrieve logged events"""
        if not os.path.exists(EventLogger.LOG_FILE):
            return []
        
        logs = []
        with open(EventLogger.LOG_FILE, 'r') as f:
            for line in f:
                logs.append(json.loads(line.strip()))
        
        if limit:
            return logs[-limit:]
        return logs


# ========================================================
# METRICS TRACKING
# ========================================================

def update_metrics(is_anomaly):
    """Update global metrics"""
    metrics["total_events"] += 1
    if is_anomaly:
        metrics["total_anomalies"] += 1
    
    if metrics["total_events"] > 0:
        metrics["detection_rate"] = round(
            (metrics["total_anomalies"] / metrics["total_events"]) * 100, 2
        )


# ========================================================
# API ENDPOINTS
# ========================================================

@app.route('/', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        "status": "running",
        "message": "AI-Enabled Smart Grid Cybersecurity Framework",
        "version": "1.0.0",
        "chunks_active": [0, 1, 2]
    }), 200


@app.route('/simulate', methods=['GET'])
def simulate_event():
    """Simulate a grid event and process through perceptual layer"""
    try:
        # Step 1: Generate grid event
        raw_event = SmartGridSimulator.generate_event()
        
        # Step 2: Process through perceptual layer
        processed_result = PerceptualLayer.process_event(raw_event)
        
        # Step 3: Log event
        EventLogger.log_event(processed_result)
        
        # Step 4: Update metrics
        update_metrics(processed_result["detection"]["is_anomaly"])
        
        # Step 5: Add to in-memory history
        event_history.append(processed_result)
        if len(event_history) > 100:  # Keep last 100 events
            event_history.pop(0)
        
        return jsonify(processed_result), 200
        
    except Exception as e:
        logger.error(f"Error in simulation: {str(e)}")
        return jsonify({"error": str(e)}), 500


@app.route('/metrics', methods=['GET'])
def get_metrics():
    """Get system metrics"""
    return jsonify(metrics), 200


@app.route('/logs', methods=['GET'])
def get_logs():
    """Get event logs"""
    limit = request.args.get('limit', type=int)
    logs = EventLogger.get_logs(limit)
    return jsonify({
        "logs": logs,
        "total_logs": len(logs)
    }), 200


@app.route('/history', methods=['GET'])
def get_history():
    """Get in-memory event history"""
    limit = request.args.get('limit', default=10, type=int)
    return jsonify({
        "history": event_history[-limit:],
        "total_in_memory": len(event_history)
    }), 200


@app.route('/export', methods=['GET'])
def export_logs():
    """Export logs in CSV format"""
    logs = EventLogger.get_logs()
    
    if not logs:
        return jsonify({"error": "No logs available"}), 404
    
    # Create CSV content
    csv_lines = ["Timestamp,Component,Voltage,Frequency,Latency,V_Deviation,L_Deviation,Anomaly,Severity,Alert_Type"]
    
    for log in logs:
        line = f"{log['timestamp']},{log['component']},{log['voltage']},{log['frequency']},{log['network_latency']},{log['voltage_deviation']},{log['latency_deviation']},{log['is_anomaly']},{log['severity']},{log['alert_type']}"
        csv_lines.append(line)
    
    csv_content = '\n'.join(csv_lines)
    
    return csv_content, 200, {
        'Content-Type': 'text/csv',
        'Content-Disposition': 'attachment; filename=grid_events.csv'
    }


# ========================================================
# FUTURE LAYER PLACEHOLDERS
# ========================================================

@app.route('/threat-model', methods=['POST'])
def threat_model():
    """Placeholder for Threat Modeling Layer"""
    return jsonify({
        "status": "not_implemented",
        "message": "Threat Modeling Layer - Future Implementation"
    }), 501


@app.route('/cascade-predict', methods=['POST'])
def cascade_predict():
    """Placeholder for Cascade Prediction Layer"""
    return jsonify({
        "status": "not_implemented",
        "message": "Cascade Prediction Layer - Future Implementation"
    }), 501


# ========================================================
# APPLICATION ENTRY POINT
# ========================================================

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
