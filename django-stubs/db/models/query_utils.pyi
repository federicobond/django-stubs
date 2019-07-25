from collections import OrderedDict, namedtuple
from typing import Any, Dict, Iterator, List, Optional, Set, Tuple, Type, Union

from django.db.models.base import Model
from django.db.models.expressions import Expression
from django.db.models.fields import Field
from django.db.models.fields.mixins import FieldCacheMixin
from django.db.models.sql.compiler import SQLCompiler
from django.db.models.sql.query import Query
from django.db.models.sql.where import WhereNode
from django.utils import tree

PathInfo = namedtuple("PathInfo", "from_opts to_opts target_fields join_field m2m direct filtered_relation")

class InvalidQuery(Exception): ...

def subclasses(cls: Type[RegisterLookupMixin]) -> Iterator[Type[RegisterLookupMixin]]: ...

class QueryWrapper:
    contains_aggregate: bool = ...
    data: Tuple[str, List[Any]] = ...
    def __init__(self, sql: str, params: List[Any]) -> None: ...
    def as_sql(self, compiler: SQLCompiler = ..., connection: Any = ...) -> Any: ...

class Q(tree.Node):
    children: Union[List[Dict[str, str]], List[Tuple[str, Any]], List[Q]]
    connector: str
    negated: bool
    AND: str = ...
    OR: str = ...
    default: Any = ...
    conditional: bool = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def __or__(self, other: Any) -> Q: ...
    def __and__(self, other: Any) -> Q: ...
    def __invert__(self) -> Q: ...
    def resolve_expression(
        self,
        query: Query = ...,
        allow_joins: bool = ...,
        reuse: Optional[Set[str]] = ...,
        summarize: bool = ...,
        for_save: bool = ...,
    ) -> WhereNode: ...
    def deconstruct(self) -> Tuple[str, Tuple, Dict[str, str]]: ...

class DeferredAttribute:
    field_name: str = ...
    def __init__(self, field_name: str) -> None: ...
    def __get__(self, instance: Optional[Model], cls: Type[Model] = ...) -> Any: ...

class RegisterLookupMixin:
    lookup_name: str
    @classmethod
    def get_lookups(cls) -> Dict[str, Any]: ...
    def get_lookup(self, lookup_name: str) -> Optional[Any]: ...
    def get_transform(self, lookup_name: str) -> Optional[Any]: ...
    @staticmethod
    def merge_dicts(dicts: List[Dict[str, Any]]) -> Dict[str, Any]: ...
    @classmethod
    def register_lookup(cls, lookup: Any, lookup_name: Optional[str] = ...) -> Type[Any]: ...
    @classmethod
    def _unregister_lookup(cls, lookup: Any, lookup_name: Optional[str] = ...): ...

def select_related_descend(
    field: Field,
    restricted: bool,
    requested: Optional[
        Union[Dict[str, Dict[str, Dict[str, Dict[str, Dict[str, Dict[str, Dict[str, Dict[Any, Any]]]]]]]], bool]
    ],
    load_fields: Optional[Set[str]],
    reverse: bool = ...,
) -> bool: ...
def refs_expression(
    lookup_parts: List[str], annotations: OrderedDict
) -> Union[Tuple[bool, Tuple], Tuple[Expression, List[str]]]: ...
def check_rel_lookup_compatibility(model: Type[Model], target_opts: Any, field: FieldCacheMixin) -> bool: ...

class FilteredRelation:
    relation_name: str = ...
    alias: Optional[str] = ...
    condition: Q = ...
    path: List[str] = ...
    def __init__(self, relation_name: str, *, condition: Any = ...) -> None: ...
    def clone(self) -> FilteredRelation: ...
    def resolve_expression(self, *args: Any, **kwargs: Any) -> None: ...
    def as_sql(self, compiler: SQLCompiler, connection: Any) -> Any: ...
