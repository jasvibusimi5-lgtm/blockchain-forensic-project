def get_forensic_report_prompt(evidence_data, blockchain_data):
    return f"""
    You are a professional cyber forensics analyst. Based on the following digital evidence data and blockchain registration details, write a formal forensic investigation report.
    
    Evidence Data Summary:
    {str(evidence_data)[:3000]}
    
    Blockchain Registration:
    Transaction Hash: {blockchain_data.get('transaction_hash', 'N/A')}
    Block Number: {blockchain_data.get('block_number', 'N/A')}
    
    Write a professional report with these sections:
    1. Executive Summary
    2. Evidence Collection Details
    3. Memory Analysis Findings
    4. Network Analysis Findings
    5. Disk Analysis Findings
    6. Blockchain Integrity Verification
    7. Conclusions and Recommendations
    
    Keep it formal and factual.
    """