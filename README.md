# Hikari - OnyxCord Modified Version

This is a modified version of [Hikari](https://github.com/hikari-py/hikari) that preserves unknown component types in modal interactions, enabling support for Discord's new modal components (types 18-23) through OnyxCord.

## Modifications

### `hikari/impl/entity_factory.py`

Modified the `deserialize_component` method to preserve unknown component types instead of logging and discarding them:

```python
# BEFORE (original Hikari)
else:
    _LOGGER.debug("Unknown component type %s", component_type)
    return None

# AFTER (OnyxCord modified)
else:
    # Preserve unknown components for OnyxCord
    return component_payload
```

This allows OnyxCord to handle new Discord component types that aren't yet natively supported by Hikari.

## Installation

### From Git (Recommended for OnyxCord)

```bash
pip install git+https://github.com/YOUR_USERNAME/hikari-onyxcord.git
```

### Local Development

```bash
pip install -e .
```

## Usage

Use this modified Hikari version together with OnyxCord:

```python
from onyxcord.hikari import OnyxBot
from onyxcord.ext.miru import install_modal_handler

bot = OnyxBot(token="YOUR_TOKEN")
install_modal_handler(bot)

bot.run()
```

## Original Hikari

This is based on Hikari v2.5.0. For the original, unmodified version, visit:
- GitHub: https://github.com/hikari-py/hikari
- Documentation: https://docs.hikari-py.dev/

## License

Same as original Hikari - MIT License
