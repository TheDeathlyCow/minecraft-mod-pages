"""
Usage: This script requires a Modrinth Personal Access Token with at least `write_project` permissions. This must be supplied with the MODRINTH_KEY environment variable, which can be supplied by a `.env` file.

Copyright 2025 TheDeathlyCow

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

import os
import sys
import json
import asyncio
from dotenv import load_dotenv
import requests


PROJECTS = ["thermoo", "frostiful", "scorchful"]


async def update_modrinth_project(project: str):
    print(f"Updating {project} mod page...")

    with open(f'{project}/modrinth.md') as modrinth_desc:
        body = modrinth_desc.read()

    r = requests.patch(
        url = f"https://api.modrinth.com/v2/project/{project}",
        headers={'Authorization': os.environ.get("MODRINTH_KEY")},
        params={ 'slug': project },
        json={
            'body': body
        }
    )

    if not r.ok:
        print(f"Failed to update {project}! Status code: {r.status_code}", file=sys.stderr)
        print(json.dumps(r.json(), indent=4), file=sys.stderr)
    else:
        print(f"Updated {project}!")


async def main():
    load_dotenv()

    await asyncio.gather(*(update_modrinth_project(project) for project in PROJECTS))


if __name__ == '__main__':
    asyncio.run(main())
