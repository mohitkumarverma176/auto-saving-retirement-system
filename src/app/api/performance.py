from fastapi import APIRouter
import psutil
import time

router = APIRouter()

@router.get("/performance")
def performance():
    return {
        "time": time.strftime("%H:%M:%S"),
        "memory": f"{psutil.Process().memory_info().rss / 1024 / 1024:.2f} MB",
        "threads": psutil.Process().num_threads()
    }