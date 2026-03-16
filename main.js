// Show result box
function showResult(id, message, isError = false) {
  const box = document.getElementById(id);
  box.classList.add('show');
  box.className = 'result-box show ' + (isError ? 'error' : 'success');
  box.innerText = message;
}

// Step 1 - Run Forensics
async function startForensics() {
  showResult('forensics-result', '⏳ Running forensics... Please wait...', false);
  
  const checkboxes = document.querySelectorAll('.checkbox-group input:checked');
  const forensic_types = checkboxes.length > 0 
    ? Array.from(checkboxes).map(cb => cb.value)
    : ['all'];

  try {
    const res = await fetch('/api/start-forensics', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({forensic_types: forensic_types})
    });
    const data = await res.json();
    
    if (data.status === 'success') {
      showResult('forensics-result', 
        `✅ Forensics Complete!\n` +
        `Session ID: ${data.session_id}\n` +
        `Evidence Hash: ${data.evidence_hash}\n` +
        `Types: ${data.forensics_completed.join(', ')}`
      );
    } else {
      showResult('forensics-result', `❌ Error: ${data.error}`, true);
    }
  } catch (err) {
    showResult('forensics-result', `❌ Error: ${err.message}`, true);
  }
}

// Step 2 - Register Blockchain
async function registerBlockchain() {
  showResult('blockchain-result', '⏳ Registering on blockchain...', false);
  
  try {
    const res = await fetch('/api/register-blockchain', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'}
    });
    const data = await res.json();
    
    if (data.status === 'success') {
      showResult('blockchain-result',
        `✅ Blockchain Registration Complete!\n` +
        `Evidence ID: ${data.evidence_id}\n` +
        `Transaction: ${data.blockchain_data.transaction_hash}\n` +
        `Block Number: ${data.blockchain_data.block_number}`
      );
    } else {
      showResult('blockchain-result', `❌ Error: ${data.error}`, true);
    }
  } catch (err) {
    showResult('blockchain-result', `❌ Error: ${err.message}`, true);
  }
}

// Step 3 - Generate Report
async function generateReport() {
  showResult('report-result', '⏳ Generating AI report... Please wait...', false);
  
  try {
    const res = await fetch('/api/generate-report', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'}
    });
    const data = await res.json();
    
    if (data.status === 'success') {
      showResult('report-result',
        `✅ Report Generated!\n\n` +
        `${data.report.report_text.substring(0, 800)}...`
      );
    } else {
      showResult('report-result', `❌ Error: ${data.error}`, true);
    }
  } catch (err) {
    showResult('report-result', `❌ Error: ${err.message}`, true);
  }
}

// Download Report
function downloadReport(type) {
  window.location.href = `/api/download-report/${type}`;
}

// Check Status
async function checkStatus() {
  try {
    const res = await fetch('/api/session-status');
    const data = await res.json();
    showResult('status-result',
      `📊 Session Status:\n` +
      `Status: ${data.status}\n` +
      `Session ID: ${data.session_id || 'None'}\n` +
      `Blockchain Registered: ${data.blockchain_registered || false}\n` +
      `Report Generated: ${data.report_generated || false}`
    );
  } catch (err) {
    showResult('status-result', `❌ Error: ${err.message}`, true);
  }
}