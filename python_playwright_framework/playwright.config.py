from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
TEST_RESULTS_DIR = BASE_DIR / "test-results"
REPORTS_DIR = BASE_DIR / "playwright-report"
DEFAULT_TIMEOUT = 30000
HEADLESS = True
