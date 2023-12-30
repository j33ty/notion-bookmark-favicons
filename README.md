# notion-bookmark-favicons

A script to add favicons to a Notion database items.

## Run

Create a `.env` file with the following variables (replace the values with your own):

```bash
INTEGRATION_TOKEN=integration_token
DATABASE_ID=database_id
```

Run the script:

```bash
set -a; source .env; set +a | python3 app.py
```

## Notes

#### Setup Integration in Notion

1. Create an integration for Notion from [Developer Portal](https://www.notion.so/my-integrations).
2. Add integration to the database: Click the 3 dots, under Connections and add the connections.

#### Find Database ID

URL format:

```
https://www.notion.so/long_hash_1?v=long_hash_2
```

In the database URL below, `long_hash_1` is the database ID and `long_hash_2` is the view ID.
