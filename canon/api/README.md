# canon/api

Command palette and invocation engine for the MIRRORNODE lattice.

## Modules

| File | Purpose |
|---|---|
| `commands.py` | Registry of all callable lattice commands |
| `invoke.py` | Invocation engine — routes commands, returns auditable results |

## Usage

```python
from canon.api.invoke import invoke

result = invoke("preflight")
print(result)
print(result.to_dict())
```

## Extending

Assign a handler to wire a real implementation:

```python
from canon.api.commands import COMMANDS

def my_preflight_handler(**kwargs):
    return {"nodes_checked": 7, "all_healthy": True}

COMMANDS["preflight"].handler = my_preflight_handler
```
