# Hungry Girlfriend Application

I have a girlfriend who happens to get very hangry when not fed. I keep forgetting when I last fed her, and more importantly, when I need to feed her next. I have a one-time script called feed-girlfriend.sh that triggers when I feed my girlfriend, and I have written a script called monitor-hunger.sh that will send a POST request to `http://localhost:8000/monitor` every 5 seconds and warn me when her status changes to "Hungry", but I can't seem to figure out the business logic for determining when she will be hungry.

For 2 minutes after I feed her, she has a status of "Full"

For 1 more minute (2 minutes - 3 minutes) she has a status of "Neutral"

For 30 more seconds, she has a status of "Hungry"

If these 30 seconds expire and she hasn't been fed, the program should throw a "NotFedException" and return an internal status code with the optional message of "Hangry"

all status messages should be json formatted with a key of "status". For example:

```
{
    "status": "Full"
}
```

My girlfriend would also freak out if the code is messy, so test cases should be written first. I will provide an example of this in the git log - tagged with intial, tests, and logic.

## Initialize

1. use venv to isolate your code. create virtual environment with `python3 -m venv venv` and use virtual environment with `source venv/bin/activate`

2. install requirements with `pip install -r requirements.txt`

## Execute

1. Ensure virtual environment is active, if not run `source venv/bin/activate`

2. Ensure pip packages are up to date. run `pip install -r requirements.txt`

3. run `python main.py`

## Unit Testing

1. run `python -m pytest tests/`

2. ensure all unit tests pass. Fix any unit tests or code that was broken by you.
