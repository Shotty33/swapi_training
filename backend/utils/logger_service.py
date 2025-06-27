from datetime import datetime

class LoggerService:
    def log_request(self, method: str, url: str, status_code: int):
        print(f"[{datetime.now()}] {method} {url} → {status_code}")
