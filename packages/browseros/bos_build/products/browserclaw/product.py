#!/usr/bin/env python3
"""BrowserOS neo — the browser for web agents."""

from pathlib import Path

from ...core.products import (
    BROWSEROS_BUG_REPORTER_EXTENSION_ID,
    BROWSERCLAW_EXTENSION_ID,
    MacProductIdentity,
    ProductDescriptor,
    WindowsProductIdentity,
)
from ..server_binaries import ServerBundle, SignSpec

BROWSERCLAW_PRODUCT = ProductDescriptor.define(
    id="browserclaw",
    display_name="RemocodeBrowser neo",
    company="Remocode",
    homepage_url="https://github.com/BlueOriginAI/RemocodeBrowser",
    support_url="https://github.com/BlueOriginAI/RemocodeBrowser/issues",
    bugtracker_url="https://github.com/BlueOriginAI/RemocodeBrowser/issues",
    windows_installer_guid="{FA2AFFF8-647B-477C-A5D2-905BA8DB9B82}",
    summary="The open source browser for web agents",
    description="RemocodeBrowser neo is an open-source browser for agent workflows based on BrowserOS.",
    required_extensions=(
        (BROWSERCLAW_EXTENSION_ID, "RemocodeBrowser neo app"),
        (BROWSEROS_BUG_REPORTER_EXTENSION_ID, "RemocodeBrowser bug reporter"),
    ),
    server_bundle_ids=("browserclaw-server",),
    artifact_prefix="RemocodeBrowser_neo",
    mac=MacProductIdentity(
        bundle_id="com.remocode.RemocodeBrowserNeo",
        dev_bundle_id="com.remocode.dev.RemocodeBrowserNeo",
        signing_identifier="com.remocode.RemocodeBrowserNeo",
        dev_signing_identifier="com.remocode.dev.RemocodeBrowserNeo",
        framework_name="RemocodeBrowser neo Framework.framework",
        dev_framework_name="RemocodeBrowser neo Dev Framework.framework",
        dmg_volume_name="RemocodeBrowser neo",
    ),
    windows=WindowsProductIdentity(
        app_user_model_id="Remocode.RemocodeBrowserNeo",
        installer_app_id="{FA2AFFF8-647B-477C-A5D2-905BA8DB9B82}",
    ),
)

BROWSERCLAW_SERVER_BUNDLE = ServerBundle(
    id="browserclaw-server",
    name="BrowserOS Claw Server",
    product_ids=("browserclaw",),
    chromium_output_root="BrowserClawServer",
    local_resources_root=Path("resources/binaries/browseros_claw_server_rust"),
    chromium_resources_root=Path("chrome/browser/browseros/claw_server/resources"),
    macos_bundle_resources_root=Path(
        "Contents/Resources/BrowserClawServer/default/resources"
    ),
    windows_bundle_resources_root=Path("BrowserClawServer/default/resources"),
    macos_binaries={
        "browseros-claw-server": SignSpec(
            "browseros_claw_server",
            "runtime",
            "browseros-executable-entitlements.plist",
        ),
    },
    windows_binaries=("browseros-claw-server.exe",),
    source_builder="cargo",
    source_component="claw-server-rust",
    runtime_binary_name="browseros-claw-server",
    required_in_chromium_output=False,
    unsigned_artifact_prefix="claw-server-rust/prod-resources",
    unsigned_artifact_base_name="browseros-claw-server-rust-resources",
)
