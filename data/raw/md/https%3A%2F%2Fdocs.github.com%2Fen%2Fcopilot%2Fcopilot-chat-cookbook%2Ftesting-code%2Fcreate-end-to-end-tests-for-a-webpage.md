  * [GitHub Copilot](https://docs.github.com/en/copilot "GitHub Copilot")/
  * [Copilot Chat Cookbook](https://docs.github.com/en/copilot/copilot-chat-cookbook "Copilot Chat Cookbook")/
  * [Testing code](https://docs.github.com/en/copilot/copilot-chat-cookbook/testing-code "Testing code")/
  * [Create end-to-end tests](https://docs.github.com/en/copilot/copilot-chat-cookbook/testing-code/create-end-to-end-tests-for-a-webpage "Create end-to-end tests")


# Create end-to-end tests for a webpage
Copilot Chat can help with generating end-to-end tests.
## In this article
  * [Example scenario](https://docs.github.com/en/copilot/copilot-chat-cookbook/testing-code/create-end-to-end-tests-for-a-webpage#example-scenario)
  * [Example prompt](https://docs.github.com/en/copilot/copilot-chat-cookbook/testing-code/create-end-to-end-tests-for-a-webpage#example-prompt)
  * [Example response](https://docs.github.com/en/copilot/copilot-chat-cookbook/testing-code/create-end-to-end-tests-for-a-webpage#example-response)
  * [Further reading](https://docs.github.com/en/copilot/copilot-chat-cookbook/testing-code/create-end-to-end-tests-for-a-webpage#further-reading)


Creating end-to-end tests for a webpage can be time-consuming and complex as the HTML will be generated dynamically. Copilot Chat can help you create end-to-end tests for a webpage by suggesting the necessary code to interact with the webpage and validate the expected results.
## [Example scenario](https://docs.github.com/en/copilot/copilot-chat-cookbook/testing-code/create-end-to-end-tests-for-a-webpage#example-scenario)
Imagine a React application that displays product details on a webpage. You need to create end-to-end tests to ensure the product details are displayed correctly. You can ask Copilot Chat to generate these tests for you.
```
import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';

const ProductDetails = ({ productId = '1' }) => {
  const [product, setProduct] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchProduct = async (try {
        const response = await fetch(`/api/product/${productId}`);
        if (!response.ok) {
          throw new Error('Product not found');
        }
        const data = await response.json();
        setProduct(data);
        setLoading(false);
      } catch (err) {
        setError(err.message);
        setLoading(false);
      }
    };

    fetchProduct();
    return;
  }, [productId]); // Add productId to dependency array

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error}</div>;

  return (
    <div>
      {product && (
        <div>
          <h2>{product.name}</h2>
          <p>{product.description}</p>
          <p>Price: ${product.price}</p>
        </div>
      )}
    </div>
  );
};

ProductDetails.propTypes = {
  productId: PropTypes.string
};

export default ProductDetails;

```

## [Example prompt](https://docs.github.com/en/copilot/copilot-chat-cookbook/testing-code/create-end-to-end-tests-for-a-webpage#example-prompt)
This example uses Playwright for end-to-end testing, but you can use other frameworks like Selenium or Cypress.
`Using Playwright, generate an e2e test to ensure the product displays correctly.`
If you have an existing test you wish Copilot to use as a model, you can use `#file: path/to/test-file.js` to provide the path to the file, and include this information in the prompt.
## [Example response](https://docs.github.com/en/copilot/copilot-chat-cookbook/testing-code/create-end-to-end-tests-for-a-webpage#example-response)
The following response is an example. Copilot Chat responses are non-deterministic, so you may get a different response from the one shown here.
Copilot will respond with an end-to-end test that you can use for your application.
```
import { test, expect } from '@playwright/test';

test.describe('ProductDetails Component', () => {
  test.beforeEach(async ({ page }) => {
    // Set up API mocking
    await page.route('/api/product/1', async (route) => {
      await route.fulfill({
        status: 200,
        contentType: 'application/json',
        body: JSON.stringify({
          name: 'Test Product',
          description: 'This is a test product',
          price: 99.99
        })
      });
    });

    // Mock error response for product ID 999
    await page.route('/api/product/999', async (route) => {
      await route.fulfill({
        status: 404,
        contentType: 'application/json',
        body: JSON.stringify({ error: 'Product not found' })
      });
    });
  });

  test('displays loading state initially', async ({ page }) => {
    await page.goto('/product/1');
    const loadingElement = page.locator('text=Loading...');
    await expect(loadingElement).toBeVisible();
  });

  test('displays product details correctly', async ({ page }) => {
    await page.goto('/product/1');

    // Wait for loading to disappear
    await expect(page.getByText('Loading...')).toBeHidden();

    // Check all product details
    await expect(page.locator('h2')).toHaveText('Test Product');
    await expect(page.locator('text=This is a test product')).toBeVisible();
    await expect(page.locator('text=Price: $99.99')).toBeVisible();
  });

  test('displays error message when product not found', async ({ page }) => {
    await page.goto('/product/999');

    // Wait for loading to disappear
    await expect(page.getByText('Loading...')).toBeHidden();

    // Check error message
    await expect(page.locator('text=Error: Product not found')).toBeVisible();
  });
});

```

## [Further reading](https://docs.github.com/en/copilot/copilot-chat-cookbook/testing-code/create-end-to-end-tests-for-a-webpage#further-reading)
  * [Prompt engineering for Copilot Chat](https://docs.github.com/en/copilot/using-github-copilot/prompt-engineering-for-github-copilot)
  * [Best practices for using GitHub Copilot](https://docs.github.com/en/copilot/using-github-copilot/best-practices-for-using-github-copilot)


