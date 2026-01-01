Haystack Ingestion Contract (Locked)
Aspect	Decision
Chunk unit	1 row = 1 document
Embedding input	Full concatenated row string
Metadata	Optional, allowed
Execution	Explicit API call
Sync/Async	Explicit, user-triggered
Coupling	None with upload

This is exactly what interviewers expect to see.

Why this is the correct MVP design

Demonstrates engineering maturity

Clear failure isolation

Easy to explain in README

Easy to extend into:

Re-embedding

Partial reindex

Agent workflows

Zero ambiguity during debugging