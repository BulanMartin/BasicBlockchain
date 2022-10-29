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

JSON response example
```json
{"Blockchain":"New block was mined!",
"current_complexity":5,
"index":6,
"nonce":1050773,
"previous_hash":"00000f12566ad5c62ca38aaf7214da3eea7afa6b99cc6596801fa66b7e21b6ab",
"timestamp":"2022-10-29 10:19:42.211427"}
```
  
### /get_chain
- Return current blockchain

JSON response example
```json
{"chain":[
 {"current_complexity":4,
  "index":1,
  "nonce":1,
  "prev_hash":"0",
  "timestamp":"2022-10-29 09:44:52.155196"
  },
  {"current_complexity":4,
  "index":2,
  "nonce":19135,
  "prev_hash":"000033ae00581b947e8a8ff405e89aea47024b2a0faaebcce759f6ef6eaf4d4c",
  "timestamp":"2022-10-29 09:44:57.636357"
  },
  {"current_complexity":4,
  "index":3,
  "nonce":460,
  "prev_hash":"0000ba0c85d2c476a4bab40cfc0769fde770fdaee65d278465bdada37905f951",
  "timestamp":"2022-10-29 10:08:13.049064"}
  ],
  "length":3}
```
  
### /complexity
- Get current complexity (number of leading zeros)

JSON response example
```json
{"Current number of leading zeros ":4}
```
  
### /complexity/<int:leading_zeros>
- Set complexity (number of leading zeros)

JSON response example
```json
{"Leading zeros set to ":5}
```
  
### /validate
- Validate blockchain and return true if the chain is valid

JSON response example
```json
{"Chain valid":true}
```
