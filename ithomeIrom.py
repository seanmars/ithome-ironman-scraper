import asyncio
from playwright.async_api import async_playwright, Playwright, Locator


async def author_crawler(locator: Locator):
    divs = await locator.locator("div.row > div").all()
    left = divs[0]
    right = divs[1]
    topic = await right.locator("div > div.tag > span").inner_text()
    author_name = await left.locator("div.contestants-list__name").inner_text()
    a_tag = right.locator("a").first
    title = await a_tag.inner_text()
    href = await a_tag.get_attribute("href")
    return {
        "author": author_name,
        "topic": topic,
        "title": title,
        "href": href
    }


async def crawler_all_authors(playwright: Playwright, page_number: int):
    webkit = playwright.webkit
    browser = await webkit.launch(headless=True)
    context = await browser.new_context()
    page = await context.new_page()
    result = []
    total_pages = page_number
    try:
        url = f"https://ithelp.ithome.com.tw/2025ironman/signup/list?page={page_number}"
        response = await page.goto(url)
        if response.status != 200:
            print(f"Failed to load page {page_number}")
            await browser.close()
            return

        selector = "section.sec-contestants > div.container > div.list-card"
        article_cards = await page.locator(selector).all()
        for card in article_cards:
            article = await author_crawler(card)
            result.append(article)

        selector_nav = "section.sec-contestants > div.container > nav.pagination-container > div > span.pagination-inner"
        nav = await page.locator(selector_nav).all()
        total_pages = int(await (await nav[2].locator("a").all())[-1].inner_text())
    finally:
        await browser.close()
        return {
            "total_pages": total_pages,
            "articles": result
        }


async def main():
    async with async_playwright() as playwright:
        current_page = 1
        dataset = []
        while True:
            print(f"Crawling page {current_page}...")
            result = await crawler_all_authors(playwright, current_page)
            total_pages = result["total_pages"]
            if not result or "articles" not in result:
                break

            dataset.extend(result["articles"])
            if current_page == total_pages:
                break
            current_page += 1

        print(f"Total articles: {len(dataset)}")
        # save to json file
        import json
        with open("ithome_ironman_authors.json", "w", encoding="utf-8") as f:
            json.dump(dataset, f, ensure_ascii=False, indent=4)
        print("Data saved to ithome_ironman_authors.json")

if __name__ == "__main__":
    asyncio.run(main())
