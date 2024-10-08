import logging
import os
from datetime import datetime

# Create logs directory if not created
if not os.path.exists("logs"):
    os.makedirs("logs")

# Creates filename based on timestamp
log_filename = os.path.join("logs", datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".log")

# Configures logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_filename),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger()

# Outputs log messages to console and log file
def log_info(message):
    logger.info(message)

def save_plot(plt, log_filename):
    # Saves the plot as a PNG file with the same name as the log file
    plot_filename = log_filename.replace('.log', '.png')
    plt.savefig(plot_filename)
    logger.info(f"Saved plot as {plot_filename}")
