import logging

# Configure logging
logging.basicConfig(filename='healthcare_app.log', level=logging.INFO, 
                    format='%(asctime)s:%(levelname)s:%(message)s')

def log_access(user):
    logging.info(f"User {user} accessed the system")

# Example usage
log_access("doctor")
