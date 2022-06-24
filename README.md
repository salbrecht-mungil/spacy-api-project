# Pre-existing knowledge

At the beginning I wasn't familiar with Python beyond a couple of Udemy courses and some small practice tasks in Jupyter Notebook. 

I had no knowledge in dependency handling in Python or which framework to use. I chose Flask since Flask applications are known for being lightweight and it has plenty of documentation in case you run into issues. 

Also, my previous experience with creating and deploying APIs were limited to Mulesoft and working within very confined requirements (most things were set up with matured tooling and configured CICDs). 

I never had to worry about how to package an application and deploy it. So this was a useful exercise for me to learn how to containerise an API using Docker.

I wanted to understand SpaCy a lot more but I tried to stick close to the 1.5 hour mark as suggested in the specification.

This all took considerably longer than I anticipated, but I had to upskill to achieve this and I'm grateful for this opportunity.

# Assumptions

- The user knows the language of the unstructured text ahead of time and passes it along with the actual text in the payload.
- The API should return an error if the language is not supported.  

# Tech stack:

- Python3.8
- pipenv for dependencies
- Flask for the API using gunicorn
- Docker for containerisation
- SpaCy for natural language processing
- DE and EN language models for SpaCy

# Instructions for running the API

First you need to navigate to the main folder: `cd spacy_api`

## With Docker installed run the following commands:
- To build API: `docker build -t spacy_api .`
- To run API: `docker run --env PORT=5000 -p 5000:5000 spacy_api`

Now you can access the API on localhost:5000. The Dockerfile respects the PORT env variable so feel free to adjust if required. You will need to update the port binding.

## Without Docker run the following commands:
You will need to have Python3.8 installed along with pip. Run the following:
- Install pipenv for dependencies: `pip install pipenv`
- Install the required dependencies: `pipenv install`
- Run the API: `./bootstrap.sh`

You can now access the API on localhost:5000

## Postman file for example requests
Hopefully this all works nicely for you too. Inside the postman file you will find three requests: 
- en and de which are supported languages
- unsupported language

## Ideas for improvements
- Add payload validation to verify language is present in the right format and not null.
- Add more details to error handling, e.g. if payload is not sent in correct format then return more meaningful error than 500.
- Try and understand spacy's natural language processing to return more meaingful responses
- Abstract logic to call SpaCy to its own class and think about normalising output.  
- Add more language packages and think about how a key:value / Dictionary can be used instead of endless if elif else statements.  
- Add language detection (experimental, requires investigation) - currently the language of the input text is not being recognised. By adding spacy-langdetect the input text can be verified before entities are being extracted (https://spacy.io/universe/project/spacy-langdetect).
- Add unit tests and e2e tests to ensure the API can cope with the following cases:
    - Valid language input with no text
    - Valid language with various input texts (matching against expected output)
    - Invalid language and expecting 422 error
- Consider handling multiple content types (e.g. xml) rather than just json.
- Deploy the API to Google Cloud Run.

## Interesting parts
- I found the dependency management quite interesting as I never had to consider this before.
- Flask is very lightweight for creating RESTful APIs.

# Breakdown of time used
- Setting up laptop (code editor, Postman etc) and upskilling in Python including writing small test application: approx. 4 hours
- Writing spacy_api: approx. 2 hours
- Reaing up on and adding error handling: 45 min
- Reading about and setting up Docker for containerisation: 4.5 hours

# Useful links for upskilling as part of this task
- https://auth0.com/blog/developing-restful-apis-with-python-and-flask/
- https://towardsdatascience.com/the-right-way-to-build-an-api-with-python-cd08ab285f8f
- https://docs.docker.com/engine/reference/commandline/run/
- https://cloud.google.com/run/docs/quickstarts/build-and-deploy/deploy-python-service