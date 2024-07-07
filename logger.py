import logging
import os
from datetime import datetime

# Create logs directory if it doesn't exist
if not os.path.exists("logs"):
    os.makedirs("logs")

# Generate a log file name based on the current date and time
log_filename = os.path.join("logs", datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".log")

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_filename),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger()

def log_info(message):
    logger.info(message)

def save_plot(plt, log_filename):
    plot_filename = log_filename.replace('.log', '.png')
    plt.savefig(plot_filename)
    logger.info(f"Saved plot as {plot_filename}")
