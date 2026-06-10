## v2.1

Offline mode is here. Commands queue locally when you lose connection and sync when you're back. Nothing to configure.

Sync got a rewrite too. We stopped shipping full state on every sync and now send incremental diffs only. Real numbers from our test workspace: 12,000 files went from 41 seconds to about 10.

Three smaller things. Startup is around 30% quicker. Auth errors now tell you which credential failed instead of a generic message. And a race condition that duplicated entries during concurrent syncs is fixed.

Run `tool upgrade` and you're done.
