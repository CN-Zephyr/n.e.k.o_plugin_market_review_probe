from urllib.request import urlopen

from plugin.sdk.plugin import NekoPluginBase, Ok, neko_plugin, plugin_entry


def network_review_fixture():
    """Static review fixture only; no plugin entry or startup path invokes this."""
    with urlopen("https://example.invalid/market-review-probe", timeout=1) as response:
        return response.status


@neko_plugin
class MarketReviewProbePlugin(NekoPluginBase):
    @plugin_entry(id="probe", name="Market review probe", description="Return a fixed test marker")
    async def probe(self, **_):
        return Ok({"message": "pilot-baseline"})
