# General
AUTHOR = "花村貴史 / Takashi Hanamura"
AUTHOR_DESC = (
    "ソフトウェアエンジニア＆空気感フォトグラファー。Python/Golang/JavaScriptを使ったり、\n"
    "人や場の「空気感」をそっとすくい撮ることを得意としています。"
)
SITENAME = "nnamm.work.work"
SITESUBTITLE = "portfolio note"
# for Dev
SITEURL = ""
SITEDESCRIPTION = "空気感フォトグラファーのポートフォリオサイトです。写真系、技術系のブログと作品リンクを掲載しています。"
TIMEZONE = "Japan"
DEFAULT_LANG = "ja"

# for Dev
GOOGLE_ANALYTICS = ""
OUTPUT_PATH = "output_dev"

# Theme
THEME = "./theme/nnamm.work"
PATH = "content"
PAGE_PATHS = ["pages"]
STATIC_PATHS = ["images", "extra/robots.txt"]
EXTRA_PATH_METADATA = {"extra/robots.txt": {"path": "robots.txt"}}
DIRECT_TEMPLATES = ["index", "categories", "tags"]
ARTICLE_URL = "posts/{slug}/"
ARTICLE_SAVE_AS = "posts/{slug}/index.html"
PAGE_URL = "pages/{slug}/"
PAGE_SAVE_AS = "pages/{slug}/index.html"

# Markdown
MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.codehilite": {"css_class": "highlight"},
        "markdown.extensions.extra": {},
        "markdown.extensions.meta": {},
        "markdown.extensions.toc": {},
        "markdown_cjk_spacing.cjk_spacing": {},
    },
    "output_format": "html5",
}

# Pagination
DEFAULT_PAGINATION = 5
# PAGINATION_PATTERNS = (
#     (1, "{url}", "{save_as}"),
#     (2, "{base_name}/page/{number}/", "{base_name}/page/{number}/index.html"),
# )

# Feed
FEED_ALL_ATOM = "feeds/all.rss.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.rss.xml"
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Site menu
HEADER_MENU_ITEMS = (
    ("Portfolio", "https://www.behance.net/nnamm", "_blank"),
    ("Stock Photo", "https://note.com/tnnamm/m/m2aa9550047ed", "_blank"),
    ("About", "http://localhost:8000/pages" + "/about", "_self"),  # for Dev
    (
        "Privacy Policy",
        "http://localhost:8000/pages" + "/privacy-policy",
        "_self",
    ),  # for Dev
)

# -------------------
#  Pelican plugins
# -------------------
# 1.Pelican sitemap
SITEMAP = {
    "format": "xml",
    "priorities": {"articles": 0.8, "indexes": 0.5, "pages": 1.0},
    "changefreqs": {"articles": "monthly", "indexes": "daily", "pages": "monthly"},
}

# 2.Pelican Image Process
IMAGE_PROCESS = {
    # Article/Page images
    "crisp": {
        "type": "responsive-image",
        "srcset": [
            ("1x", ["scale_in 1200 900 True"]),
            ("2x", ["scale_in 1600 1200 True"]),
            ("3x", ["scale_in 2000 1500 True"]),
        ],
        "default": "1x",
    },
    # Default images
    "default": {
        "type": "responsive-image",
        "srcset": [
            ("1x", ["scale_in 1800 1200 True"]),
            ("2x", ["scale_in 2400 1600 True"]),
            ("3x", ["scale_in 3000 2000 True"]),
        ],
        "default": "1x",
    },
    # sample settings
    "large-photo": {
        "type": "responsive-image",
        "sizes": (
            "(min-width: 1200px) 800px,"
            "(min-width: 992px) 650px,"
            "(min-width: 768px) 718px,"
            "100vw"
        ),
        "srcset": [
            ("600w", ["scale_in 600 450 True"]),
            ("800w", ["scale_in 800 600 True"]),
            ("1600w", ["scale_in 1600 1200 True"]),
        ],
        "default": "800w",
    },
}
