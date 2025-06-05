  * [GitHub Copilot](https://docs.github.com/en/copilot "GitHub Copilot")/
  * [Copilot Chat Cookbook](https://docs.github.com/en/copilot/copilot-chat-cookbook "Copilot Chat Cookbook")/
  * [Testing code](https://docs.github.com/en/copilot/copilot-chat-cookbook/testing-code "Testing code")/
  * [Create mock objects](https://docs.github.com/en/copilot/copilot-chat-cookbook/testing-code/create-mock-objects-to-abstract-layers "Create mock objects")


# Create mock objects to abstract layers
Copilot Chat can help with creating mock objects that you can use for unit tests.
## In this article
  * [Example scenario](https://docs.github.com/en/copilot/copilot-chat-cookbook/testing-code/create-mock-objects-to-abstract-layers#example-scenario)
  * [Example prompt](https://docs.github.com/en/copilot/copilot-chat-cookbook/testing-code/create-mock-objects-to-abstract-layers#example-prompt)
  * [Example response](https://docs.github.com/en/copilot/copilot-chat-cookbook/testing-code/create-mock-objects-to-abstract-layers#example-response)
  * [Further reading](https://docs.github.com/en/copilot/copilot-chat-cookbook/testing-code/create-mock-objects-to-abstract-layers#further-reading)


When creating unit tests, it's important to ensure they're isolated and not depending on external services. One way to achieve this is to create mock objects that abstract layers of your application. Copilot Chat can help you generate the code you need to create these mock objects.
## [Example scenario](https://docs.github.com/en/copilot/copilot-chat-cookbook/testing-code/create-mock-objects-to-abstract-layers#example-scenario)
Imagine a website built with TypeScript which displays a list of runners. You have a service which fetches the runners from a database, and the server-side code which uses this service. You want to test the server-side code, but you don't want to make a call to the database. You can ask Copilot Chat to generate a mock object for the service.
```
// SvelteKit example at +page.server.ts
import service from './service';

export async function load({ params }) {
  const runner = await service.getRunner(params.id);

  return {
    runner
  };
}

```

## [Example prompt](https://docs.github.com/en/copilot/copilot-chat-cookbook/testing-code/create-mock-objects-to-abstract-layers#example-prompt)
This example assumes you are using [vitest](https://vitest.dev/) for your tests, but will work with other test runners.
`/tests Create a unit test to ensure the service is called correctly. Mock the service object.`
If you have an existing test you wish Copilot to use as a model, you can use `#file: path/to/test-file.js` to provide the path to the file, and include this information in the prompt.
## [Example response](https://docs.github.com/en/copilot/copilot-chat-cookbook/testing-code/create-mock-objects-to-abstract-layers#example-response)
The following response is an example. Copilot Chat responses are non-deterministic, so you may get a different response from the one shown here.
Copilot provides the plan it will implement and the code text which includes the mocks.
```
import { describe, it, expect, vi, beforeEach } from 'vitest';
import { load } from './+page.server.ts';

// Mock the entire service module
vi.mock('./service', () => ({
  default: {
    getRunner: vi.fn()
  }
}));

// Import the mocked service
import service from './service';

describe('load function', () => {
  const mockRunner = {
    id: '123',
    name: 'Test Runner',
    status: 'active'
  };

  beforeEach(() => {
    // Reset mock before each test
    vi.resetAllMocks();

    // Setup default mock implementation
    (service.getRunner as any).mockResolvedValue(mockRunner);
  });

  it('should fetch runner with correct id', async () => {
    const params = { id: '123' };
    const result = await load({ params });

    expect(service.getRunner).toHaveBeenCalledWith('123');
    expect(service.getRunner).toHaveBeenCalledTimes(1);
    expect(result).toEqual({ runner: mockRunner });
  });
});

```

## [Further reading](https://docs.github.com/en/copilot/copilot-chat-cookbook/testing-code/create-mock-objects-to-abstract-layers#further-reading)
  * [Prompt engineering for Copilot Chat](https://docs.github.com/en/copilot/using-github-copilot/prompt-engineering-for-github-copilot)
  * [Best practices for using GitHub Copilot](https://docs.github.com/en/copilot/using-github-copilot/best-practices-for-using-github-copilot)


