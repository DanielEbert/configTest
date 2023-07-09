from __future__ import annotations

from typing import Any


class Config:
    repository_root_path: str

    def __init__(self):
        self.config = {}

    def add(self, key: str, value: Any) -> None:
        self.config[key] = value

    def __getattr__(self, name: str) -> Any:
        if name not in self.config:
            raise AttributeError(f'Settings object has no attribute {name}')
        return self.config[name]

    def __repr__(self) -> str:
        return 'Config:\n' + '\n'.join([f'    {key}: {value}' for (key, value) in self.config.items()])

    def __str__(self) -> str:
        return str(self.config)


settings = Config()
