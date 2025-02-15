from pydantic import UUID4, BaseModel, ConfigDict, Field


class Maintance(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID4 = Field(..., description="Maintance step ID")
    step_name: str = Field(..., description="Maintance step name")
    step_count: int = Field(..., description="Maintance step order")
    description: str = Field(..., description="Maintance step description")
