#!/usr/bin/env python3
"""
OctoTrip Rental Cars — stdio MCP proxy.

Bridges stdio-only MCP clients to the hosted OctoTrip server.
Use when your client doesn't support Streamable HTTP transport.

    python proxy.py
    OCTOTRIP_ENDPOINT=https://custom.endpoint/mcp python proxy.py
"""

import json
import os
import sys
import urllib.error
import urllib.request

ENDPOINT = os.environ.get(
    "OCTOTRIP_ENDPOINT",
    "https://mcp.octotrip.app/rental-cars/mcp",
)
TIMEOUT = 120


def forward(request, session_id=None):
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json, text/event-stream",
    }
    if session_id:
        headers["Mcp-Session-Id"] = session_id

    data = json.dumps(request).encode()
    req = urllib.request.Request(ENDPOINT, data=data, headers=headers, method="POST")
    resp = urllib.request.urlopen(req, timeout=TIMEOUT)

    new_session = resp.headers.get("mcp-session-id", session_id)

    if "id" not in request:
        return None, new_session

    ct = resp.headers.get("content-type", "")
    body = resp.read().decode()

    if "event-stream" in ct:
        data = None
        for line in body.strip().splitlines():
            if line.startswith("data: "):
                data = json.loads(line[6:])
        return data, new_session

    return json.loads(body), new_session


def error_response(req_id, code, message):
    return {"jsonrpc": "2.0", "id": req_id, "error": {"code": code, "message": message}}


def main():
    session_id = None

    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        try:
            request = json.loads(line)
        except json.JSONDecodeError:
            continue

        try:
            response, session_id = forward(request, session_id)
        except TimeoutError:
            response = error_response(request.get("id"), -32000, "upstream timeout")
        except urllib.error.HTTPError as exc:
            response = error_response(
                request.get("id"), -32000, f"upstream HTTP {exc.code}"
            )
        except urllib.error.URLError:
            response = error_response(request.get("id"), -32000, "upstream unreachable")

        if response is not None:
            sys.stdout.write(json.dumps(response) + "\n")
            sys.stdout.flush()


if __name__ == "__main__":
    main()
