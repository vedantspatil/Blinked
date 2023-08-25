# BLINKED - BLOCKCHAIN BASED JOB PORTAL
Connecting the world's professionals via a job portal where recruiters meet job applicants whose profiles are backed by a Blockchain ledger. All credentials are validated from the ledger of universities that are operating as half-node, making it impossible for individuals to fake their professional achievements. This is a **full-stack application** where users can perform a range of operations. 


Tech Stack -  Django, Blockchain 

## BLOCKCHAIN 
We used Ganche to simulate the blockchain in our network. Ganache is a personal blockchain for Ethereum development you can use to deploy contracts, develop your applications, and run tests. 
It is available as both a desktop application as well as a command-line tool (formerly known as the TestRPC).

Some important aspects of Ganache Blockchain
### Blockchain Log Output
See the log output of Ganache’s internal blockchain, including responses and other vital debugging information.
### Advanced Mining Controls
Configure advanced mining with a single click, setting block times to best suit your development needs.
### Built-in Block Explorer
Examine all blocks and transactions to gain insight about what’s happening under the hood.
### The Ethereum Blockchain
Byzantium comes standard, giving you the latest Ethereum features needed for modern dapp development.

## ETHEREUM IDE - REMIX
Remix Develops  Smart Contracts for the Ethereum Blockchain. Remix is a Solidity IDE that's used to write, compile and debug Solidity code. 
Solidity is a high-level, contract-oriented programming language for writing smart contracts. It was influenced by popular languages such as C++, Python and JavaScript.

## SYSTEM - ARCHITECHTURE
We discuss the implementation from the point of view of system architecture, database architecture. The system architecture and database architecture show how the system is designed from the engineering point of view.

The system briefly consists of three components in the implementation: 
1. Verification application including federated identity
2. Issuing applications involving multi-signature and BTC-address-based revocation
3. Blockchain and local Database adopted by Databases(IPFS).


<picture>
   <img alt="sysarch" src="https://github.com/vedantspatil/Blinked/assets/37808420/95276ae8-1128-428b-bdde-349ce6bb0547" width="70%" height="70%">
</picture>


## DATABASE - ARCHITECHTURE

The database has been designed to contain two categories of data:
1. The public authentication data and the private certificate data.
2. The public authentication data is available to the public and released to the blockchain; the private certificate data are stored on database where it is securely protected and isolated in the intranet.

<picture>
   <img alt="dbarch" src="https://github.com/vedantspatil/Blinked/assets/37808420/d7b19138-cfef-4858-a37f-e7998c59dab2" width="70%" height="70%">
</picture>

<picture>
   <img alt="dbrtable" src="https://github.com/vedantspatil/Blinked/assets/37808420/1633401a-61b2-4d2f-8ffb-81ebb54d91c8" width="70%" height="70%">
</picture>


## WORKFLOW DIAGRAM
1. Student completes a course and asks issuer for the certificate.
2. Issuer creates a certificate which contains details about the public key of the student, issuer details, course details and then signs the certificate.
3. This certificate is then executed on smart contract which stores it on blockchain and verifies the validity of the certificate.
4. A certificate receipt is sent to the student at the same time who can now use this as a proof of completing the course.
5. Now the person/student can apply for job by sending his certificate receipt, and recruiter can easily verify it through the web application which will call the smart contract.

<picture>
   <img alt="wrkflow" src="https://github.com/vedantspatil/Blinked/assets/37808420/e47e4684-e29a-4389-94eb-5b156a907ea4" width="70%" height="70%">
</picture>

## BLOCKCHAIN VERIFIED ACADEMIC QUALIFICATIONS

Our smart contract:
The important functions are:
1. register institute - An institute can register itself to the blockchain. This is mandatory for an institute and only after this can the institute upload any records.
2. addBatchMerkleRoot - The institute creates a merkle tree of the batch of degrees and then uses this contract call to upload this merkel root on blockchain
3. verifyBatchMerkleRoot - This checks whether given merkle root is same as the one stored onto the blockchain.

## HOW DOES IT WORK
The important aspects of the working are covered in these section. The functionality of the application can be broken down into following aspects.

Issuance of digital certificate from Institute to students:
1. Institute registers itself on the blockchain through the smart contract
2. Institute creates a merkle tree of all the student's degree and uploads the merkel root on the blockchain.
3. Institute issues digital certificate(JSON file) consisting of fields: cpi, name, year, student Id, institution, degree and merkel path(or proof which will be used to verify the legitimacy of the certificate).
Creation of merkle tree helps to reduce the number of transactions, and save space, time and cost.

Verification of the certificate in the portal:
Now in order for a student to claim a degree from this Institute, he should have a json certificate which will be issued by the institution to the students. These certificates, along with the student details, contains a merkel path to a leaf node on the merkel tree. When verified the merkel path with the one uploaded by the Institute, the System determines if the claim of the user is valid.
This is shown by a visual confirmation in the profile page.

1. The user enter the details, and uploads the digital certificate.
2. Using the merkel path in certificate, merkel root is obtained and then verifyBatchMerkelRoot contract call is made.
3. This ensures that certificate is legit, so now comparison of certificate details and form details is done. If all of this are correct, then we add this education with green tick else a red cross.


