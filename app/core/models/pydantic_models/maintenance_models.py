from pydantic import BaseModel, ConfigDict, Field


class Maintance(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    step_name: str = Field(..., description="Maintance step name")
    step_count: int = Field(..., description="Maintance step order")
    description: str = Field(..., description="Maintance step description")
