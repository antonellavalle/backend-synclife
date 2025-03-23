from sqlmodel import Field, SQLModel


class SQLModelNoteTagModel(SQLModel, table=True):
    __tablename__ = "note_tag"

    note_uuid: str = Field(foreign_key="note.uuid", primary_key=True)
    tag_uuid: str = Field(foreign_key="tag.uuid", primary_key=True)
