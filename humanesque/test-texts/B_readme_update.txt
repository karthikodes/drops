## v2.1

Two changes in this release.

**Offline mode.** Commands queue locally when you have no connection and sync when you reconnect. No configuration needed.

**Faster sync.** The sync engine now diffs incrementally and only transfers changed files. On workspaces over 10,000 files, sync runs roughly 4x faster than v2.0.

Also fixed: startup time is down about 30%, authentication errors now explain what failed, and a race condition no longer duplicates entries during concurrent syncs.

Upgrade with `tool upgrade`. If something breaks, open an issue.
