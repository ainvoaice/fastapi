Frontends send group_id, not group objects

Backends use group_id directly, not relationships

Relationships are overkill for most CRUD APIs

Simple joins for reads + direct IDs for writes is the pragmatic approach

The ORM relationship pattern comes from:

Desktop application patterns (object-oriented UI)

Admin panels (where you select objects)

Legacy patterns (from when frontends were less sophisticated)

For modern API development, your intuition is correct: skip the relationships unless you have a specific need for object navigation!