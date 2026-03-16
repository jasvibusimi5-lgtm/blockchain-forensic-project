# 🔍 Cyber Forensic Tool
## Blockchain Integrated Evidence Management System

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Flask](https://img.shields.io/badge/Flask-2.0+-green)
![Blockchain](https://img.shields.io/badge/Blockchain-Ethereum-purple)
![License](https://img.shields.io/badge/License-GPL3.0-red)

A comprehensive digital forensic investigation platform that integrates multiple forensic tools, maintains evidence integrity using blockchain technology (Ethereum), and generates legal-ready reports using AI (Groq/Llama).

---

## 🎯 Problem Statement

Current cyber forensic investigations suffer from:
- ❌ Manual evidence collection across different tools
- ❌ Weak or manual chain-of-custody documentation
- ❌ Time-consuming legal report preparation
- ❌ Risk of evidence tampering or poor audit trails

---

## ✅ Solution

This platform provides:
- ✅ **Automated Forensic Tool Integration** - Disk, Memory, Network, and Log forensics
- ✅ **Blockchain Chain of Custody** - Immutable evidence tracking on Ethereum
- ✅ **AI-Powered Legal Reports** - Automated compliance and legal documentation
- ✅ **Evidence Integrity** - Cryptographic hash verification

---

## 🏗️ Architecture
```
┌─────────────────────────────────────────┐
│         Flask Web Application           │
├─────────────────────────────────────────┤
│  Frontend: HTML/CSS/JS                  │
│  Backend: Flask                         │
│  Forensic Engine                        │
└─────────────────────────────────────────┘
              ↓
┌─────────────────┐      ┌───────────────┐
│  Forensic Tools │      │  Blockchain   │
│  Execution      │←────→│  (Ethereum)   │
└─────────────────┘      └───────────────┘
              ↓                  ↓
┌─────────────────┐      ┌───────────────┐
│ Evidence Storage│      │  LLM Report   │
│ (JSON + Raw)    │─────→│  (Groq/Llama) │
└─────────────────┘      └───────────────┘
```

---

## 📂 Project Structure
```
blockchain_forensic_project/
│
├── app.py                     # Main Flask application
├── config.py                  # Configuration settings
├── requirements.txt           # Python dependencies
├── README.md                  # Documentation
├── LICENSE                    # GNU License
│
├── blockchain/
│   ├── __init__.py
│   ├── blockchain_handler.py  # Ethereum connection
│   └── evidence_logger.py    # Evidence logging
│
├── contracts/
│   ├── EvidenceChain.sol      # Smart contract
│   └── contract_abi.json     # Contract ABI
│
├── forensic_engine/
│   ├── __init__.py
│   ├── orchestrator.py       # Main coordinator
│   ├── disk_forensics.py     # Disk analysis
│   ├── memory_forensics.py   # Memory analysis
│   ├── network_forensics.py  # Network analysis
│   ├── log_forensics.py      # Log analysis
│   └── utils.py              # Helper functions
│
├── llm_engine/
│   ├── __init__.py
│   ├── prompt_templates.py   # AI prompts
│   └── report_generator.py  # AI report generation
│
├── static/
│   ├── css/style.css         # Styling
│   └── js/
│       ├── main.js           # Frontend logic
│       └── web3-integration.js # Blockchain JS
│
└── templates/
    ├── index.html            # Dashboard
    ├── forensics.html        # Results page
    └── report.html           # Report page
```

---

## 🔧 Forensic Modules

### 1. Memory Forensics
- Lists all running processes
- Shows memory usage per process
- Captures system RAM details

### 2. Network Forensics
- Lists all active connections
- Shows local and remote addresses
- Captures network interfaces

### 3. Disk Forensics
- Lists files and directories
- Shows file sizes and timestamps
- Captures disk information

### 4. Log Forensics
- Reads system logs
- Captures authentication logs
- Records system activity

---

## 📋 Prerequisites

### Requirements
- Python 3.8 or higher
- Node.js (for Ganache)
- Git

### Required Accounts
1. **Groq** - Free LLM API
   - Sign up: https://console.groq.com
2. **GitHub** - Code repository

---

## 🚀 Installation

### Step 1 - Clone Repository
```bash
git clone https://github.com/YourUsername/blockchain-forensic-project.git
cd blockchain-forensic-project
```

### Step 2 - Install Python Packages
```bash
pip install -r requirements.txt
```

### Step 3 - Install Ganache
```bash
npm install -g ganache
```

### Step 4 - Create `.env` file
```bash
INVESTIGATOR_ID=Your_Name
ORGANIZATION=Your_Organization
BLOCKCHAIN_URL=http://127.0.0.1:7545
CONTRACT_ADDRESS=0xYourContractAddress
PRIVATE_KEY=0xYourPrivateKey
ACCOUNT_ADDRESS=0xYourAccountAddress
GROQ_API_KEY=your_groq_key
SECRET_KEY=your_secret_key
```

### Step 5 - Deploy Smart Contract
1. Go to https://remix.ethereum.org
2. Create new file: `EvidenceChain.sol`
3. Paste contract code
4. Compile with Solidity 0.8.0
5. Connect to Ganache
6. Click Deploy
7. Copy contract address to `.env`

---

## 🎮 How to Run

### Step 1 - Start Ganache
```bash
ganache --port 7545
```

### Step 2 - Start Application
```bash
python app.py
```

### Step 3 - Open Browser
```
http://localhost:5000
```

---

## 🖥️ How to Use

### Step 1 - Collect Evidence
- Select forensic types (Memory, Network, Disk, Log)
- Click **Run Forensics** button
- Wait for evidence collection
- SHA-256 hash is generated automatically

### Step 2 - Register on Blockchain
- Click **Register Evidence** button
- Evidence hash is stored on Ethereum blockchain
- Transaction hash is recorded permanently

### Step 3 - Generate AI Report
- Click **Generate Report** button
- Groq AI writes professional forensic report
- Report saved as JSON and Text files

### Step 4 - Download Report
- Click **Download JSON Report**
- Click **Download Text Report**
- Use for court submission

---

## 🔐 Security

### Evidence Integrity
- ✅ All evidence is hashed (SHA-256)
- ✅ Hashes stored on blockchain
- ✅ Timestamps are immutable
- ✅ Chain of custody is verifiable

### Important Rules
- ⚠️ NEVER commit `.env` file to Git
- ⚠️ NEVER share your private key
- ⚠️ Use test accounts only for Ganache

---

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python + Flask | Web server and backend |
| Ethereum Blockchain | Permanent evidence storage |
| Solidity Smart Contract | Blockchain logic |
| Ganache | Local blockchain network |
| Web3.py | Python to blockchain connection |
| SHA-256 Hashing | Evidence fingerprinting |
| Groq/Llama AI | Report generation |
| HTML + CSS + JS | Web dashboard |

---

## 👥 Team Members

| Name | Role |
|---|---|
| Member 1 | Project Lead |
| Member 2 | Blockchain Developer |
| Member 3 | Forensics Developer |
| Member 4 | Frontend Developer |

---

## 📊 API Endpoints

| Endpoint | Method | Description |
|---|---|---|
| `/` | GET | Main dashboard |
| `/api/start-forensics` | POST | Run forensics |
| `/api/register-blockchain` | POST | Register on blockchain |
| `/api/generate-report` | POST | Generate AI report |
| `/api/session-status` | GET | Check status |
| `/api/verify-evidence` | POST | Verify evidence |
| `/api/download-report/json` | GET | Download JSON report |
| `/api/download-report/text` | GET | Download text report |

---

## ⚖️ Legal Compliance

### Supported Standards
- IT Act 2000 (India) - Sections 43, 65B
- ISO/IEC 27037 - Digital evidence guidelines
- NIST SP 800-86 - Integration guides

### Evidence Admissibility
- ✅ Hash verification
- ✅ Chain of custody
- ✅ Timestamp verification
- ✅ Investigator identification

---

## 🔮 Future Enhancements

- Mobile app support
- Real-time monitoring
- Multi-investigator support
- Advanced analytics dashboard
- IPFS storage for large evidence files
- Automated alert system

---

## 📝 License

This project is licensed under the GNU General Public License v3.0

---

## ⚖️ Disclaimer

This tool is intended for legitimate forensic investigations and educational purposes only. Users are responsible for ensuring compliance with applicable laws and regulations.

---

**Built with ❤️ for the Cyber Security Community**
```

## Step 3 - Click **Commit Changes** button ✅

---

## ✅ After This Your GitHub Will Show:
```
✅ Beautiful README
✅ Project description
✅ Installation steps
✅ Team members table
✅ Technology stack
✅ API documentation
✅ Security rules
