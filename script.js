/**
 * AI-Enabled Smart Grid Cybersecurity Framework
 * Frontend JavaScript - API Integration & UI Management
 */

// =========================================
// CONFIGURATION
// =========================================

const API_BASE_URL = 'https://cyber-production-7ec6.up.railway.app';

// =========================================
// DOM ELEMENTS
// =========================================

const simulateBtn = document.getElementById('simulateBtn');
const loadingOverlay = document.getElementById('loadingOverlay');
const systemStatus = document.getElementById('systemStatus');
const systemStatusText = document.getElementById('systemStatusText');

// Event Panel
const eventTimestamp = document.getElementById('eventTimestamp');
const eventContent = document.getElementById('eventContent');

// Status Panel
const statusBadge = document.getElementById('statusBadge');
const statusMessage = document.getElementById('statusMessage');

// Metrics Panel
const voltageDeviation = document.getElementById('voltageDeviation');
const latencyDeviation = document.getElementById('latencyDeviation');
const frequencyDeviation = document.getElementById('frequencyDeviation');

// Alert Panel
const alertContent = document.getElementById('alertContent');

// =========================================
// EVENT LISTENERS
// =========================================

document.addEventListener('DOMContentLoaded', () => {
    // Check backend health on load
    checkBackendHealth();
    
    // Simulate button click handler
    simulateBtn.addEventListener('click', handleSimulation);
});

// =========================================
// BACKEND HEALTH CHECK
// =========================================

async function checkBackendHealth() {
    try {
        const response = await fetch(`${API_BASE_URL}/`);
        const data = await response.json();
        
        if (data.status === "Smart Grid Agentic Framework Running") {
            updateSystemStatus('online', 'System Online & Ready');
        } else {
            updateSystemStatus('warning', 'System Status Unknown');
        }
    } catch (error) {
        updateSystemStatus('offline', 'Backend Offline');
        console.error('Health check failed:', error);
    }
}

// =========================================
// SIMULATION HANDLER
// =========================================

async function handleSimulation() {
    // Show loading overlay
    showLoading(true);
    
    try {
        // Call backend API
        const response = await fetch(`${API_BASE_URL}/simulate`);
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const data = await response.json();
        
        // Update UI with response data
        updateDashboard(data);
        
    } catch (error) {
        handleError(error);
    } finally {
        // Hide loading overlay
        showLoading(false);
    }
}

// =========================================
// DASHBOARD UPDATE
// =========================================

function updateDashboard(data) {
    // Update event data
    updateEventPanel(data.event);
    
    // Update status
    updateStatusPanel(data.status, data.alert);
    
    // Update metrics
    updateMetricsPanel(data.metrics);
    
    // Update alerts
    updateAlertPanel(data.alert);
}

// =========================================
// EVENT PANEL UPDATE
// =========================================

function updateEventPanel(event) {
    if (!event) return;
    
    // Update timestamp
    const timestamp = new Date(event.timestamp).toLocaleString();
    eventTimestamp.textContent = timestamp;
    
    // Create event data display
    eventContent.innerHTML = `
        <div class="event-data">
            <div class="data-row">
                <span class="data-label">Component</span>
                <span class="data-value">${event.component}</span>
            </div>
            <div class="data-row">
                <span class="data-label">Voltage (V)</span>
                <span class="data-value">${event.voltage}</span>
            </div>
            <div class="data-row">
                <span class="data-label">Frequency (Hz)</span>
                <span class="data-value">${event.frequency}</span>
            </div>
            <div class="data-row">
                <span class="data-label">Latency (ms)</span>
                <span class="data-value">${event.latency}</span>
            </div>
        </div>
    `;
}

// =========================================
// STATUS PANEL UPDATE
// =========================================

function updateStatusPanel(status, alert) {
    // Remove existing classes
    statusBadge.className = 'status-badge';
    
    if (status === 'Normal Operation') {
        // Normal status
        statusBadge.classList.add('normal');
        statusBadge.innerHTML = '<span class="badge-text">✓ NORMAL</span>';
        statusMessage.textContent = 'All systems operating within normal parameters';
    } else if (status === 'Anomaly Detected') {
        // Anomaly detected
        statusBadge.classList.add('anomaly');
        statusBadge.innerHTML = '<span class="badge-text">⚠ ANOMALY</span>';
        
        const anomalyCount = alert?.total_anomalies || 0;
        statusMessage.textContent = `${anomalyCount} anomal${anomalyCount > 1 ? 'ies' : 'y'} detected in grid operations`;
    }
}

// =========================================
// METRICS PANEL UPDATE
// =========================================

function updateMetricsPanel(metrics) {
    if (!metrics) return;
    
    // Voltage Deviation
    const voltageValue = metrics.voltage_deviation || 0;
    voltageDeviation.textContent = `${voltageValue > 0 ? '+' : ''}${voltageValue} V`;
    voltageDeviation.className = 'metric-value ' + getMetricClass(Math.abs(voltageValue), 15, 25);
    
    // Latency Deviation
    const latencyValue = metrics.latency_deviation || 0;
    latencyDeviation.textContent = `${latencyValue > 0 ? '+' : ''}${latencyValue} ms`;
    latencyDeviation.className = 'metric-value ' + getMetricClass(Math.abs(latencyValue), 120, 200);
    
    // Frequency Deviation
    const frequencyValue = metrics.frequency_deviation || 0;
    frequencyDeviation.textContent = `${frequencyValue > 0 ? '+' : ''}${frequencyValue} Hz`;
    frequencyDeviation.className = 'metric-value ' + getMetricClass(Math.abs(frequencyValue), 0.3, 0.5);
}

// =========================================
// ALERT PANEL UPDATE
// =========================================

function updateAlertPanel(alert) {
    if (!alert || !alert.anomaly_detected) {
        // No anomalies
        alertContent.innerHTML = '<div class="no-alerts">No anomalies detected</div>';
        return;
    }
    
    // Display anomalies
    const anomalies = alert.anomalies || [];
    
    let alertHTML = '';
    anomalies.forEach(anomaly => {
        const severityClass = anomaly.severity.toLowerCase();
        alertHTML += `
            <div class="alert-item ${severityClass}">
                <div class="alert-type">${anomaly.type}</div>
                <div>
                    <span class="alert-severity ${severityClass}">${anomaly.severity}</span>
                    <span class="alert-details">Deviation: ${anomaly.deviation}</span>
                </div>
            </div>
        `;
    });
    
    alertContent.innerHTML = alertHTML;
}

// =========================================
// UTILITY FUNCTIONS
// =========================================

function getMetricClass(value, warningThreshold, dangerThreshold) {
    if (value >= dangerThreshold) return 'danger';
    if (value >= warningThreshold) return 'warning';
    return 'normal';
}

function updateSystemStatus(status, text) {
    systemStatusText.textContent = text;
    
    systemStatus.style.background = {
        'online': '#10b981',
        'warning': '#f59e0b',
        'offline': '#ef4444'
    }[status] || '#6b7280';
}

function showLoading(show) {
    if (show) {
        loadingOverlay.classList.add('active');
        simulateBtn.disabled = true;
    } else {
        loadingOverlay.classList.remove('active');
        simulateBtn.disabled = false;
    }
}

function handleError(error) {
    console.error('Simulation error:', error);
    
    // Update status to show error
    updateSystemStatus('offline', 'Error: Unable to connect to backend');
    
    // Show error in alert panel
    alertContent.innerHTML = `
        <div class="alert-item high">
            <div class="alert-type">System Error</div>
            <div class="alert-details">
                ${error.message || 'Failed to communicate with backend. Please check your connection.'}
            </div>
        </div>
    `;
    
    // Show error badge
    statusBadge.className = 'status-badge anomaly';
    statusBadge.innerHTML = '<span class="badge-text">⚠ ERROR</span>';
    statusMessage.textContent = 'Backend communication failure';
}

// =========================================
// AUTO-REFRESH (Optional)
// =========================================

// Uncomment to enable auto-simulation every 10 seconds
/*
setInterval(() => {
    if (!loadingOverlay.classList.contains('active')) {
        handleSimulation();
    }
}, 10000);
*/

// =========================================
// CONSOLE INFO
// =========================================

console.log('%c🔒 AI-Enabled Smart Grid Cybersecurity Framework', 'color: #3b82f6; font-size: 16px; font-weight: bold;');
console.log('%cBackend API:', 'font-weight: bold;', API_BASE_URL);
console.log('%cSystem initialized and ready', 'color: #10b981;');
