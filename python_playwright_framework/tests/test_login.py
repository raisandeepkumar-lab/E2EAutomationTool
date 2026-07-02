import os
from pathlib import Path

import pytest
from playwright.sync_api import Browser, BrowserContext

from pages.login_page import LinkedInLoginPage


@pytest.fixture(scope="session")
def storage_state_path():
    return Path(__file__).resolve().parent / "login_state.json"


def test_login_and_persist_session(browser: Browser, storage_state_path: Path):
    username = os.getenv("LINKEDIN_USERNAME")
    password = os.getenv("LINKEDIN_PASSWORD")

    if not username or not password:
        pytest.skip("Set LINKEDIN_USERNAME and LINKEDIN_PASSWORD environment variables to run the login test")

    context = browser.new_context()
    page = context.new_page()

    login_page = LinkedInLoginPage(page)
    login_page.open()
    login_page.login(username, password)
    context.storage_state(path=str(storage_state_path))

    assert login_page.is_logged_in() is True
    context.close()


def test_regression_uses_saved_session(browser: Browser, storage_state_path: Path):
    if not storage_state_path.exists():
        pytest.skip("Saved login session not found; run the login test first")

    context = browser.new_context(storage_state=str(storage_state_path))
    page = context.new_page()
    page.goto("https://www.linkedin.com/feed", wait_until="domcontentloaded", timeout=20000)

    assert "/feed" in page.url.lower() or "/in/" in page.url.lower()
    context.close()
