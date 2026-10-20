# ZombiePlus - Playwright with Python

E2E tests for **ZombiePlus**, a training app from the QAxperience course (by Papito). I first automated it with Playwright + JavaScript ([projeto-zombieplus-pw](https://github.com/BrunoCasavechia/projeto-zombieplus-pw)) and now I'm rewriting the tests in Python to learn the pytest ecosystem.

## Stack

- Python + pytest
- Playwright (`pytest-playwright`)
- Page Object Model
- Faker for test data
- pytest-html for the report

## Project structure

```
pages/   page objects (locators and actions for each screen)
tests/   test files
```

## What is covered

**Landing page (lead form)**
- successful sign up
- blank name
- blank email
- invalid email
- duplicated email

**Login (admin)** - in progress

## Running

The ZombiePlus app is not part of this repo. It needs to be running locally on `http://localhost:3000` (setup comes from the course).

```bash
pip install -r requirements.txt
playwright install

pytest                                         # all tests
pytest tests/test_landing_page.py              # one file
pytest tests/test_landing_page.py::test_success --headed   # one test, with browser
```

After the run, `report.html` is created in the root folder. Videos and screenshots are saved in `test-results/` only when a test fails.
