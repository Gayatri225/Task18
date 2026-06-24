## Allure Reporting Integration

The project integrates the **Allure Reporting Framework** using the `allure-behave` package to generate detailed test execution reports.

Allure step annotations have been implemented in the Behave step definitions to improve report readability and traceability.

Example:

```python
@allure.step("Navigate to Zen Portal")
@allure.step("Validate username and password input boxes")
@allure.step("Validate submit button")
@allure.step("Login with valid username and password")
@allure.step("Login with invalid username and password")
@allure.step("Logout from Zen Portal")
```

Allure result files are generated using:

```bash
py -m behave -f allure_behave.formatter:AllureFormatter -o allure-results
```

This command generates Allure result files in the `allure-results` directory, which can be used to create an HTML report when the Allure Commandline tool is available.
