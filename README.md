# Hikari - OnyxCord Modified Version

> **Fork modificado por Gustavo S.**
> 
> Esta é uma versão modificada do [Hikari](https://github.com/hikari-py/hikari) que preserva tipos de componentes desconhecidos em interações de modais, permitindo suporte aos novos componentes de modais do Discord (tipos 18-23) através do OnyxCord.

## Modificações

### `hikari/impl/entity_factory.py`

Modificado o método `deserialize_component` para preservar tipos de componentes desconhecidos ao invés de registrar e descartá-los:

```python
# ANTES (Hikari original)
else:
    _LOGGER.debug("Unknown component type %s", component_type)
    return None

# DEPOIS (OnyxCord modificado)
else:
    # Preserve unknown components for OnyxCord
    return component_payload
```

Esta modificação permite que o OnyxCord manipule novos tipos de componentes do Discord que ainda não são nativamente suportados pelo Hikari, incluindo:
- Label (tipo 18)
- Separator (tipo 19)
- TextArea (tipo 20)
- MediaGallery (tipo 21)
- Checkbox (tipo 22)
- RadioGroup (tipo 23)

## Instalação

### A partir do Git (Recomendado para OnyxCord)

```bash
pip install git+https://github.com/kruldevb/hikari-master.git
```

### Desenvolvimento Local

```bash
pip install -e .
```

### Versão Original

Para instalar a versão original não modificada:

```bash
pip install -U hikari
```

## Uso

Use esta versão modificada do Hikari em conjunto com o OnyxCord:

```python
from onyxcord.hikari import OnyxBot
from onyxcord.ext.miru import install_modal_handler

bot = OnyxBot(token="YOUR_TOKEN")
install_modal_handler(bot)

bot.run()
```

## Hikari Original

Este fork é baseado no Hikari v2.5.0. Para a versão original não modificada, visite:
- GitHub: https://github.com/hikari-py/hikari
- Documentação: https://docs.hikari-py.dev/

## Licença

Mesma licença do Hikari original - MIT License

---

**Modificado por:** Gustavo S.  
**Versão Base:** Hikari v2.5.0  
**Propósito:** Suporte aos novos componentes de modais do Discord via OnyxCord
