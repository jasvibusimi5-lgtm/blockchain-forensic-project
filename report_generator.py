import os
import json
from datetime import datetime
from config import Config
from .prompt_templates import get_forensic_report_prompt

class ReportGenerator:
    def __init__(self):
        self.groq_api_key = os.getenv('GROQ_API_KEY', '')
        self.openai_api_key = Config.OPENAI_API_KEY

    def generate_comprehensive_report(self, evidence_data, blockchain_data):
        prompt = get_forensic_report_prompt(evidence_data, blockchain_data)
        report_text = None

        # Try Groq first (FREE!)
        if self.groq_api_key:
            try:
                from groq import Groq
                client = Groq(api_key=self.groq_api_key)
                response = client.chat.completions.create(
                    model="llama3-8b-8192",
                    messages=[
                        {
                            "role": "system",
                            "content": "You are a senior digital forensics analyst."
                        },
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ],
                    max_tokens=2000
                )
                report_text = response.choices[0].message.content
                print("[+] Report generated using Groq!")
            except Exception as e:
                print(f"[!] Groq failed: {e}")

        # Try OpenAI if Groq fails
        if not report_text and self.openai_api_key:
            try:
                import openai
                client = openai.OpenAI(api_key=self.openai_api_key)
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {
                            "role": "system",
                            "content": "You are a senior digital forensics analyst."
                        },
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ],
                    max_tokens=2000
                )
                report_text = response.choices[0].message.content
                print("[+] Report generated using OpenAI!")
            except Exception as e:
                print(f"[!] OpenAI failed: {e}")

        # Use basic report if both fail
        if not report_text:
            report_text = self._generate_basic_report(
                evidence_data,
                blockchain_data
            )
            print("[+] Basic report generated!")

        return {
            'report_text': report_text,
            'generated_at': datetime.now().isoformat(),
            'session_id': evidence_data.get('session_id'),
            'blockchain_tx': blockchain_data.get('transaction_hash')
        }

    def _generate_basic_report(self, evidence_data, blockchain_data):
        return f"""
CYBER FORENSIC INVESTIGATION REPORT
=====================================
Generated: {datetime.now().isoformat()}
Session ID: {evidence_data.get('session_id', 'N/A')}

EXECUTIVE SUMMARY
-----------------
Digital forensic investigation conducted successfully.

BLOCKCHAIN VERIFICATION
------------------------
Transaction Hash: {blockchain_data.get('transaction_hash', 'N/A')}
Block Number: {blockchain_data.get('block_number', 'N/A')}
Status: Evidence Successfully Registered on Blockchain ✅

EVIDENCE COLLECTED
------------------
Forensic Types: {list(evidence_data.get('forensics', {}).keys())}
Timestamp: {evidence_data.get('timestamp', 'N/A')}

CONCLUSION
----------
All evidence collected and registered on blockchain
for integrity verification.
        """

    def save_report(self, report, session_dir):
        json_path = os.path.join(session_dir, 'forensic_report.json')
        txt_path = os.path.join(session_dir, 'forensic_report.txt')

        with open(json_path, 'w') as f:
            json.dump(report, f, indent=2)

        with open(txt_path, 'w') as f:
            f.write(report['report_text'])

        return {
            'json_report': json_path,
            'text_report': txt_path
        }