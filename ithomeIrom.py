import asyncio
from playwright.async_api import async_playwright, Playwright


async def crawler(playwright: Playwright, pageNumber: int):
    webkit = playwright.webkit
    browser = await webkit.launch(headless=True)
    context = await browser.new_context()
    page = await context.new_page()
    try:
        url = f"https://ithelp.ithome.com.tw/2025ironman?page={pageNumber}"
        print(f"goto page {url}")
        response = await page.goto(url)
        print(f"response status: {response.status}")
        if response.status != 200:
            print(f"Failed to load page {pageNumber}")
            await browser.close()
            return

        print(f"scraping page {pageNumber}")
        selector = "#ir-list > div > section > section.sec-articles > div.container > div.row:nth-child(2) div.articles-box"
        articleBoxs = await page.locator(selector).all()
    finally:
        await browser.close()


async def main():
    async with async_playwright() as playwright:
        await crawler(playwright, 1)

if __name__ == "__main__":
    asyncio.run(main())
