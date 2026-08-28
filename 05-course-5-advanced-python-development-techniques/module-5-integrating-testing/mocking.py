"""CSV Data Processing Utility Module.

This script demonstrates Python best practices including modular design,
type hinting, PEP 8 standards, and exception handling within a single file.
"""

from typing import Dict, List, Optional
import csv
import logging

# Logging configuration
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


class DataProcessor:
    """Class to parse and extract information from structured data files."""

    def __init__(self, filepath: str) -> None:
        """Initializes the DataProcessor with a file path.

        Args:
            filepath (str): Path to the target CSV file.
        """
        self.filepath: str = filepath
        self.records: List[Dict[str, str]] = []

    def load_data(self) -> bool:
        """Loads data from the CSV file into memory.

        Returns:
            bool: True if loading succeeded, False otherwise.
        """
        try:
            with open(self.filepath, mode="r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                self.records = [row for row in reader]
            logging.info(f"Successfully loaded {len(self.records)} records.")
            return True
        except FileNotFoundError:
            logging.error(f"Error: File '{self.filepath}' was not found.")
            return False
        except Exception as err:
            logging.error(f"An unexpected error occurred: {err}")
            return False

    def filter_by_key(self, key: str, value: str) -> List[Dict[str, str]]:
        """Filters stored records matching a key-value pair.

        Args:
            key (str): Column name to filter on.
            value (str): Matching value required.

        Returns:
            List[Dict[str, str]]: Filtered record items.
        """
        return [
            item for item in self.records if item.get(key, "").lower() == value.lower()
        ]


# Execution block for testing or command line execution
if __name__ == "__main__":
    # Sample usage
    processor = DataProcessor("sample.csv")
    if processor.load_data():
        filtered_results = processor.filter_by_key("status", "active")
        print(f"Filtered Count: {len(filtered_results)}")