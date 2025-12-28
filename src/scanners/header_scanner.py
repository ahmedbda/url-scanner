import httpx

class HeaderScanner():
    def scan(self, url: str):
        # changing the "python-httpx" default header for privacy and professionalism
        headers_request = {"User-Agent": "url-scanner/1.0"}
        headers_to_scan = ["hsts", "Strict-Transport-Security", "Content-Security-Policy", "X-Frame-Options"]
        analysis_results = {}

        try:
            response = httpx.get(url, headers=headers_request, timeout=5) # 5 second timeout to not get flagged
            received_headers = response.headers
        
        except httpx.RequestError as exc:
            print(f"Error connecting to {url}: {exc}")
            return None
        
        for header in headers_to_scan:
                if header in received_headers:
                    analysis_results[header] = received_headers.get(header)

                else:
                    analysis_results[header] = "Missing"
        
        return analysis_results