"""
_summary_
"""
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


class Calculator:
    def sum(self, a: float, b: float) -> float:
        logging.info("Error")
        return a + b
