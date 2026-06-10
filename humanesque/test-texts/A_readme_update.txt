## What's New in v2.1

This release focuses on two of the most requested features from the community: working without a connection, and getting your data where it needs to be — faster.

**Offline Mode** 🔌
You can now use the CLI entirely offline. All commands queue locally and sync automatically the next time you're connected. No configuration required — it just works.

**Faster Sync** ⚡
We've rewritten the sync engine from the ground up. Incremental diffing means we only transfer what's changed, resulting in sync times that are up to 4x faster on large workspaces.

**Other improvements:**
- Reduced startup time by ~30%
- Clearer error messages when authentication fails
- Fixed a race condition that could duplicate entries during concurrent syncs

As always, upgrading is a single command: `tool upgrade`. Full changelog below. If you run into any issues, open an issue — we read every single one.
