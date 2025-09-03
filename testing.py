import logging
import os
from datetime import datetime

# build log file path
log_folder = 'logs'
os.makedirs(log_folder, exist_ok=True)

# format log file name with current date
datenow = datetime.now().strftime('%Y-%m-%d')
log_filename = f'airflow_log_{datenow}.log'
log_filepath = os.path.join(log_folder, log_filename)

# setup logger
logging.basicConfig(
    filename=log_filepath,
    filemode='a',
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# main function to log a message
def process_data(data):
    logging.info("start processing data")
    if not data:
        logging.warning("no data provided")
        return None

    try:
        result = [d * 2 for d in data]
        logging.info("data processed successfully")
        return result
    except Exception as e:
        logging.error(f"error processing data: {e}")
        return None

# main
if __name__ == "__main__":
    logging.info("script started")
    sample_data = [1, 2, 3, 4, 5]
    processed_data = process_data(sample_data)
    logging.info("script finished")
    
