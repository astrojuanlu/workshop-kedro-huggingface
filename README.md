# Who needs ChatGPT? Rock solid AI pipelines with Hugging Face and Kedro

![Powered by Kedro](https://img.shields.io/badge/powered_by-kedro-ffc900?logo=kedro)

Material for the workshop "Who needs ChatGPT? Rock solid AI pipelines with Hugging Face and Kedro".

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/astrojuanlu/workshop-kedro-huggingface/)

![Architecture](./kedro-hf.png)

## Outline

### Kedro as a library: catalog and configuration

```python
from kedro.config import OmegaConfigLoader
from kedro.io import DataCatalog

config_loader = OmegaConfigLoader(".")  # Configuration lives in current directory
print(config_loader["catalog"])  # Catalog configuration gets returned as a dictionary
catalog = DataCatalog.from_config(config_loader["catalog"])

catalog.load("ds_name")  # Loads the dataset corresponding to the `ds_name` entry in `catalog.yml`
```

## Links

- Kedro documentation https://docs.kedro.org/en/0.19.3/
