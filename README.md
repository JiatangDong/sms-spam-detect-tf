# SMS spam detect API using TF-BERT

## Install
```shell
pip install -r requirements.txt
```

## Train/Verify Model

```shell
python model.py <params>
```
`-t` or `--train`: True or False for running model train
`-r` or `--read`: path for data file
`-m` or `--model`: path for model file
`-s` or `--save`: True or False for saving model

## Start Service

```shell
python service.py <params>
```
`-m` or `--model`: path for model file
`-d` or `--debug`: True or False for debug mode


## Test API
POST http://localhost:5000/check_spam

```JSON
[
    "http://paperok.ml - Professional academic help for you!",
    "You know what the warmer weather means...it's burn season! 🔥 Just ask me to roast one of ur friends. I'll take care of the rest 😎",
    "Your package is waiting for delivery. Please confirm the settlement of $19.99 on the following link: http://aka.ms/adfuyiwy",
    "NHS: we have identified that you are eligible to apply for your vaccine. For more information and apply, follow here: application-ukform.com",
    "Hi, Darya. When I test the iOS telemetry today, I found the same issue with \"New Chat Open\" event. I've ready report a bug for that."
]
```
