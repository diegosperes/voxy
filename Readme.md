# Voxy Challenge

Voxy is a python solution for the word counter challenge.


### Setup / Running the application

The Dockerfile will consist of two stages: "prod" and "dev". The "prod" stage will be the image used in production, while the "dev" stage will extend "prod" by installing the development requirements to facilitate running tests.
Pipenv was chosen to ensure consistency across multiple environments.

```console
~$ docker-compose up
```

After the initialization of docker container open your browser and type `localhost:8000/words` 

### Tests

Tests run inside docker container using the following command.

```console
~$ docker-compose up tests
```

### Functional Requirements

As a user when I view the application then I see a form containing a text box to enter a body of text and when I submit the form with some text then I see a result containing the number of words in the text box
and when I submit the form with an empty text then I see a form error telling me that some text input is required.

As an engineer when I look at your project then I should understand how to install and run it.

As a system tests must cover critical user cases.

As a system word counter implementation must support English language.

As a system word counter implementation must not count special character, numbers and unicode symbols as a word.

As a system word counter implementation must count word ending with punctuation as valid word.

As a system word counter implementation must count word between double-quote, grave, and rounded parentheses as valid word.

As a system word counter implementation must count word contraction as single word.

As a user when the outcome of words returns I see the same text submited highlighting the valid words.