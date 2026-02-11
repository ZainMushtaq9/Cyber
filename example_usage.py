"""
Example Usage Script for Smart Grid Cybersecurity Framework
Demonstrates how to interact with the API programmatically
"""

import requests
import json
import time

# Configuration
BASE_URL = "https://cyber-production-7ec6.up.railway.app"
# For local testing, use: BASE_URL = "http://localhost:5000"


def check_health():
    """Check if the system is running"""
    print("=== Checking System Health ===")
    response = requests.get(f"{BASE_URL}/")
    data = response.json()
    print(f"Status: {data['status']}")
    print(f"Version: {data['version']}")
    print(f"Active Chunks: {data['chunks_active']}\n")


def simulate_single_event():
    """Simulate a single grid event"""
    print("=== Simulating Single Event ===")
    response = requests.get(f"{BASE_URL}/simulate")
    data = response.json()
    
    # Extract event details
    event = data['event']
    detection = data['detection']
    metrics = data['behavioral_metrics']
    
    print(f"Component: {event['component']}")
    print(f"Voltage: {event['voltage']} V")
    print(f"Frequency: {event['frequency']} Hz")
    print(f"Latency: {event['network_latency']} ms")
    print(f"\nVoltage Deviation: {metrics['voltage_deviation']} V")
    print(f"Latency Deviation: {metrics['latency_deviation']} ms")
    print(f"\nAnomaly Detected: {detection['is_anomaly']}")
    print(f"Severity: {detection['severity']}")
    print(f"Alert Type: {detection['alert_type']}\n")


def simulate_multiple_events(count=10):
    """Simulate multiple events and collect statistics"""
    print(f"=== Simulating {count} Events ===")
    
    normal_count = 0
    anomaly_count = 0
    severity_counts = {'NORMAL': 0, 'MEDIUM': 0, 'HIGH': 0, 'CRITICAL': 0}
    
    for i in range(1, count + 1):
        response = requests.get(f"{BASE_URL}/simulate")
        data = response.json()
        
        detection = data['detection']
        severity = detection['severity']
        
        severity_counts[severity] += 1
        
        if detection['is_anomaly']:
            anomaly_count += 1
            print(f"Event {i}: ⚠️  ANOMALY ({severity})")
        else:
            normal_count += 1
            print(f"Event {i}: ✅ Normal")
        
        time.sleep(0.5)  # Small delay
    
    print(f"\n--- Statistics ---")
    print(f"Total Events: {count}")
    print(f"Normal: {normal_count} ({normal_count/count*100:.1f}%)")
    print(f"Anomalies: {anomaly_count} ({anomaly_count/count*100:.1f}%)")
    print(f"\nSeverity Breakdown:")
    for severity, count_val in severity_counts.items():
        if count_val > 0:
            print(f"  {severity}: {count_val}")
    print()


def get_current_metrics():
    """Get current system metrics"""
    print("=== Current System Metrics ===")
    response = requests.get(f"{BASE_URL}/metrics")
    data = response.json()
    
    print(f"Total Events: {data['total_events']}")
    print(f"Total Anomalies: {data['total_anomalies']}")
    print(f"Detection Rate: {data['detection_rate']}%\n")


def get_recent_history(limit=5):
    """Get recent event history"""
    print(f"=== Recent {limit} Events ===")
    response = requests.get(f"{BASE_URL}/history?limit={limit}")
    data = response.json()
    
    for event_data in data['history']:
        event = event_data['event']
        detection = event_data['detection']
        
        status = "⚠️  ANOMALY" if detection['is_anomaly'] else "✅ Normal"
        print(f"{event['timestamp'][:19]} | {event['component']} | {status}")
    print()


def export_logs():
    """Export logs to CSV"""
    print("=== Exporting Logs ===")
    response = requests.get(f"{BASE_URL}/export")
    
    # Save to file
    with open('exported_logs.csv', 'w') as f:
        f.write(response.text)
    
    lines = response.text.split('\n')
    print(f"Exported {len(lines)-1} events to exported_logs.csv\n")


def continuous_monitoring(duration_seconds=30):
    """Monitor system continuously for specified duration"""
    print(f"=== Continuous Monitoring ({duration_seconds}s) ===")
    
    start_time = time.time()
    event_count = 0
    
    while time.time() - start_time < duration_seconds:
        response = requests.get(f"{BASE_URL}/simulate")
        data = response.json()
        
        event_count += 1
        detection = data['detection']
        event = data['event']
        
        if detection['is_anomaly']:
            print(f"[{time.strftime('%H:%M:%S')}] ⚠️  ANOMALY on {event['component']} - {detection['severity']}")
        else:
            print(f"[{time.strftime('%H:%M:%S')}] ✅ Normal on {event['component']}")
        
        time.sleep(2)  # Check every 2 seconds
    
    print(f"\nMonitored {event_count} events in {duration_seconds} seconds\n")


if __name__ == "__main__":
    print("\n" + "="*60)
    print("  SMART GRID CYBERSECURITY FRAMEWORK - USAGE EXAMPLES")
    print("="*60 + "\n")
    
    # Example 1: Check system health
    check_health()
    
    # Example 2: Simulate single event
    simulate_single_event()
    
    # Example 3: Simulate multiple events
    simulate_multiple_events(10)
    
    # Example 4: Get current metrics
    get_current_metrics()
    
    # Example 5: Get recent history
    get_recent_history(5)
    
    # Example 6: Export logs
    export_logs()
    
    # Example 7: Continuous monitoring (uncomment to run)
    # continuous_monitoring(30)
    
    print("="*60)
    print("  All examples completed successfully!")
    print("="*60 + "\n")
