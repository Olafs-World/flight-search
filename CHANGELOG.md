# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.5] - 2026-02-06

### Added
- `--upgrade` flag to self-update (auto-detects uv/pipx/pip)

## [0.1.4] - 2026-02-06

### Added
- `--version` / `-v` flag to show version
- README: Added "Updating" section with upgrade commands

## [0.1.3] - 2026-02-06

### Fixed
- Use "common" fetch mode instead of "fallback" (fixes 401 token error)

## [0.1.2] - 2026-02-06

### Changed
- README: Added example output at top
- README: Added troubleshooting section for 401 errors
- README: Removed duplicate example output section

## [0.1.1] - 2026-02-06

### Fixed
- Use absolute URL for banner image on PyPI

## [0.1.0] - 2026-02-06

### Added
- Initial release
- Search Google Flights from the command line
- One-way and round-trip support
- Multiple seat classes (economy, premium-economy, business, first)
- Passenger count options (adults, children)
- Text and JSON output formats
- Built on [fast-flights](https://github.com/AWeirdDev/flights)
