## MonoPY

[Unofficial] python wrapper for making requests to the [Mono](https://mono.co/) API and a webhook implementation.

Github Link: [monopy](https://github.com/iameo/monopy)

### Features
- Account endpoints [transaction log, statament (json or pdf format)]
- User endpoints [transaction, income and identity]
- Unlink Account
- Misc.



### How to Get Started

You would need to get your mono secret key [here](https://mono.co), and then move to acquire an account ID via the many Mono Connect options.

### Installation & Usage Guide
```
pip install monopy
```

#### SET YOUR KEYS IN YOUR ENVIRONMENT

Open up your CMD (replace ```set``` with ```export``` if you are on MAC/LINUX)

```cmd
set TEST_MONO_SEC_KEY=test_sk_xxxxxxxxxxxxxx
set acc_ID=xxxxxxxxxxxxxxxxx
```

#### #Making Requests


```python
from mono.api import Account, UserMono, Misc, DirectPay
```

### User Client

```python
mono_user = UserMono(mono_sec_key='xxxxxxxxxxxxxxxx')


# Get Transaction logs
mono_user.transaction(id='xxxxxxxxxxx')
```
##### A successful response (status code: 200), otherwise {} (status code: 400)

```json
{
  "paging": {
    "total": 190,
    "page": 2,
    "previous": "https://api.withmono.com/accounts/:id/transactions?page=2",
    "next": "https://api.withmono.com/accounts/:id/transactions?page=3",
  },
  "data": [
    {
      "_id": "xxxxxxxxxxxxxxxxxxxx",
      "amount": 10000,
      "date": "2020-07-21T00:00:00.000Z",
      "narration": "TRANSFER from Emmanuel to Fred",
      "type": "debit",
      "category": "E-CHANNELS",
    },
    ...,
  ]
}
```

##### Get income

```python
mono_user.income(id='xxxxxxxxxxxx')
```



### Account

```python
py_acc = Account(mono_sec_key='xxxxxxxxxxxxxxxx')

# this represents the account details with the financial institution.
py_acc.information(id='xxxxxxxxxx')
```

##### A successful response (status code: 200), otherwise {} (status code: 400)

```json
{
    "meta": {
        "data_status": "AVAILABLE", 
        "auth_method": "mobile_banking" 
    },
    "account": {
        "_id": "5feec8ce95e8dc6axxxxxx",
        "institution": {
            "name": "GTBank",
            "bankCode": "058",
            "type": "PERSONAL_BANKING"
        },....}
}
```

### Misc

#### Get all institutions currently available on Mono

```python
misc = Misc(mono_sec_key='xxxxxxxxxxxxxxx)


misc.institutions()
```

#### A successful reponse is as follow (truncated here)


```python
[
    {'name': 'Brass', 'icon': 'https://mono-public-bucket.s3.eu-west-2.amazonaws.com/images/brass_logo.jpeg', 'coverage': {'countries': ['NG'], 'business': True, 'personal': False}, 'products': ['Auth', 'Accounts', 'Transactions', 'Balance', 'Income', 'Identity'], 'website': None}, {'name': 'Ecobank', 'icon': 'https://mono-public-bucket.s3.eu-west-2.amazonaws.com/images/ecobank-icon.png', 'coverage': {'countries': ['NG'], 'business': False, 'personal': True}, 'products': ['Auth', 'Accounts', 'Transactions', 'Balance', 'Income', 'Identity'], 'website': None},
    .....
    {'name': 'Cowrywise', 'icon': 'https://mono-public-bucket.s3.eu-west-2.amazonaws.com/images/cowrywise-icon.png', 'coverage': {'countries': ['NG'], 'business': False, 'personal': True}, 'products': ['Auth', 'Accounts', 'Transactions', 'Balance', 'Income', 'Identity'], 'website': 'https://cowrywise.com'},
    {'name': 'Polaris Bank', 'icon': 'https://mono-public-bucket.s3.eu-west-2.amazonaws.com/images/polaris-bank-icon.png', 'coverage': {'countries': ['NG'], 'business': False, 'personal': True}, 'products': ['Auth', 'Accounts', 'Transactions', 'Balance', 'Income', 'Identity'], 'website': 'https://www.polarisbanklimited.com'}
]
```


### Contribution

Kindly adhere to the following rules:
- fork the repo
- make your changes on a descriptive branch name
- ....and make a pull request ONLY when your tests pass.


#### Author
- [Emmanuel Okwudike](https://twitter.com/__iameo__)



