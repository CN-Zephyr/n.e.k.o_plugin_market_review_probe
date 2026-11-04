from plugin.sdk.plugin import NekoPluginBase, Ok, neko_plugin, plugin_entry


@neko_plugin
class MarketReviewProbePlugin(NekoPluginBase):
    @plugin_entry(id="probe", name="Market review probe", description="Return a fixed test marker")
    async def probe(self, **_):
        return Ok({"message": "pilot-baseline"})
