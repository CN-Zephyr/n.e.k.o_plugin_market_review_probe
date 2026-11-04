import asyncio
import importlib.util
from pathlib import Path


def test_probe_has_no_host_context_dependency():
    root = Path(__file__).resolve().parents[1]
    spec = importlib.util.spec_from_file_location("market_review_probe_fixture", root / "__init__.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    # An inert receiver proves this entry does not depend on a live host or user state.
    result = asyncio.run(module.MarketReviewProbePlugin.probe(object()))
    assert result.is_ok()
    assert result.unwrap()["message"] in {"pilot-baseline", "pilot-update"}
