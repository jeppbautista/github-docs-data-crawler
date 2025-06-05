  * [GitHub Copilot](https://docs.github.com/en/copilot "GitHub Copilot")/
  * [Copilot Chat Cookbook](https://docs.github.com/en/copilot/copilot-chat-cookbook "Copilot Chat Cookbook")/
  * [Documenting code](https://docs.github.com/en/copilot/copilot-chat-cookbook/documenting-code "Documenting code")/
  * [Sync documentation](https://docs.github.com/en/copilot/copilot-chat-cookbook/documenting-code/syncing-documentation-with-code-changes "Sync documentation")


# Syncing documentation with code changes
Copilot Chat can help with keeping code documentation up-to-date.
## In this article
  * [Example scenario](https://docs.github.com/en/copilot/copilot-chat-cookbook/documenting-code/syncing-documentation-with-code-changes#example-scenario)
  * [Example prompt](https://docs.github.com/en/copilot/copilot-chat-cookbook/documenting-code/syncing-documentation-with-code-changes#example-prompt)
  * [Example response](https://docs.github.com/en/copilot/copilot-chat-cookbook/documenting-code/syncing-documentation-with-code-changes#example-response)
  * [Further reading](https://docs.github.com/en/copilot/copilot-chat-cookbook/documenting-code/syncing-documentation-with-code-changes#further-reading)


It can be difficult to keep documentation up to date with changes to code. However, good documentation is essential for maintaining codebases and ensuring that developers can work effectively with the code. Copilot Chat can assist in updating existing code documentation.
## [Example scenario](https://docs.github.com/en/copilot/copilot-chat-cookbook/documenting-code/syncing-documentation-with-code-changes#example-scenario)
Imagine a scenario where you have a TypeScript function that retrieves products by category name, but the documentation is out of date.
```
/**
 * Retrieves all products belonging to a specific category.
 *
 * @param categoryId - The unique identifier of the product category
 * @returns Promise that resolves to an array of Product objects
 *
 * @example
 * const products = await getByCategoryName(5);
 * // Returns: [{id: 1, name: "Product 1", categoryId: 5}, ...]
 *
 * @throws {PrismaClientKnownRequestError} If database query fails
 * @see {@link https://www.prisma.io/docs/reference/api-reference/prisma-client-reference#findmany}
 */
async getByCategoryName(categoryId: number, page = 1, pageSize = 10): Promise<Products[]> {
  return await prisma.products.findMany({
    where: { categoryId },
    skip: (page - 1) * pageSize,
    take: pageSize,
    include: {
      reviews: {
        orderBy: { date: 'desc' },
        take: 5,
      },
    },
  });
}

```

## [Example prompt](https://docs.github.com/en/copilot/copilot-chat-cookbook/documenting-code/syncing-documentation-with-code-changes#example-prompt)
You can ask Copilot Chat to update the documentation according to the current code.
`Update the existing documentation for the getByCategoryName function to reflect the current implementation.`
## [Example response](https://docs.github.com/en/copilot/copilot-chat-cookbook/documenting-code/syncing-documentation-with-code-changes#example-response)
The following response is an example. Copilot Chat responses are non-deterministic, so you may get a different response from the one shown here.
Copilot explains it will create the updated documentation for the `getByCategoryName` function. It then provides the updated documentation, which now includes the `page` and `pageSize` parameters, as well as the `PrismaClientKnownRequestError` error that can be thrown.
For example:
```
/**
 * Retrieves all products belonging to a specific category with pagination and recent reviews.
 *
 * @param categoryId - The unique identifier of the product category
 * @param page - The page number for pagination (default: 1)
 * @param pageSize - Number of products per page (default: 10)
 * @returns Promise that resolves to an array of Product objects with their 5 most recent reviews
 *
 * @example
 * const products = await getByCategoryName(5, 2, 20);
 * // Returns: [{id: 1, name: "Product 1", categoryId: 5, reviews: [...5 recent reviews]}, ...]
 *
 * @throws {PrismaClientKnownRequestError} If database query fails
 * @see {@link https://www.prisma.io/docs/reference/api-reference/prisma-client-reference#findmany}
 */

```

## [Further reading](https://docs.github.com/en/copilot/copilot-chat-cookbook/documenting-code/syncing-documentation-with-code-changes#further-reading)
  * [Prompt engineering for Copilot Chat](https://docs.github.com/en/copilot/using-github-copilot/prompt-engineering-for-github-copilot)
  * [Best practices for using GitHub Copilot](https://docs.github.com/en/copilot/using-github-copilot/best-practices-for-using-github-copilot)


