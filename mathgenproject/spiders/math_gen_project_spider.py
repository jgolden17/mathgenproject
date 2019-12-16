"""
Mathematics Genealogy Project Spider
"""
from scrapy import Request, Spider
from mathgenproject.items import Advisor, Mathematician
from mathgenproject.utils import clean_string, parse_id

class MathGenProjectSpider(Spider):
    """
    MathGenProjectSpider
    """

    name = "mathgenproject"

    ADVISOR_XPATH = '//p[contains(.,\'Advisor\')]/a'
    NAME_XPATH = '//h2[@style=\'text-align: center; margin-bottom: 0.5ex; margin-top: 1ex\']/text()'
    DISSERTATION_CSS = '#thesisTitle::text'
    HREF_CSS = '::attr(href)'

    mgp_id = None

    def start_requests(self):
        yield Request('https://genealogy.math.ndsu.nodak.edu/id.php?id=%s' % self.mgp_id)

    @staticmethod
    def parse_advisor(selector):
        """
        Parse advisor from selector
        """
        href = selector.css('::attr(href)').get()
        name = selector.css('::text').get()
        mgp_id = parse_id(href)

        return Advisor(
            id=mgp_id,
            name=clean_string(name),
            href=href
        )

    def parse_mathematician(self, response):
        """
        Parse mathematician from response
        """
        print(response.css('title'))
        name = response.xpath(self.NAME_XPATH).get()
        mgp_id = parse_id(response.request.url)
        dissertation = response.css(self.DISSERTATION_CSS).get()

        advisors = [self.parse_advisor(x) for x in response.xpath(self.ADVISOR_XPATH)]

        return Mathematician(
            id=mgp_id,
            name=clean_string(name),
            advisors=advisors,
            dissertation=clean_string(dissertation),
        )

    def parse(self, response):
        mathematician = self.parse_mathematician(response)
        advisors = mathematician['advisors']

        for advisor in advisors:
            href = advisor['href']

            if href is not None:
                yield response.follow(href, self.parse)

        yield mathematician
