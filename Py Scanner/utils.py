import datetime

def log_event(event, level="INFO"):
    with open("scanner.log", "a", encoding="utf-8") as log_file:
        log_file.write(f"{datetime.datetime.now()} [{level}]: {event}\n")
