import logging 

logging.basicConfig(
    filename= "engine.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

def log(message):
    logging.info(message)

