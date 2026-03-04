from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any

class StorageSpec(BaseModel):
    type: str = Field(..., description="block|file|object")
    performance_tier: str = Field(..., description="hot|warm|cold")
    capacity_tb: int
    replication: int = 2
    protocol: str = "NFS"

class Retention(BaseModel):
    years: Optional[int] = None

class Tiering(BaseModel):
    archive_after_days: Optional[int] = None
    delete_after_days: Optional[int] = None

class Intent(BaseModel):
    tenant: str
    workload: str
    criticality: str = "MEDIUM"
    storage: StorageSpec
    dependencies: List[str] = []
    retention: Optional[Retention] = None
    tiering: Optional[Tiering] = None
    extra: Dict[str, Any] = {}
