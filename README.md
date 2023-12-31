# Operator

This python package is the designated python client to [Agent Smith](https://github.com/agentsofthesystem/agent-smith).

## Requirements

- Python 3.11+ is recommended.

## Usage

Create a python virtual environment & install the client.

On Linux:

```
python -m venv venv
. ./venv/bin/activate
pip install git+https://github.com/agentsofthesystem/operator
```

On Windows:
```
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install git+https://github.com/agentsofthesystem/operator
```

Please note: if a targeted version is required, then used the at symbol to specify branch, tag, etc..

Eg, for the latest main branch:
```
pip install git+https://github.com/agentsofthesystem/operator@main
```

## Example

To use in source code:

```
from operator_client import Operator

hostname = "http://127.0.0.1"
port = "3000"

operator = Operator(hostname, port=port, verbose=True)

games = operator.game.get_games()
```
