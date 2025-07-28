from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from app.core.database import Base

class LoanApplication(Base):
    __tablename__ = "loan_applications"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    status = Column(String, default="pending")  
    requested_amount = Column(Float, nullable=False)
    interest_rate = Column(Float, nullable=True)
    credit_score = Column(Float, nullable=True)
    created_at = Column(DateTime, default=datetime.now(timezone.utc))

    # Fully qualified string for lazy resolution
    user = relationship("app.models.user.User", back_populates="applications")
