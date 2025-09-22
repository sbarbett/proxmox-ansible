# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.0.5] - 2025-09-21

### Added
- Support for password authentication
- Support for mounts

### Changed
- `neofetch` swapped out for `fastfetch` in container extras
- Updated `community.general.proxmox` to `community.proxmox.proxmox`

### Fixed
- Fallback to non-root user if root connect fails

## [1.0.4] - 2025-04-02

### Added
- Added ble.sh installation to container extras role
  - Installs ble.sh from source
  - Configures ble.sh in user's .bashrc
  - Automatically cleans up after installation

### Changed
- Improved code quality and linting compliance
  - Added proper changed_when conditions to file operations
  - Replaced shell commands with appropriate Ansible modules
  - Added task names for better readability
  - Updated Ansible version requirement to >=2.18.0

## [1.0.3] - 2025-02-24

### Added
- New Docker Compose manifest for Pi-hole v6
  - Updated for Pi-hole's new architecture and API
  - Added pihole-unbound flag for lightweight stack deployment
  - Preconfigured Unbound for upstream recursion
  - Future plans for DNS over HTTPS (DoH) support

### Changed
- Major repository structural improvements
  - Cleaned up unnecessary files
  - Improved organization
  - Added automated workflow for Ansible Galaxy releases 