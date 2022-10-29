# BasicBlockchain
Implementation of a blockchain in Python &amp; Flask

## Starting the project (Docker required)

 1. Clone the repository
 2. CD to the repository folder
 3. Call "docker-compose up" to start the dockerized project
 4. Flask server is started on localhost, port 5000 (http://127.0.0.1:5000)
 
## Blockain REST API functions

### /mine_block
- Mine a new block and add it to the end of the blockchain
  
### /get_chain
- Return current blockchain
  
### /complexity
- Get current complexity (number of leading zeros)
  
### /complexity/<int:leading_zeros>
- Set complexity (number of leading zeros)
  
### /validate
- Validate blockchain and return true if the chain is valid
