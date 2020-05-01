pragma solidity ^0.5.0;

contract Credentials {
    // mapping from address to college name
    mapping(bytes32 => address) private institutes;
    // mapping from college+batchPeriod to merkle root
    mapping(bytes32 => bytes32) private batchMerkleRoots;

    // helper hash function - 1 param
    function hash(string memory _str) private pure returns(bytes32) {
        return  keccak256(abi.encode(_str));
    }
    // helper hash function - 2 params
    function hash(string memory _str1, string memory _str2) private pure returns(bytes32) {
        return  keccak256(abi.encode(_str1, _str2));
    }

    // register new institute
    function registerInstitute(string memory _instituteName) public {
        institutes[hash(_instituteName)] = msg.sender;
    }

    // add root for institute+batch
    function addBatchMerkleRoot(string memory _instituteName, string memory _batchPeriod, string memory _merkleRoot) public {
        require(institutes[ hash(_instituteName)] == msg.sender);
        batchMerkleRoots[hash(_instituteName, _batchPeriod)] = hash(_merkleRoot);
    }

    // verify root for institute+batch
    function verifyBatchMerkleRoot(string memory _instituteName, string memory _batchPeriod, string memory _merkleRoot) public view returns(bool) {
        return (batchMerkleRoots[hash(_instituteName, _batchPeriod)] == hash(_merkleRoot));
    }
}