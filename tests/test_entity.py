from dataclasses import dataclass
from typing import Any

import pytest

from dddentity import Entity, ref


class UserNaive(Entity[int]):
    def __init__(self, id: int, name: str) -> None:
        self.id = id
        self.name = name

    def _ref_(self) -> int:
        return self.id


@dataclass(eq=False)
class UserDataclass(Entity[int]):
    id: int
    name: str

    def _ref_(self) -> int:
        return self.id


@dataclass(eq=False, frozen=True)
class UserDataclassFrozen(Entity[int]):
    id: int
    name: str

    def _ref_(self) -> int:
        return self.id


@pytest.mark.parametrize("User", [UserNaive, UserDataclass, UserDataclassFrozen])
class TestEntity:
    def test_eq(self, User: Any) -> None:
        assert User(1, "A") == User(1, "B")
        assert User(1, "A") != User(2, "A")

    def test_hash(self, User: Any) -> None:
        assert hash(User(1, "A")) == hash(User(1, "B")) == hash(1)
        assert hash(User(1, "A")) != hash(User(2, "A"))

        assert len({User(1, "A"), User(1, "B")}) == 1

    def test_ref(self, User: Any) -> None:
        assert ref(User(1, "A")) == 1
