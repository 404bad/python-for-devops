# Docker health check scripts

import subprocess
import logging

logging.basicConfig(level=logging.INFO)

try:
    result = subprocess.run (
        ["docker","ps"],
        check=True,
        text=True,
        capture_output=True
    )

    logging.info(result.stdout)
except FileNotFoundError:
    logging.error("Docker not installed.")

except subprocess.calledProcessError as e:
    logging.error("command failed: {e}")

finally:
    logging.info("Scipt finished.")
