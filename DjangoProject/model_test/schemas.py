# schemas.py
from pydantic import BaseModel, Field, validator, ConfigDict
from ninja import ModelSchema, Schema
from .models import Dataset, Experiment
from .utils import to_camel

from pydantic import BaseModel, Field
from typing import Dict, Any

class CamelModel(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        from_attributes=True,  # 替代 from_orm
        # alias_generator=lambda s: ''.join(
        #     word if i == 0 else word.capitalize()
        #     for i, word in enumerate(s.split('_'))
        # ),
        json_schema_extra={"by_alias": True}  # ✅ 输出用别名
    )

# 🔹 嵌套的 JSON 配置结构
class ConfigSchema(Schema):
    learning_rate: float = Field(..., gt=0, le=1, description="学习率")
    epochs: int = Field(default=10, ge=1, le=1000)
    optimizer: str = Field(default="adam")

    @validator("optimizer")
    def check_optimizer(cls, v):
        if v not in {"adam", "sgd", "rmsprop"}:
            raise ValueError("Invalid optimizer")
        return v


# 🔹 Dataset 展示
class DatasetOut(ModelSchema):
    class Config:
        model = Dataset
        model_fields = ['id', 'name', 'source_url', 'created_at']
        alias_generator = to_camel
        allow_population_by_field_name = True


# 🔹 Experiment 创建请求体


class ExperimentCreate(BaseModel):
    name: str
    dataset_id: int = Field(alias='datasetId')
    config: Dict[str, Any]

    class Config:
        allow_population_by_field_name = True  # 支持通过字段名和别名传参
        populate_by_name = True                # pydantic v2 支持
        by_alias = True
        alias_generator = lambda s: ''.join(
            word if i == 0 else word.capitalize()
            for i, word in enumerate(s.split('_'))
        )  # 自动将 snake_case 转 camelCase



class ExperimentOut(BaseModel):
    id: int
    name: str
    dataset_id: int = Field(alias='aawa')
    config: Dict[str, Any]

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        populate_by_name = True                # pydantic v2 支持
        by_alias = True
        # alias_generator = lambda s: ''.join(
        #     word if i == 0 else word.capitalize()
        #     for i, word in enumerate(s.split('_'))
        # )

