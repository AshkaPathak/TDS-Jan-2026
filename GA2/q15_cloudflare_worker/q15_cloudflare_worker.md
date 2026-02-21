# GA2 — Q15: Cloudflare Workers Serverless Deployment (POST /data)

## Problem Summary

Deploy a Cloudflare Worker that exposes a POST endpoint at:

    /data

It must accept JSON input:

    { "type": "...", "value": ... }

And return JSON output:

    { "reversed": ..., "email": "23f3002663@ds.study.iitm.ac.in" }

The Worker must:
- Implement correct reverse logic based on `type`
- Support CORS
- Handle OPTIONS preflight requests

---

## Reverse Rules Implemented

Given `{ type, value }`, compute `reversed` as:

- type = "string" → reverse characters  
  Example: "abcd" → "dcba"

- type = "array" → reverse array elements  
  Example: [1,2,3] → [3,2,1]

- type = "words" → reverse word order  
  Example: "i love tds" → "tds love i"

- type = "number" → reverse digits and return as integer  
  Example: 25988 → 88952

---

## Project Setup

### Step 1 — Initialize Worker

    mkdir -p GA2/ga2-q15-worker
    cd GA2/ga2-q15-worker
    wrangler init

Selections during setup:
- Start with: Hello World example
- Template: Worker only
- Language: JavaScript
- AGENTS.md: No
- Git integration: Yes
- Deploy immediately: No

---

## Worker Implementation

### Step 2 — Replace src/index.js

```js
export default {
  async fetch(request) {
    const corsHeaders = {
      "Access-Control-Allow-Origin": "*",
      "Access-Control-Allow-Methods": "POST, OPTIONS",
      "Access-Control-Allow-Headers": "Content-Type",
    };

    // Handle CORS preflight
    if (request.method === "OPTIONS") {
      return new Response(null, { headers: corsHeaders });
    }

    const url = new URL(request.url);

    // Allow only POST /data
    if (url.pathname !== "/data" || request.method !== "POST") {
      return new Response("Not Found", { status: 404, headers: corsHeaders });
    }

    let body;
    try {
      body = await request.json();
    } catch {
      return new Response(JSON.stringify({ error: "Invalid JSON" }), {
        status: 400,
        headers: { ...corsHeaders, "Content-Type": "application/json" },
      });
    }

    const { type, value } = body;
    let reversed;

    if (type === "string") {
      reversed = String(value).split("").reverse().join("");
    } 
    else if (type === "array") {
      if (!Array.isArray(value)) {
        return new Response(JSON.stringify({ error: "value must be array" }), {
          status: 400,
          headers: { ...corsHeaders, "Content-Type": "application/json" },
        });
      }
      reversed = [...value].reverse();
    } 
    else if (type === "words") {
      reversed = String(value).trim().split(/\s+/).reverse().join(" ");
    } 
    else if (type === "number") {
      const s = String(value);
      reversed = parseInt(s.split("").reverse().join(""), 10);
    } 
    else {
      return new Response(JSON.stringify({ error: "Unknown type" }), {
        status: 400,
        headers: { ...corsHeaders, "Content-Type": "application/json" },
      });
    }

    const out = {
      reversed,
      email: "23f3002663@ds.study.iitm.ac.in",
    };

    return new Response(JSON.stringify(out), {
      headers: { ...corsHeaders, "Content-Type": "application/json" },
    });
  },
};
