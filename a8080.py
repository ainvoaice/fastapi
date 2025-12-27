# run.py or a8080.py
import uvicorn
from app.main import create_app
from app.config import Settings

# Load settings
settings = Settings()

# Create app
app = create_app(settings)

if __name__ == "__main__":
    uvicorn.run(
        "a8080:app",
        host="0.0.0.0",
        port=8080,
        reload=True,
        log_level="info"
    )