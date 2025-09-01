import asyncio
from playwright.async_api import async_playwright, Playwright


async def crawler(page: int):
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto(f"https://ithelp.ithome.com.tw/2025ironman?page={page}")
        
        # Add your scraping logic here
        # get xpath
        pages = await page.locator("//*[@id='ir-list']/div/nav/div/span[3]").inner_text()
        print(pages)
        await browser.close()

if __name__ == "__main__":
    asyncio.run(crawler(1))
