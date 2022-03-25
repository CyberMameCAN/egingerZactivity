from typing import Optional
from pydantic import BaseModel, Field

class TaskBase(BaseModel): # FastAPIのスキーマモデルから継承
    title: Optional[str] = Field(None, example="クリーニングを取りに行く")

class TaskCreate(TaskBase):
    pass

class TaskCreateResponse(TaskCreate):
    id: int

    class Config:
        orm_mode = True
    
class Task(TaskBase):
    id: int
    #title: Optional[str] = Field(None, example="クリーニングを取りに行く")
    done: bool = Field(False, description="完了フラグ")

    class Config:
        orm_mode = True

# 「型ヒント」というらしい、Pythonは動的型付け言語
