import typing as t
import polars as pl
from kedro.io import AbstractDataset


class DeltaPolarsDataset(AbstractDataset):
    def __init__(
        self,
        filepath,
        load_args: dict[str, t.Any] | None = None,
        save_args: dict[str, t.Any] | None = None,
        credentials: dict[str, t.Any] | None = None,
        storage_options: dict[str, t.Any] | None = None,
    ):
        self._filepath = filepath
        self._load_args = load_args or {}
        self._save_args = save_args or {}
        self._credentials = credentials or {}
        self._storage_options = storage_options or {}

        self._storage_options.update(self._credentials)

    def _load(self) -> pl.DataFrame:
        return pl.read_delta(
            self._filepath, storage_options=self._storage_options, **self._load_args
        )

    def _save(self, data: pl.DataFrame) -> None:
        data.write_delta(
            self._filepath,
            storage_options=self._storage_options,
            **self._save_args,
        )

    def _describe(self) -> dict[str, t.Any]:
        return dict(
            filepath=self._filepath,
            load_args=self._load_args,
            save_args=self._save_args,
            storage_options=self._storage_options,
        )
