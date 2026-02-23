from http.server import BaseHTTPRequestHandler
import json
from pathlib import Path
from statistics import mean

class handler(BaseHTTPRequestHandler):

    def _cors(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "*")

    def do_OPTIONS(self):
        self.send_response(200)
        self._cors()
        self.end_headers()

    def do_POST(self):
        try:
            length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(length).decode("utf-8")
            payload = json.loads(body)

            regions = payload.get("regions", [])
            threshold_ms = payload.get("threshold_ms", 180)

            data_path = (Path(__file__).resolve().parent / ".." / "q-vercel-latency.json").resolve()
            with open(data_path, "r", encoding="utf-8") as f:
                data = json.load(f)

            if isinstance(data, dict) and "records" in data:
                records = data["records"]
            else:
                records = data

            out = {}

            for region in regions:
                region_records = [r for r in records if r.get("region") == region]

                latencies = [float(r.get("latency_ms", 0)) for r in region_records]
                uptimes = [1.0 if r.get("uptime", 1) else 0.0 for r in region_records]

                avg_latency = mean(latencies) if latencies else 0.0
                sorted_lat = sorted(latencies)
                p95_latency = sorted_lat[int(0.95 * len(sorted_lat))] if sorted_lat else 0.0
                avg_uptime = mean(uptimes) if uptimes else 0.0
                breaches = sum(1 for x in latencies if x > float(threshold_ms))

                out[region] = {
                    "avg_latency": avg_latency,
                    "p95_latency": p95_latency,
                    "avg_uptime": avg_uptime,
                    "breaches": breaches
                }

            self.send_response(200)
            self._cors()
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(out).encode("utf-8"))

        except Exception as e:
            self.send_response(500)
            self._cors()
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"error": str(e)}).encode("utf-8"))
