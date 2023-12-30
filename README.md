# notion-bookmark-favicons

A script to add favicons to a Notion database items.

## Setup

1. Install [Python 3.8+](https://www.python.org/downloads/).
1. Install dependencies with [pip](https://pypi.org/project/pip/):
   ```bash
   pip3 install -r requirements.txt
   ```
1. Setup Integration in [Notion Developer Portal](https://developers.notion.com).
   1. Go to [My Integrations](https://www.notion.so/my-integrations).
   1. Create a new integration.
   1. Select Type: Internal Integration.
   1. Select Associated Workspace: <Your Workspace>.
   1. Name: Populate Favicons.
   1. Upload Optional Logo.
   1. Copy the Integration Token.
1. Add the integration to the database.
   1. Navigate to the database in Notion.
   1. Click the 3 dots, and Add Connections.
   1. Select the integration 'Populate Favicons'.

## Run

1. Find the database ID.
   1. Navigate to the database in Notion.
   1. Note URL that should look like: `https://www.notion.so/long_hash_1?v=long_hash_2`
   1. `long_hash_1` is the database ID and `long_hash_2` is the view ID.
1. Create a `.env` file with the following variables (replace the values with your own):
   ```bash
   INTEGRATION_TOKEN=integration_token
   DATABASE_ID=database_id
   ```
1. Run the script:
   ```bash
   set -a; source .env; set +a | python3 app.py
   ```
