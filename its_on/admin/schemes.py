from __future__ import annotations

import typing
from marshmallow import Schema, fields


class SplitList(fields.List):
    def deserialize(
        self,
        value: typing.Any,
        attr: str = None,
        data: typing.Mapping[str, typing.Any] = None,
        **kwargs: typing.Any,
    ) -> typing.List[typing.Any]:
        value = value or ''
        values = filter(None, (item.strip() for item in value.split(',')))
        return super().deserialize(values, attr, data, **kwargs)


class BaseSwitchAdminPostRequestSchema(Schema):
    is_active = fields.Boolean()
    version = fields.Int()
    comment = fields.Str()


class SwitchDetailAdminPostRequestSchema(BaseSwitchAdminPostRequestSchema):
    groups = SplitList(fields.Str())


class SwitchAddAdminPostRequestSchema(BaseSwitchAdminPostRequestSchema):
    name = fields.Str()
    groups = SplitList(fields.Str())


class SwitchAddFromAnotherItsOnAdminPostRequestSchema(BaseSwitchAdminPostRequestSchema):
    name = fields.Str()
    groups = fields.List(fields.Str())
    is_hidden = fields.Boolean()


class SwitchCopyFromAnotherItsOnAdminPostRequestSchema(BaseSwitchAdminPostRequestSchema):
    name = fields.Str()
    groups = fields.List(fields.Str())
    is_hidden = fields.Boolean()
    created_at = fields.DateTime(required=False, allow_none=True)


class UserDetailPostRequestSchema(Schema):
    is_superuser = fields.Boolean()
    switch_ids = fields.Integer()
