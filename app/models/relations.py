from app import db

user_roles = db.Table(
    "user_roles",
    db.Column("User_id", db.Integer, db.ForeignKey("User.id"), primary_key=True),
    db.Column("roles_id", db.Integer, db.ForeignKey("roles.id"), primary_key=True),
)
