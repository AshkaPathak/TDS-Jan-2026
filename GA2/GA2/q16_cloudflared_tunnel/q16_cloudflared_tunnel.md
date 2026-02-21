# GA2 — Q16: Create a Public Tunnel with cloudflared

## Problem Summary
Create a public URL for a local web server running on port **5500** using a Cloudflare Quick Tunnel (`cloudflared`).  
The submitted URL must be reachable from the internet and return content served from the local machine.

The evaluator sends an HTTP GET request to the submitted URL and verifies that it serves content from the local server.

---

## Step 1 — Start Local Web Server (Port 5500)

From the directory to be served:

```bash
python3 -m http.server 5500
```

This starts a server at:

http://localhost:5500

The server process was kept running during verification.

---

## Step 2 — Install cloudflared (macOS)

```bash
brew install cloudflared
```

Verify installation:

```bash
cloudflared --version
```

---

## Step 3 — Create Cloudflare Quick Tunnel

In a second terminal (while the local server is running):

```bash
cloudflared tunnel --url http://localhost:5500
```

Cloudflared generates a temporary public URL ending in `.trycloudflare.com`.

---

## Public Tunnel URL Used

The tunnel generated the following public URL:

https://above-nodes-calculate-gilbert.trycloudflare.com

Note:
- This URL is generated dynamically.
- It must be copied exactly from the cloudflared output.
- Do not use the example placeholder shown in the question.
- Do not add a trailing slash.

---

## Verification Steps

1. Opened the generated tunnel URL in a browser.
2. Confirmed it served the same content as `http://localhost:5500`.
3. Ensured both processes were running during submission:

   - `python3 -m http.server 5500`
   - `cloudflared tunnel --url http://localhost:5500`

The portal successfully validated the URL by performing an HTTP GET request.

---

## Conclusion

A Cloudflare Quick Tunnel successfully exposed the local server running on port 5500 to a public `trycloudflare.com` URL.  
The submitted URL was reachable and returned local server content, satisfying the assignment requirements.
