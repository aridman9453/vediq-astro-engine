from datetime import datetime


def get_current_transits():

    return {
        "generated_at": str(datetime.utcnow()),
        "status": "Transit module ready"
    }
