import csv
from pathlib import Path
from typing import List, Dict


class TestDataManager:
    """
    Utility class to manage test data from CSV files.
    Provides methods to load and retrieve test data.
    """

    @staticmethod
    def load_test_data(file_path: str = "data/test_profiles.csv") -> List[Dict]:
        """
        Load test data from CSV file.

        Args:
            file_path: Path to the CSV file containing test data

        Returns:
            List of dictionaries containing test data
        """
        test_data = []
        csv_path = Path(file_path)

        if not csv_path.exists():
            raise FileNotFoundError(f"Test data file not found: {file_path}")

        try:
            with open(csv_path, 'r', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    test_data.append(row)
            return test_data
        except Exception as e:
            raise Exception(f"Error reading test data file: {str(e)}")

    @staticmethod
    def get_test_user(index: int = 0) -> Dict:
        """
        Get a specific test user by index.

        Args:
            index: Index of the test user (0-based)

        Returns:
            Dictionary containing test user data
        """
        test_data = TestDataManager.load_test_data()
        if index >= len(test_data):
            raise IndexError(f"Test user index {index} not found. Available: {len(test_data)}")
        return test_data[index]

    @staticmethod
    def get_all_test_users() -> List[Dict]:
        """
        Get all test users.

        Returns:
            List of all test user dictionaries
        """
        return TestDataManager.load_test_data()

