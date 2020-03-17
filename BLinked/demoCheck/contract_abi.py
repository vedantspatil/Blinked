abi = """
[
	{
		"constant": false,
		"inputs": [
			{
				"name": "_instituteName",
				"type": "string"
			},
			{
				"name": "_batchPeriod",
				"type": "string"
			},
			{
				"name": "_merkleRoot",
				"type": "string"
			}
		],
		"name": "addBatchMerkleRoot",
		"outputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [
			{
				"name": "_instituteName",
				"type": "string"
			}
		],
		"name": "registerInstitute",
		"outputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [
			{
				"name": "_instituteName",
				"type": "string"
			},
			{
				"name": "_batchPeriod",
				"type": "string"
			},
			{
				"name": "_merkleRoot",
				"type": "string"
			}
		],
		"name": "verifyBatchMerkleRoot",
		"outputs": [
			{
				"name": "",
				"type": "bool"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	}
]
"""
