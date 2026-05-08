from pydantic import BaseModel
from typing import Optional


class MarketSignal(BaseModel):
    symbol: str
    trend: str
    confidence: float
    sma_signal: str
    ema_signal: str
    volatility: float
    volume_spike: bool


class SentimentReport(BaseModel):
    symbol: str
    sentiment: str
    risk_level: str
    summary: str


class TradeDecision(BaseModel):
    symbol: str
    action: str
    reason: str
    quantity: int
    stop_loss: Optional[float]
    target: Optional[float]
    approved_by_guardian: bool
