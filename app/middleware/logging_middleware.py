import logging
import time

from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.requests import Request
from starlette.responses import Response

logger = logging.getLogger(__name__)


class LoggerMiddleware(BaseHTTPMiddleware):
    async def dispatch(
        self, request: Request, call_next: RequestResponseEndpoint
    ) -> Response:
        start_time = time.time()
        response = await call_next(request)
        status_code = response.status_code
        client = request.client
        end_time = f"{time.time() - start_time:.3f}s."
        extra = {
            "request_url": request.url,
            "request_method": request.method,
            "request_path": request.url.path,
            "request_size": int(request.headers.get("content-length", 0)),
            "request_hosnent": f"{client.host}:{client.port}" if client else "",
            "response_status": status_code,
            "response_size": int(response.headers.get("content-length", 0)),
            "response_duration": end_time,
        }
        if status_code < 300:
            logger.info("Success response", extra=extra)
        elif status_code < 400:
            logger.info("Redirect response", extra=extra)
        elif status_code < 500:
            logger.warning("Client request error", extra=extra)
        else:
            logger.error("Server response error", extra=extra)

        return response
