# E2E Automation Tool

This repository is an end-to-end automation workspace for building and running AI-assisted quality engineering workflows. It currently includes a starter Python + Playwright framework for browser automation, along with a custom agent guide for future automation development.

## What this repository includes

- A Python-based end-to-end automation framework using Playwright
- A starter test suite to validate the setup
- A reusable project structure for tests, pages, and utilities
- A custom agent configuration file to guide future automation work

## Project structure

- .agent.md: guidance for creating and maintaining Playwright-based automation work
- python_playwright_framework/: main automation framework folder
  - tests/: end-to-end test cases
  - pages/: page object classes for UI interactions
  - utils/: shared helper functions and utilities
  - requirements.txt: Python dependencies
  - pytest.ini: pytest configuration
  - playwright.config.py: Playwright configuration
  - README.md: framework-specific setup instructions

## Prerequisites

Before running the framework, make sure you have:

- Python 3.9 or newer
- pip installed
- A terminal with access to Python

## Setup instructions

1. Open the project folder:
   ```bash
   cd python_playwright_framework
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Install Playwright browsers:
   ```bash
   playwright install
   ```

5. Run the sample test:
   ```bash
   pytest
   ```

## Current automation workflow

The repository is intended to support the following workflow:

1. Read requirements or issue details from Jira
2. Create or update test cases
3. Validate test cases through automation
4. Merge changes in GitHub
5. Run build validation and create pull requests

## Future enhancements

Planned improvements include:

- More advanced page object models
- Shared fixtures for login and browser setup
- Data-driven test scenarios
- CI/CD integration for automated test execution
- Better reporting and screenshots on failures

## Notes

This is a starting point for a scalable automation framework. You can expand it by adding more tests, reusable page classes, and environment-based configuration as the project grows.
