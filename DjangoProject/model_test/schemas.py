# schemas.py
from pydantic import BaseModel, Field, validator
from ninja import ModelSchema, Schema
from .models import Dataset, Experiment
from .utils import to_camel

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
class ExperimentCreate(Schema):
    name: str
    dataset_id: int
    config: ConfigSchema

    class Config:
        alias_generator = to_camel
        allow_population_by_field_name = True


# 🔹 Experiment 返回体（嵌套 Dataset + Config）
class ExperimentOut(ModelSchema):
    config: ConfigSchema
    dataset: DatasetOut

    class Config:
        model = Experiment
        model_fields = ['id', 'name', 'dataset', 'config', 'created_at']
        alias_generator = to_camel
        allow_population_by_field_name = True
