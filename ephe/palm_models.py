from pydantic import BaseModel
from typing import Optional, Dict, Any
from datetime import datetime


class PalmUploadRequest(BaseModel):
    user_id: str
    hand_type: str  # left or right


class PalmAnalyzeRequest(BaseModel):
    user_id: str
    image_url: str
    birth_chart_id: Optional[str] = None


class PalmReportResponse(BaseModel):
    success: bool
    report_id: str
    image_url: str
    analysis: Dict[str, Any]
    final_report: Dict[str, Any]
    created_at: datetime


class PalmHistoryItem(BaseModel):
    report_id: str
    created_at: datetime
    image_url: str


class PalmHistoryResponse(BaseModel):
    success: bool
    reports: list[PalmHistoryItem]
