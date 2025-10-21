# Automation Framework

This is a sample test automation framework built using Python, Playwright, and Pytest. It is designed to automate web application testing and integrate with Azure DevOps Test Plans.

## Features

- **Web Automation**: Uses Playwright for browser automation.
- **Test Management**: Integrates with Azure DevOps Test Plans to create test runs and update test results.
- **Logging**: Provides detailed logs for test execution.
- **Screenshots**: Captures screenshots on test failures.
- **Configurable**: Supports configuration via `config.yaml` and environment variables.

## Project Structure
```
├── config.yaml # Configuration file
├── conftest.py # Pytest hooks and fixtures
├── pages/ # Page Object Model (POM) classes
├── tests/ # Test cases
├── utils/ # Utility modules
├── logs/ # Logs directory
├── screenshots/ # Screenshots directory
└── requirements.txt # Python dependencies
```

## Setup Instructions

### Prerequisites

- Python 3.8 or higher
- Node.js (for Playwright installation)

### Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd automation-framework
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   playwright install
   ```

3. Set the following environment variables before running the tests:

   ```bash
   export APP_USERNAME="your-username"
   export APP_PASSWORD="your-password"
   export AZURE_DEVOPS_PAT="your-pat-token"
   ```
4. Update config.yaml with other required values.
Running Tests
Run all tests:

```bash
pytest
```

Logs and Screenshots
Logs are saved in the logs/ directory.
Screenshots of failed tests are saved in the screenshots/ directory.

## Integration with Azure DevOps
This framework integrates with Azure DevOps Test Plans to:

- Create test runs
- Update test results
- Close test runs

Ensure the following values are set in config.yaml or environment variables:

- organization
- project
- test_plan_id
- test_suite_id
- pat_token