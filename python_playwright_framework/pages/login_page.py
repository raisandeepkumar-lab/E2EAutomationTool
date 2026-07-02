import os
from playwright.sync_api import Locator, Page


class LinkedInLoginPage:
    URL = "https://www.linkedin.com/"
    USERNAME_SELECTORS = [
        "input[name='session_key']",
        "input#session_key",
        "input[name='username']",
        "input#username",
        "input[type='email']",
    ]
    PASSWORD_SELECTORS = [
        "input[name='session_password']",
        "input#session_password",
        "input[type='password']",
    ]
    SUBMIT_SELECTORS = [
        "button[type='submit']",
        "button[data-id='sign-in-form__submit-btn']",
        "button:has-text('Sign in')",
        "button:has-text('Log in')",
    ]

    def __init__(self, page: Page):
        self.page = page

    def open(self):
        self.page.goto(self.URL, wait_until="domcontentloaded")
        self.page.wait_for_load_state("networkidle", timeout=10000)
        return self

    def _find_first_visible(self, selectors: list[str]) -> Locator:
        for selector in selectors:
            locator = self.page.locator(selector).first
            if locator.count() > 0:
                return locator
        raise AssertionError(f"No matching locator found for selectors: {selectors}")

    def login(self, username: str, password: str):
        username_input = self._find_first_visible(self.USERNAME_SELECTORS)
        password_input = self._find_first_visible(self.PASSWORD_SELECTORS)
        submit_button = self._find_first_visible(self.SUBMIT_SELECTORS)

        username_input.wait_for(state="visible", timeout=15000)
        username_input.fill(username)
        password_input.wait_for(state="visible", timeout=15000)
        password_input.fill(password)
        submit_button.wait_for(state="visible", timeout=15000)
        submit_button.click()
        self.page.wait_for_load_state("networkidle", timeout=30000)
        return self

    def is_logged_in(self) -> bool:
        current_url = self.page.url.lower()
        return "/feed" in current_url or "/in/" in current_url

    def login_with_env(self):
        username = os.getenv("LINKEDIN_USERNAME")
        password = os.getenv("LINKEDIN_PASSWORD")

        if not username or not password:
            raise ValueError("Set LINKEDIN_USERNAME and LINKEDIN_PASSWORD environment variables before running this test")

        self.open()
        self.login(username, password)
        return self
