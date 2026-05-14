import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


class Calculadora():
    def soma(self, a: float, b: float) -> float:
        logging.info("Soma executada")
        return a + b
