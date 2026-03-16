// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract EvidenceChain {
    
    struct Evidence {
        string evidenceId;
        string evidenceHash;
        string osSource;
        string forensicType;
        string toolsUsed;
        uint256 timestamp;
        address registeredBy;
        bool exists;
    }
    
    mapping(string => Evidence) private evidenceRegistry;
    string[] private evidenceIds;
    
    event EvidenceRegistered(
        string evidenceId,
        string evidenceHash,
        uint256 timestamp,
        address registeredBy
    );
    
    function registerEvidence(
        string memory _evidenceId,
        string memory _evidenceHash,
        string memory _osSource,
        string memory _forensicType,
        string memory _toolsUsed
    ) public {
        require(!evidenceRegistry[_evidenceId].exists, "Evidence already registered");
        
        evidenceRegistry[_evidenceId] = Evidence({
            evidenceId: _evidenceId,
            evidenceHash: _evidenceHash,
            osSource: _osSource,
            forensicType: _forensicType,
            toolsUsed: _toolsUsed,
            timestamp: block.timestamp,
            registeredBy: msg.sender,
            exists: true
        });
        
        evidenceIds.push(_evidenceId);
        emit EvidenceRegistered(_evidenceId, _evidenceHash, block.timestamp, msg.sender);
    }
    
    function getEvidence(string memory _evidenceId) public view returns (
        string memory, string memory, string memory, uint256, address
    ) {
        require(evidenceRegistry[_evidenceId].exists, "Evidence not found");
        Evidence memory e = evidenceRegistry[_evidenceId];
        return (e.evidenceId, e.evidenceHash, e.osSource, e.timestamp, e.registeredBy);
    }
    
    function verifyHash(string memory _evidenceId, string memory _hash) public view returns (bool) {
        require(evidenceRegistry[_evidenceId].exists, "Evidence not found");
        return keccak256(bytes(evidenceRegistry[_evidenceId].evidenceHash)) == keccak256(bytes(_hash));
    }
    
    function getTotalEvidence() public view returns (uint256) {
        return evidenceIds.length;
    }
}