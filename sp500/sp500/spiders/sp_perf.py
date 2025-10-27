import scrapy
from bs4 import BeautifulSoup


class SpPerfSpider(scrapy.Spider):
    name = "sp_perf"
    allowed_domains = ["slickcharts.com"]
    start_urls = ["https://www.slickcharts.com/sp500/performance"]

    # keep it polite, make CSV open nicely in Excel
    custom_settings = {
        "USER_AGENT": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                       "AppleWebKit/537.36 (KHTML, like Gecko) "
                       "Chrome/124.0 Safari/537.36"),
        "FEED_EXPORT_ENCODING": "utf-8-sig",
        "ROBOTSTXT_OBEY": True,
        "DOWNLOAD_DELAY": 0.25,
    }

    def parse(self, response):
        # Use BeautifulSoup + html5lib to avoid lxml charset issues entirely
        soup = BeautifulSoup(response.text, "html5lib")

        table = soup.select_one("table")
        if not table:
            self.logger.warning("No table found. Writing page.html for inspection.")
            with open("page.html", "w", encoding="utf-8") as f:
                f.write(response.text)
            return

        tbody = table.find("tbody")
        rows = tbody.find_all("tr") if tbody else []
        self.logger.info("Found %d rows", len(rows))

        for tr in rows:
            tds = tr.find_all("td")
            if len(tds) < 4:
                continue
            number  = tds[0].get_text(strip=True)
            company = tds[1].get_text(strip=True)
            symbol  = tds[2].get_text(strip=True)
            ytd     = tds[3].get_text(strip=True).replace("%", "")

            yield {
                "number": number,
                "company": company,
                "symbol": symbol,
                "ytd_return": ytd,
            }
