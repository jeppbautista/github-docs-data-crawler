import asyncio
from typing import List, Tuple
import urllib.parse

from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, RateLimiter
from crawl4ai.async_dispatcher import SemaphoreDispatcher
from crawl4ai.content_scraping_strategy import LXMLWebScrapingStrategy


ROOT_URL = [
    "https://docs.github.com/en/get-started",
    "https://docs.github.com/en/codespaces",
    "https://docs.github.com/en/copilot",
    "https://docs.github.com/en/actions",
    "https://docs.github.com/en/code-security",
    "https://docs.github.com/en/github-cli",
    "https://docs.github.com/en/issues",
    "https://docs.github.com/en/organizations",
    "https://docs.github.com/en/apps",
    "https://docs.github.com/en/communities",
    
]

async def main():
    browser_config = BrowserConfig(headless=False, verbose=False)
    config = CrawlerRunConfig(
        check_robots_txt=True,
        css_selector="div[data-testid='sidebar']",
        scraping_strategy=LXMLWebScrapingStrategy(),
        verbose=True,
        simulate_user=True,
        delay_before_return_html=2.0
    )

    links =[]

    async with AsyncWebCrawler(config=browser_config) as crawler:
        for url in ROOT_URL:
            results = await crawler.arun(url, config=config)

            links.append({ "url": url, "links": [result["href"] for result in results.links['internal']]})

            print(links)
    

    del results

    dispatcher = SemaphoreDispatcher(
        max_session_permit=5,
        rate_limiter=RateLimiter(
            base_delay=(2.0, 5.0),
            max_delay=60.0,
            max_retries=5,
            rate_limit_codes=[429, 503]
        ),
    )

    link_config = CrawlerRunConfig(
        check_robots_txt=True,
        css_selector="#main-content",
        scraping_strategy=LXMLWebScrapingStrategy(),
        verbose=True,
        simulate_user=True,
        delay_before_return_html=2.0,
        capture_mhtml=True
    )

    async with AsyncWebCrawler(config=browser_config) as link_crawler:
        for i, url in enumerate(ROOT_URL):
            results = await link_crawler.arun_many(
                urls=links[i]["links"], 
                config=link_config,
                dispatcher=dispatcher
            )

            for result in results:
                if result.success:
                    print(result.url)
                    with open(f"data/raw/html/{urllib.parse.quote_plus(result.url)}.html", "w+", encoding="utf-8") as f:
                        f.write(result.cleaned_html)
                    with open(f"data/raw/md/{urllib.parse.quote_plus(result.url)}.md", "w+", encoding="utf-8") as f:
                        f.write(result.markdown.raw_markdown)
                else:
                    print(f"Failed to crawl {result.url}: {result.error_message}")


if __name__ == "__main__":
    asyncio.run(main())
