  * [GitHub Copilot](https://docs.github.com/en/copilot "GitHub Copilot")/
  * [Copilot Chat Cookbook](https://docs.github.com/en/copilot/copilot-chat-cookbook "Copilot Chat Cookbook")/
  * [Testing code](https://docs.github.com/en/copilot/copilot-chat-cookbook/testing-code "Testing code")/
  * [Generate unit tests](https://docs.github.com/en/copilot/copilot-chat-cookbook/testing-code/generate-unit-tests "Generate unit tests")


# Generate unit tests
Copilot Chat can help with generating unit tests for a function.
## In this article
  * [Example scenario](https://docs.github.com/en/copilot/copilot-chat-cookbook/testing-code/generate-unit-tests#example-scenario)
  * [Example prompt](https://docs.github.com/en/copilot/copilot-chat-cookbook/testing-code/generate-unit-tests#example-prompt)
  * [Example response](https://docs.github.com/en/copilot/copilot-chat-cookbook/testing-code/generate-unit-tests#example-response)
  * [Further reading](https://docs.github.com/en/copilot/copilot-chat-cookbook/testing-code/generate-unit-tests#further-reading)


A good suite of unit tests is critical to the success of any project. However, writing these tests can be time-consuming and are often neglected. Copilot Chat can help generate these tests for you.
## [Example scenario](https://docs.github.com/en/copilot/copilot-chat-cookbook/testing-code/generate-unit-tests#example-scenario)
Imagine you have a Python function which validates data before updating the database. You need to create unit tests to ensure the validation performs the way you expect. You can ask Copilot Chat to generate these tests for you.
```
def validate_price(price: float):
  if price <= 0:
    raise ValueError("Price must be greater than 0")
  if price > 1000:
    raise ValueError("Price must be less than or equal to 1000")

```

## [Example prompt](https://docs.github.com/en/copilot/copilot-chat-cookbook/testing-code/generate-unit-tests#example-prompt)
`/tests Generate unit tests for this function. Validate both success and failure, and include edge cases.`
## [Example response](https://docs.github.com/en/copilot/copilot-chat-cookbook/testing-code/generate-unit-tests#example-response)
The following response is an example. Copilot Chat responses are non-deterministic, so you may get a different response from the one shown here.
If this is your first time asking Copilot Chat to generate unit tests, it may ask you if you wish to configure unit tests for your project. For this example, we are assuming you decline this offer.
Copilot will provide a strategy for generating the tests, and then provide the tests themselves.
```
import unittest
from generate_unit_tests import validate_price

class TestValidateProduct(unittest.TestCase):
  def test_price_zero(self):
    with self.assertRaises(ValueError) as context:
      validate_price(0)
    self.assertEqual(str(context.exception), "Price must be greater than 0")

  def test_price_negative(self):
    with self.assertRaises(ValueError) as context:
      validate_price(-10)
    self.assertEqual(str(context.exception), "Price must be greater than 0")

  def test_price_above_limit(self):
    with self.assertRaises(ValueError) as context:
      validate_price(1500)
    self.assertEqual(str(context.exception), "Price must be less than or equal to 1000")

  def test_price_edge_case_zero(self):
    with self.assertRaises(ValueError) as context:
      validate_price(0)
    self.assertEqual(str(context.exception), "Price must be greater than 0")

  def test_price_edge_case_max(self):
    try:
      validate_price(1000)
    except ValueError:
      self.fail("validate_price() raised ValueError unexpectedly!")

if __name__ == '__main__':
  unittest.main()

```

## [Further reading](https://docs.github.com/en/copilot/copilot-chat-cookbook/testing-code/generate-unit-tests#further-reading)
  * [Prompt engineering for Copilot Chat](https://docs.github.com/en/copilot/using-github-copilot/prompt-engineering-for-github-copilot)
  * [Best practices for using GitHub Copilot](https://docs.github.com/en/copilot/using-github-copilot/best-practices-for-using-github-copilot)


