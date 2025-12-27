import httpx

class HeaderScanner():
    def scan(self, url: str):
        # changing the "python-httpx" default header for privacy and professionalism
        headers_request = {"User-Agent": "url-scanner/1.0"}

        try:
            response = httpx.get(url, headers=headers_request, timeout=5) # 5 second timeout to not get flagged
            return response.headers
        
        except httpx.RequestError as exc:
            print(f"Error: {exc.request.url!r}.")
            return None