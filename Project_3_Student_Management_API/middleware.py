from fastapi import Request


async def log_requests(request: Request, call_next):
    print(f"Request Started: {request.method} {request.url.path}")

    response = await call_next(request)

    print(f"Request Finished: {response.status_code}")

    return response