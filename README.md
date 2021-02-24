# Install requirements
* Navigate to the highest directory in the terminal (path ends /mini-project-tests)
* (Ideally you'd create and activate a virtual environment, then run the pip install command given below, so the requirements aren't installed globally)
* Run the below command 
```py
pip install -r requirements.txt
```
* This should have installed pytest and its dependencies so you're able to run the test suite

# Run tests
To run the tests, follow the below steps
* Navigate in your terminal so your `pwd` path ends with
```bash
 /mini-project-tests
 ```
* Run the below command in your terminal
* NB: you may need to substitute `python` and `pytest` depending on your local setup
```py
python -m pytest tests/tests.py
```
* Tip: run the below command for a more verbose test output
```py
python -m pytest tests/tests.py -v
```

# Run the code
* In the same directory (path ends /mini-project-tests)
* Run the below command in the terminal
* NB: you may need to substitute `python` depending on your local setup
```py
python -m src.products
```
* You should see three green dots - for the three passing tests!