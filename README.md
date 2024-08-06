# E-commerce Automation Tests

This project contains automated tests for an e-commerce site, including UI and API tests. The tests use the BDD approach and are designed to be executed in a Docker container for consistency.

## Minimum Requirements

- **Python**: 3.9 or later
- **Docker**: 20.10 or later
- **Docker Compose**: 1.27 or later
- **Google Chrome**: Make sure the ChromeDriver version is compatible with the installed Chrome version.

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/ferhattufekci/ecommerce-automation-case-study.git
cd ecommerce-automation-case-study
```

### 2. Install Dependencies

Dependencies are listed in the requirements.txt file. You can install them locally using pip:

```bash
pip install -r requirements.txt
```

### 3. Set Up Docker

Build Docker Image
Build the Docker image using the provided Dockerfile:

```bash
docker build -t ecommerce-tests .
```

Run Docker Compose
Use Docker Compose to run the tests:

```bash
docker-compose up
```

## 4. Running Tests Locally

If you prefer to run tests locally without Docker, use pytest:

```bash
pytest --html=reports/report.html
```

## 5.Test Report

Test results will be saved in the reports directory in HTML format. You can view the report by opening reports/report.html in a web browser.

## 6. Screenshots

In case of test failures, screenshots will be saved in the screenshots directory. Each screenshot is named based on the test case that failed.

## Contributing

Feel free to open issues or submit pull requests. Please ensure that any changes are tested before submission.

## License

This project is licensed under the MIT License. See the [LICENSE](/LICENSE) file for details.

## Author

[![Author](https://img.shields.io/badge/author-ferhattufekci-red)](https://github.com/ferhattufekci)
[![Contact](https://img.shields.io/badge/contact-linkedin-blue)](https://www.linkedin.com/in/ferhattufekci/)
