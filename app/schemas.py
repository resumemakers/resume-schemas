from marshmallow import Schema, fields


class Education(Schema):
    institution = fields.Str(required=True)
    inicial_data = fields.Date(required=True)
    finished_data = fields.Date()
    comments = fields.Str()


class Experience(Schema):
    institution = fields.Str(required=True)
    inicial_data = fields.Date(required=True)
    finished_data = fields.Date()
    comments = fields.Str()


class Skills(Schema):
    skill = fields.Str(required=True)
    level = fields.Str(required=True)


class Languages(Schema):
    languages = fields.Str(required=True)
    level = fields.Str(required=True)


class SimpleResumeSchema(Schema):
    name = fields.Str(required=True)
    profession = fields.Str(required=True)
    phone = fields.Str(required=True)
    email = fields.Email(required=True)
    address = fields.Str(required=True)
    portfolio = fields.Str(required=True)
    languages = fields.Nested(Languages(), many=True)
    skills = fields.Nested(Skills(), many=True)
    experience = fields.Nested(Experience(), many=True)
    education = fields.Nested(Education(), many=True)
