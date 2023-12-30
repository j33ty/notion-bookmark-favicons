import os
from notion_client import Client
from urllib.parse import urlparse


# Database column names in Notion.
db_key_name = "Name"
db_key_url = "url"


# Function to get environment variable
def get_env_variable(name):
    value = os.getenv(name)
    if value is None or value == "":
        raise EnvironmentError(f"Environment variable '{name}' not found.")
    return value


# Function to get favicon URL
def get_favicon_url(website_url):
    parsed = urlparse(website_url)
    # Only use base URL for favicon search
    favicon_url = "https://www.google.com/s2/favicons?domain=" + parsed.netloc
    return favicon_url


# Function to update a row with the favicon
def update_notion_page_with_icon(notion, page_id, icon_url):
    notion.pages.update(
        **{
            "page_id": page_id,
            "icon": {
                "type": "external",
                "external": {
                    "url": icon_url,
                }
            },
        }
    )


def notion_page_has_favicon(notion, page_id):
    row = notion.pages.retrieve(page_id=page_id)
    if "icon" in row and row["icon"] is not None:
        return True
    else:
        return False


# Integration token of your Notion integration
integration_token = get_env_variable("INTEGRATION_TOKEN")

# ID of your Notion database
database_id = get_env_variable("DATABASE_ID")

# Initialize Notion client
notion = Client(auth=integration_token)

# Retrieve all rows from the database
start_cursor = None
while True:
    query = notion.databases.query(
        database_id=database_id, start_cursor=start_cursor)
    rows = query.get("results", [])
    print("Retrieved %d rows from Notion database with start cursor=%s" %
          (len(rows), start_cursor))

    # Process each row
    for row in rows:
        page_id = row["id"]
        page_title = row["properties"][db_key_name]['title'][0]["plain_text"]

        if notion_page_has_favicon(notion, page_id):
            print("Skipped %s" % (page_title))
            continue

        favicon_url = get_favicon_url(row["properties"][db_key_url]["url"])
        update_notion_page_with_icon(notion, page_id, favicon_url)
        print("Updated %s" % (page_title))

    # has_more is False when we've reached the last page of results
    if query["has_more"]:
        start_cursor = query["next_cursor"]
    else:
        break
