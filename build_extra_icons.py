#!/usr/bin/env python3

from builder.basic_builder import BasicBuildSettings, build_basic_pack


def main():
    settings = BasicBuildSettings()
    settings.repo_url = "https://github.com/stratumauth/app.git"
    settings.png_glob = ["extraicons", "*.png"]
    settings.output_name = "extra-icons"
    settings.pack_name = "Extra Icons"
    settings.pack_description = (
        "Icons that don't fit the inclusion criteria or that were removed"
    )
    settings.pack_url = "https://github.com/stratumauth/app"

    build_basic_pack(settings)


if __name__ == "__main__":
    main()
