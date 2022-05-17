# MIA NLP Challenge
## Compound Nouns
### Installation
To install the required dependencies, run: <br />
`pip install -r requirements.txt`
### Usage
To run the application, run: <br />
`uvicorn main:app` <br /><br />
**Note**: The first execution will try to download the model, in case the required model is not present locally.
### Tests
All tests are under the folder **/tests**. In order to run the tests:
* `cd /tests`
* `pytest` (_to run all the tests_) or
* `pytest <FILE_NAME>` (_to run each test separately_)
